from pydantic import BaseModel


class VlanSchemaImput(BaseModel):
    tenant_name: str
    application_name: str
    vlan_name: str
    alias: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "tenant_name": "tenant_example",
                    "application_name": "application_example",
                    "vlan_name": "vlan_example",
                    "alias": "alias_example",
                }
            ]
        }
    }
