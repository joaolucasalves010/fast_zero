from typing import Annotated

from fastapi import Depends, FastAPI, Body

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


@app.get("/items/")
async def read_items(commons: Annotated[CommonQueryParams, Depends(CommonQueryParams)], tag: str = None):
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    if tag:
        response.update({"tag": tag})
    items = fake_items_db[commons.skip: commons.skip + commons.limit]
    response.update({"items": items})
    return response

@app.get("/users/")
async def read_users(commons: Annotated[dict, Depends(common_parameters)], username: str):
    commons.update(username)
    return commons