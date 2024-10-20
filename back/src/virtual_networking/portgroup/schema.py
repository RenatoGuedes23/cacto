from typing import List
from pydantic import BaseModel


class PortGroupSchemaImput(BaseModel):
    vmware_name: str
    portgoup_name: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                 "vmware_name": "vmware_example",
                 "portgoup_name": "port_group_example"}
            ]
        }
    }


class AttributesInfoSchema(BaseModel):
    aggrImedcy: str
    allocMode: str
    annotation: str
    bdDn: str
    bindingType: str
    blockAllPorts: str
    cfgdDelimiter: str
    childAction: str
    classPref: str
    configFlags: str
    crtrnEnabled: str
    ctxDn: str
    customEpgName: str
    deployIssues: str
    descr: str
    dn: str
    domName: str
    encap: str
    encapAllocKey: str
    encapChanged: str
    encapCtx: str
    encapMode: str
    encapModeOverride: str
    epgCos: str
    epgCosPref: str
    epgPKey: str
    eppDn: str
    extMngdBy: str
    faultDKey: str
    featureFlags: str
    forgedTransmit: str
    id: str
    idConsumerDn: str
    instrImedcy: str
    intraSecConf: str
    issues: str
    lagPolicyName: str
    lbAlgo: str
    lcOwn: str
    macChange: str
    mcastAddr: str
    modTs: str
    monPolDn: str
    name: str
    nameAlias: str
    netflowDir: str
    netflowPref: str
    numPorts: str
    operDelimiter: str
    pcEnfPref: str
    portAllocation: str
    primaryEncap: str
    primaryEncapInner: str
    promMode: str
    resImedcy: str
    secondaryEncapInner: str
    statsCollectionState: str
    status: str
    switchingMode: str
    txId: str
    type: str
    uid: str
    untagged: str
    updateTs: str
    userdom: str
    vnetOnly: str
    
class AttributesSchema(BaseModel):
    attributes: AttributesInfoSchema

class VmmUsrAggrPgSchema(BaseModel):
    vmmUsrAggr: AttributesSchema

class PortGroupSchemaOutput(BaseModel):

    totalCount: str
    imdata: List[VmmUsrAggrPgSchema]
