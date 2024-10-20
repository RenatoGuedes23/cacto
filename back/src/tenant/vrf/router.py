import json

from fastapi import APIRouter, Depends, status, Request, Response, HTTPException
from fastapi.responses import JSONResponse

from config.request.base_session import requests_session
from config.logger.base_logger import logger
from config.security.security import JWTBearer
from src.tenant.vrf.schemas import VrfSchemaImput, VrfSchemaOutput



vrf_router = APIRouter(
    prefix="/vrf",
    tags=["vrf"],
)



@vrf_router.get(
    "/{tenant_name}",
    response_model=VrfSchemaOutput,
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(JWTBearer())],
)
async def get_epg(
    ip_address: str,
    tenant_name: str,
    request: Request):
    try:
        url = f"https://{ip_address}/api/node/mo/uni/tn-{tenant_name}.json?query-target=children&target-subtree-class=fvCtx&query-target-filter=and(not(wcard(fvCtx.dn,%22__ui_%22)),not(wcard(fvCtx.annotation,%22shadow:yes%22)))&order-by=fvCtx.name|asc"
        
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


@vrf_router.post(
    "",
    dependencies=[Depends(JWTBearer())],
    description="Use this endpoint to create vrf in the tenant",
)
async def create_vrf(
    ip_address: str, 
    vrf: VrfSchemaImput, 
    request: Request
):
    try:


        url = f"https://{ip_address}/api/node/mo/uni/tn-{vrf.tenant_name}.json"
        # "fvCtx":{"attributes":{"dn":"uni/tn-ntt_0001/ctx-ntt_vrf_0002","name":"ntt_vrf_0002","nameAlias":"ntt_vrf_0002","rn":"ctx-ntt_vrf_0002","status":"created"},"children":[]
        request_body = {
            "fvCtx": {
                "attributes": {
                    "dn": f"uni/tn-{vrf.tenant_name}/ctx-{vrf.name}",
                    "name": vrf.name,
                    "nameAlias": vrf.alias,
                    "rn": f"ctx-{vrf.name}",
                    "status": "created",
                },
                "children": [],
            }
        }

        response = requests_session.post(
            url=url,
            json=request_body,
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
        print(e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Request cannot be completed with the current parameters or it already exist: {str(e)}",
        )





@vrf_router.delete(
    "/{tenant_name}/{vrf_name}",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(JWTBearer())],
)
async def get_epg(
    ip_address: str,
    tenant_name: str,
    vrf_name: str,
    request: Request):
    try:
        url = f"https://{ip_address}/api/node/mo/uni/tn-{tenant_name}/ctx-{vrf_name}.json"
        
        response = requests_session.delete(
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

