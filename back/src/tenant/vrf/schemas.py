from typing import List
from pydantic import BaseModel


class VrfSchemaImput(BaseModel):
    tenant_name: str
    name: str
    alias: str


    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "tenant_name": "TSW_Tenant0",
                    "name": "teste_example",
                    "alias": "alias_example",
                }
            ]
        }
    }


class AttributesInfoSchema(BaseModel):
    annotation: str
    bdEnforcedEnable: str
    childAction: str
    descr: str
    dn: str
    extMngdBy: str
    ipDataPlaneLearning: str
    knwMcastAct: str
    lcOwn: str
    modTs: str
    monPolDn: str
    name: str
    nameAlias: str
    ownerKey: str
    ownerTag: str
    pcEnfDir: str
    pcEnfDirUpdated: str
    pcEnfPref: str
    pcTag: str
    scope: str
    seg: str
    status: str
    uid: str
    userdom: str
    vrfId: str
    vrfIndex: str

class AttributesSchema(BaseModel):
    attributes: AttributesInfoSchema
    
class FvCtxSchema(BaseModel):
    fvAp: AttributesSchema

class VrfSchemaOutput(BaseModel):
    totalCount: str
    imdata: List[FvCtxSchema]
    