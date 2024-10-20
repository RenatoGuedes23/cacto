from pydantic import BaseModel



class PhysicalInterfaceSchema(BaseModel):
    pod_name: str
    leaf_name: str
    eth_port_name: str


class EnablePhysicalInterfaceSchema(PhysicalInterfaceSchema):
    model_config = {
        "json_schema_extra": {
            "examples": [
                {"pod_name": "1", "leaf_name": "102", "eth_port_name": "eth1/1"}
            ]
        }
    }


class DisablePhysicalInterfaceSchema(PhysicalInterfaceSchema):
    model_config = {
        "json_schema_extra": {
            "examples": [
                {"pod_name": "1", "leaf_name": "102", "eth_port_name": "eth1/1"}
            ]
        }
    }
