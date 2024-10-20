from pydantic import BaseModel


class TenantSchemaImput(BaseModel):
    dn: str
    name: str
    nameAlias: str
    descr: str
    rn: str
    # children: list = []

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "dn": "teste",
                    "name": "teste",
                    "nameAlias": "teste",
                    "descr": "description",
                    "rn": "teste",
                }
            ]
        }
    }
