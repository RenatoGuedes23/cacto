import json
from fastapi import APIRouter, Depends, status, Request, HTTPException
from fastapi.responses import JSONResponse

from config.request.base_session import requests_session
from config.logger.base_logger import logger
from config.security.security import JWTBearer

from src.virtual_networking.vmware.schema import VMWareSchemaImput, VMwareSchemaOutput

vmware_router = APIRouter(
    prefix="/vmware",
    tags=["vmware"],
    responses={404: {"description": "Not found"}},
)


@vmware_router.get(
    "",
    response_model=VMwareSchemaOutput,
    dependencies=[Depends(JWTBearer())],
    status_code=status.HTTP_200_OK
    )
async def get_vmware(
    ip_address: str,
    request: Request):
    try:
        url = f"https://{ip_address}/api/node/mo/comp/prov-VMware.json?query-target=children&target-subtree-class=compDom&query-target-filter=ne(compDom.mode,%22nsx%22)"

        response = requests_session.get(
            url=url,
            verify=False,
            cookies={"APIC-Cookie": request.headers.get("Authorization").split()[1]},
        )

        if response.status_code == 200:
            return JSONResponse(
                status_code=200,
                content=response.json(),
            )

        else:
            return JSONResponse(
                    status_code=response.status_code,
                    content=response.json(),
                )

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Request cannot be completed with the current parameters: {str(e)}",
        )


@vmware_router.post(
    "",
    dependencies=[Depends(JWTBearer())],
    status_code=status.HTTP_200_OK
    )
async def create_vmware(
    vmware: VMWareSchemaImput,
    ip_address:str,
    request: Request):
    try:


        url = f"https://{ip_address}/api/node/mo/uni/vmmp-VMware/dom-{vmware.vmware_name}.json"

        request_body = {
            "vmmDomP": {
                "attributes": {
                    "dn": f"uni/vmmp-VMware/dom-{vmware.vmware_name}",
                    "name": f"{vmware.vmware_name}",
                    "rn": f"dom-{vmware.vmware_name}",
                    "status": "created",
                },
                "children": [
                    {
                        "aaaDomainRef": {
                            "attributes": {
                                "dn": f"uni/vmmp-VMware/dom-{vmware.vmware_name}/domain-security_0001g",
                                "name": "security_0001g",
                                "rn": "domain-security_0001g",
                                "status": "created",
                            },
                            "children": [],
                        }
                    },
                    {
                        "vmmVSwitchPolicyCont": {
                            "attributes": {
                                "dn": f"uni/vmmp-VMware/dom-{vmware.vmware_name}/vswitchpolcont",
                                "status": "created,modified",
                            },
                            "children": [],
                        }
                    },
                ],
            }
        }
        response = requests_session.post(
            url=url,
            verify=False,
            json=request_body,
            cookies={"APIC-Cookie": request.headers.get("Authorization").split()[1]},
        )

        if response.status_code == 200:
            return JSONResponse(
                status_code=200,
                content=response.json(),
            )

        else:
            return JSONResponse(
                    status_code=response.status_code,
                    content=response.json(),
                )
            
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Request cannot be completed with the current parameters: {str(e)}",
        )




@vmware_router.delete(
    "/{vmware_name}",
    dependencies=[Depends(JWTBearer())]
)
async def delete_application(
    ip_address: str,
    vmware_name: str,
    request: Request
):
    try:
        url = f"https://{ip_address}/api/node/mo/uni/vmmp-VMware/dom-{vmware_name}.json"

        response = requests_session.delete(
            url=url,
            verify=False,
            cookies={"APIC-Cookie": request.headers.get("Authorization").split()[1]},
        )

        if response.status_code == 200:
            json_response = json.loads(response.text)

            return JSONResponse(status_code=200, content=json_response)

        else:
            return JSONResponse(
                status_code=response.status_code,
                content=response.json(),
            )

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Request cannot be completed with the current parameters: {str(e)}",
        )
