from pydantic import BaseModel
from typing import List, Dict


class ApplicationSchemaImput(BaseModel):
    tenant_name: str
    application_name: str
    alias: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "tenant_name": "tenant_name_test",
                    "application_name": "app_name_test",
                    "alias": " alias_test",
                }
            ]
        }
    }


class AttributesInfoSchema(BaseModel):
    annotation: str
    childAction: str
    descr: str
    dn: str
    extMngdBy: str
    lcOwn: str
    modTs: str
    monPolDn: str
    name: str
    nameAlias: str
    ownerKey: str
    ownerTag: str
    prio: str
    status: str
    uid: str
    userdom: str


class AttributesSchema(BaseModel):
    attributes: AttributesInfoSchema


class FvApSchema(BaseModel):
    fvAp: AttributesSchema


class ApplicationSchemaOutput(BaseModel):

    totalCount: str
    imdata: List[FvApSchema]
