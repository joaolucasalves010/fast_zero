from typing import Annotated

from fastapi import Depends, FastAPI, Body, Cookie

app = FastAPI()

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
async def read_query(query_or_default: Annotated[str, Depends(query_or_cookie_extractor)],
):
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
    return {"q_or_cookie": query_or_default}
    

@app.get("/users/")
async def read_users(commons: Annotated[dict, Depends(common_parameters)], username: str):
    commons.update(username)
    return commons
