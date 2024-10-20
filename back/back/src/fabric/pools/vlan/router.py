import json
from fastapi import APIRouter, Depends, status, Request, HTTPException
from fastapi.responses import JSONResponse

from config.request.base_session import requests_session
from config.logger.base_logger import logger
from config.security.security import JWTBearer
from src.fabric.pools.vlan.schemas import VlanSchemaImput


vlan_router = APIRouter(
    prefix="/pools/vlan",
    tags=["vlan"],
    responses={404: {"description": "Not found"}},
)


@vlan_router.get(
    "",
    dependencies=[Depends(JWTBearer())],
    status_code=status.HTTP_200_OK)
async def get_vlan(ip_address: str, request: Request):
    try:
        
        url = f"https://{ip_address}/api/node/mo/uni/infra.json?"\
            "query-target=subtree&target-subtree-class=fvnsVlanInstP&query-target-filter="\
            "not(wcard(fvnsVlanInstP.dn,%22__ui_%22))&query-target=subtree&rsp-subtree=full&rsp-subtree-class=tagAliasInst"

        response = requests_session.get(
            url=url,
            verify=False,
            cookies={"APIC-Cookie": request.headers.get("Authorization")},
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


@vlan_router.post(
    "",
    dependencies=[Depends(JWTBearer())],
    status_code=status.HTTP_200_OK)
async def create_vlan(
    vlan: VlanSchemaImput,
    ip_address: str,
    request: Request,
):
    try:
        url = f"https://{ip_address}/api/node/mo/uni/tn-{vlan.tenant_name}/ap-{vlan.application_name}/vlan-{vlan.vlan_name}.json"

        request_body = {
            "fvAEPg": {
                "attributes": {
                    "dn": f"uni/tn-{vlan.tenant_name}/ap-{vlan.application_name}/vlan-{vlan.vlan_name}",
                    "name": f"{vlan.vlan_name}",
                    "nameAlias": f"{vlan.alias}",
                    "rn": f"vlan-{vlan.vlan_name}",
                    "status": "created",
                },
            }
        }
        response = requests_session.post(
            url=url,
            verify=False,
            json=request_body,
            cookies={"APIC-Cookie": request.headers.get("Authorization")},
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
