from pydantic import BaseModel


# url: https://198.18.133.200/api/node/mo/uni/tn-ntt_example/ap-ntt_application_example/epg-ntt_epg_example.json
# payload{"fvRsIntraEpg":{"attributes":{"tnVzBrCPName":"contract_ntt_example","status":"created,modified"},"children":[]}}
# response: {"totalCount":"0","imdata":[]}
class ConsumedContractEpgImput(BaseModel):
    tenant_name: str
    application_name: str
    epg_name: str
    contract_name: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "tenant_name": "ntt_example",
                    "application_name": "ntt_application_example",
                    "epg_name": "ntt_epg_example",
                    "contract_name": "contract_ntt_example",
                }
            ]
        }
    }


class DeleteConsumedContractEpgImput(BaseModel):
    tenant_name: str
    application_name: str
    epg_name: str
    contract_name: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "tenant_name": "ntt_example",
                    "application_name": "ntt_application_example",
                    "epg_name": "ntt_epg_example",
                    "contract_name": "contract_ntt_example",
                }
            ]
        }
    }


class AssociateContract(BaseModel):
    tenant_name: str
    ext_epg_name: str
    contract_name: str
    l3out_name: str
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "tenant_name": "ntt_example", 
                    "l3out_name": "l3out_example",
                    "epg_name": "ext_epg_example",
                    "contract_name": "contract_ntt_example",
                }
            ]
        }
    }
