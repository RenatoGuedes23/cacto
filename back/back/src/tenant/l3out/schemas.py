from typing import List
from pydantic import BaseModel


class L3outSchemaImput(BaseModel):
    tenant_name: str
    l3out_name: str
    vrf: str
    ext_dom: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "tenant_name": "tenant_example",
                    "l3out_name": "l3out__example",
                    "vrf": "vrf_example",
                    "ext_dom": "ext_dom_example"
                }
            ]
        }
    }


class AttributesInfoSchema(BaseModel):
    annotation: str
    childAction: str
    descr: str
    dn: str
    enforceRtctrl: str
    extMngdBy: str
    lcOwn: str
    modTs: str
    monPolDn: str
    mplsEnabled: str
    name: str
    nameAlias: str
    ownerKey: str
    ownerTag: str
    status: str
    targetDscp: str
    uid: str
    userdom: str

class AttributesSchema(BaseModel):
    attributes: AttributesInfoSchema

class L3extOutPgSchema(BaseModel):
    fvAEPg: AttributesSchema

class L3outSchemaOutput(BaseModel):

    totalCount: str
    imdata: List[L3extOutPgSchema]
