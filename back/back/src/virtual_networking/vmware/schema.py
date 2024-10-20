from typing import List
from pydantic import BaseModel


class VMWareSchemaImput(BaseModel):
    vmware_name: str

    model_config = {
        "json_schema_extra": {
            "examples": [{"vmware_name": "vmware_example"}]
        }
    }



class AttributesInfoSchema(BaseModel):
    childAction: str
    descr: str
    dn: str
    enableAVE: str
    id: str
    issues: str
    lcOwn: str
    modTs: str
    mode: str
    monPolDn: str
    name: str
    nameAlias: str
    status: str
    
class AttributesSchema(BaseModel):
    attributes: AttributesInfoSchema

class CompDomPgSchema(BaseModel):
    compDom: AttributesSchema

class VMwareSchemaOutput(BaseModel):

    totalCount: str
    imdata: List[CompDomPgSchema]
