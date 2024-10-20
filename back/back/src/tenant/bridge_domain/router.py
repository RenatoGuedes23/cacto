from fastapi import APIRouter, Depends, status, Request, Response, HTTPException
from fastapi.responses import JSONResponse

from config.security.security import JWTBearer
from src.tenant.bridge_domain.schemas import BridgeDomainSchemaImput, BridgeDomainSchemaOutput

from config.request.base_session import requests_session
from config.logger.base_logger import logger

bridge_domain_router = APIRouter(
    prefix="/bridge-domain",
    tags=["bridge-domain"],
    responses={404: {"description": "Not found"}},
)


@bridge_domain_router.get(
    "/{tenant_name}",
    response_model=BridgeDomainSchemaOutput,
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(JWTBearer())],
)
async def get_bridge_domain(
    ip_address: str,
    tenant_name: str,
    request: Request):
    try:
        url = f"https://{ip_address}/api/node/mo/uni/tn-{tenant_name}.json?query-target=children&target-subtree-class=fvBD"
        
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



@bridge_domain_router.post(
    "",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(JWTBearer())])
async def create_bridge_domain(
    bridge_domain: BridgeDomainSchemaImput,
    ip_address: str,
    request: Request
):
    try:
        url = f"https://{ip_address}/api/node/mo/uni/tn-{bridge_domain.tenant_name}/BD-{bridge_domain.name}.json"


        request_body = {
            "fvBD": {
                "attributes": {
                    "dn": f"uni/tn-{bridge_domain.tenant_name}/BD-{bridge_domain.name}",
                    "mac": f"{bridge_domain.mac}",
                    "arpFlood": bridge_domain.arpFlood,
                    "name": bridge_domain.name,
                    "nameAlias": bridge_domain.nameAlias,
                    "descr": bridge_domain.descr,
                    "rn": f"BD-{bridge_domain.rn}",
                    "status": "created",
                },
                "children": bridge_domain.children,
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
                content={"message": f"{response.json()}"},
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



@bridge_domain_router.delete(
    "/{tenant_name}/{bridge_domain}",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(JWTBearer())],
)
async def delete_bridge_domain(
    ip_address: str,
    tenant_name: str,
    bridge_domain: str,
    request: Request):
    try:
        url = f"https://{ip_address}/api/node/mo/uni/tn-{tenant_name}/BD-{bridge_domain}.json?query-target=children&target-subtree-class=fvBD"
        
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

