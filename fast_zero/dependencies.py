from typing import Annotated

from fastapi import Depends, FastAPI, Body, Cookie, Header, HTTPException
from fastapi import status

def verify_token(token: Annotated[str, Header()]):
    if token != "fake-super-secret-token":
        raise HTTPException(status_code=401, detail="Token secret invalid")
    
def verify_key(key: Annotated[str, Header()]):
    if key != "fake-super-secret-key":
        raise HTTPException(status_code=401, detail="Key secret invalid")

app = FastAPI(dependencies=[Depends(verify_key), Depends(verify_token)])

async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}

CommonsDep = Annotated[dict, Depends(common_parameters)]

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# Dependencias como Classes
class CommonQueryParams:
    def __init__(self, q: str | None = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


def query_extractor(q: str | None = None):
    return q

def query_or_cookie_extractor(
    q: Annotated[str, Depends(query_extractor)],
    last_query: Annotated[str | None, Cookie()] = None
):
    if not q:
        return last_query
    return q


@app.get("/items/")
async def read_items():
    """
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    if tag:
        response.update({"tag": tag})
    items = fake_items_db[commons.skip: commons.skip + commons.limit]
    response.update({"items": items})
    return response
    """
    return [{"item": "Portal Gun"}, {"item": "Plumbus"}]
    

@app.get("/users/")
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]

fake_db_languages = [
  {
    "name": "Python",
    "description": "Readable, friendly, and secretly judging your indentation."
  },
  {
    "name": "JavaScript",
    "description": "Runs everywhere and behaves… questionably."
  },
  {
    "name": "Java",
    "description": "Verbose, strict, and very proud of it."
  },
  {
    "name": "Rust",
    "description": "Safe, fast, and emotionally demanding."
  }
]

@app.get("/languages/{name}", dependencies=[Depends(verify_token), Depends(verify_key)])
async def read_languages(name: str):
    for language in fake_db_languages:
        if language["name"].lower().strip() == name.lower().strip():
            return language
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found language")