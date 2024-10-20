from pydantic import BaseModel


class ApicLoginSchema(BaseModel):
    name: str
    pwd: str

    model_config = {
        "json_schema_extra": {"examples": [{"name": "admin", "pwd": "C1sco12345"}]}
    }
