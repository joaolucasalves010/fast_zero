from pydantic import BaseModel

class Cookies(BaseModel):
    model_config = {'extra': 'forbid'} # proibir cookies extras

    session_id: str
    fatebook_tracker: str | None = None
    googall_tracker: str | None = None