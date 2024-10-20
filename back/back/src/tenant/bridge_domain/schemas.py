from pydantic import BaseModel
from typing import List



class BridgeDomainSchemaImput(BaseModel):
    tenant_name: str
    dn: str
    mac: str
    arpFlood: str
    name: str
    nameAlias: str
    descr: str
    rn: str
    status: str
    children: List

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "tenant_name": "tenant_example",
                    "dn": "bridge_ntt_example",
                    "mac": "00:22:BD:F8:19:FF",
                    "arpFlood": "true",
                    "name": "bridge_ntt_example",
                    "nameAlias": "bridge_alias_ntt_example",
                    "descr": "description sample for payload",
                    "rn": "bridge_ntt_example",
                    "status": "created",
                    "children": [],
                }
            ]
        }
    }


class AttributesInfoSchema(BaseModel):
    OptimizeWanBandwidth: str
    annotation: str
    arpFlood: str
    bcastP: str
    childAction: str
    configIssues: str
    descr: str
    dn: str
    epClear: str
    epMoveDetectMode: str
    extMngdBy: str
    hostBasedRouting: str
    intersiteBumTrafficAllow: str
    intersiteL2Stretch: str
    ipLearning: str
    ipv6McastAllow: str
    lcOwn: str
    limitIpLearnToSubnets: str
    llAddr: str
    mac: str
    mcastAllow: str
    modTs: str
    monPolDn: str
    mtu: str
    multiDstPktAct: str
    name: str
    nameAlias: str
    ownerKey: str
    ownerTag: str
    pcTag: str
    scope: str
    seg: str
    status: str
    type: str
    uid: str
    unicastRoute: str
    unkMacUcastAct: str
    unkMcastAct: str
    userdom: str
    v6unkMcastAct: str
    vmac: str

class AttributesSchema(BaseModel):
    attributes: AttributesInfoSchema

class fvBDSchema(BaseModel):
    fvAEPg: AttributesSchema

class BridgeDomainSchemaOutput(BaseModel):

    totalCount: str
    imdata: List[fvBDSchema]