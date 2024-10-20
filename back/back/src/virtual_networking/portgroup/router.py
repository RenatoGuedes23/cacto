import json
from fastapi import APIRouter, Depends, status, Request, HTTPException
from fastapi.responses import JSONResponse

from config.request.base_session import requests_session
from config.logger.base_logger import logger

from config.security.security import JWTBearer
from src.virtual_networking.portgroup.schema import PortGroupSchemaImput, PortGroupSchemaOutput

portgroup_router = APIRouter(
    prefix="/portgroup",
    tags=["portgroup"],
    responses={404: {"description": "Not found"}},
)


@portgroup_router.get(
    "/{vmware}",
    response_model=PortGroupSchemaOutput,
    dependencies=[Depends(JWTBearer())],
    status_code=status.HTTP_200_OK
    )
async def get_portgroup(
    ip_address: str,
    vmware: str,
    request: Request):
    try:
        url = (
            f"https://{ip_address}/api/node/class/vmmUsrAggr.json?query-target-filter=and"
            f"(not(wcard(vmmUsrAggr.dn,%22__ui_%22)),eq(vmmUsrAggr.domName,%22{vmware}%22))"
            "&rsp-subtree=no&rsp-subtree-class=fvnsEncapBlk,vmmRsUsrAggrLagPolAtt"
        )

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


@portgroup_router.post(
    "",
    dependencies=[Depends(JWTBearer())],
    status_code=status.HTTP_200_OK)
async def create_portgroup(
    portgroup: PortGroupSchemaImput,
    ip_address: str,
    request: Request):
    try:

        url = f"https://{ip_address}/api/node/mo/uni/vmmp-VMware/dom-{portgroup.vmware_name}/usraggr-{portgroup.portgoup_name}.json"

        request_body = {
            "vmmUsrAggr": {
                "attributes": {
                    "dn": f"uni/vmmp-VMware/dom-{portgroup.vmware_name}/usraggr-{portgroup.portgoup_name}",
                    "name": f"{portgroup.portgoup_name}",
                    "rn": f"usraggr-{portgroup.portgoup_name}",
                    "status": "created",
                },
                "children": [],
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



@portgroup_router.delete(
    "/{vmware_name}/{port_group}",
    dependencies=[Depends(JWTBearer())]
)
async def delete_application(
    ip_address: str,
    vmware_name: str,
    port_group: str,
    request: Request
):
    try:
        url = f"https://{ip_address}/api/node/mo/uni/vmmp-VMware/dom-{vmware_name}/usraggr-{port_group}.json"

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
