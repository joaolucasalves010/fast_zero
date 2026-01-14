from pydantic import BaseModel

class CommonHeaders(BaseModel):
    # model_config = {'extra': 'forbid'} -> Proibir headers adicionais

    host: str
    save_data: bool
    if_modified_since: str | None = None
    traceparent: str | None = None
    x_tag: list[str] = []