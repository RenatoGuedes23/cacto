from pydantic import BaseModel
from typing import List, Dict


class EpgSchemaImput(BaseModel):
    tenant_name: str
    application_name: str
    epg_name: str
    alias: str
    bd_name: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "tenant_name": "tenant_example",
                    "application_name": "application_example",
                    "epg_name": "epg_example",
                    "alias": "alias_example",
                    "bd_name": "default",
                }
            ]
        }
    }


class AttributesInfoSchema(BaseModel):

    childAction: str
    configIssues: str
    configSt: str
    descr: str
    dn: str
    exceptionTag: str
    extMngdBy: str
    floodOnEncap:  str
    fwdCtrl: str
    hasMcastSource: str
    isAttrBasedEPg: str
    isSharedSrvMsiteEPg: str
    lcOwn: str
    matchT: str
    modTs: str
    monPolDn: str
    name: str
    nameAlias: str
    pcEnfPref: str
    pcTag: str
    pcTagAllocSrc: str
    prefGrMemb: str
    prio: str
    scope: str
    shutdown: str
    status: str
    triggerSt: str
    txId: str
    uid: str
    userdom: str
    
class AttributesSchema(BaseModel):
    attributes: AttributesInfoSchema

class FvAEPgSchema(BaseModel):
    fvAEPg: AttributesSchema

class EpgSchemaOutput(BaseModel):

    totalCount: str
    imdata: List[FvAEPgSchema]