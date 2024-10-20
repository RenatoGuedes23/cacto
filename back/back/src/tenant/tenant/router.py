import json

from fastapi import APIRouter, Depends, status, Request, Response, HTTPException
from fastapi.responses import JSONResponse

from config.request.base_session import requests_session
from config.logger.base_logger import logger
from config.security.security import JWTBearer
from src.tenant.tenant.schemas import TenantSchemaImput


tenant_router = APIRouter(
    prefix="/tenant",
    tags=["tenant"],
)


@tenant_router.get(
    "",
    dependencies=[Depends(JWTBearer())],
    description="Use this endpoint to list all tenants available in the host",
)
async def list_tenant(ip_address: str, request: Request):
    url = f"https://{ip_address}/api/node/class/fvTenant.json"

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



@tenant_router.post(
    "",
    dependencies=[Depends(JWTBearer())],
    description="Use this endpoint to create tenants in the host",
)
async def create_tenant(
    ip_address: str,
    tenant: TenantSchemaImput,
    request: Request
):
    try:

        url = f"https://{ip_address}/api/node/mo/uni/tn-{tenant.name}.json"

        request_body = {
            "fvTenant": {
                "attributes": {
                    "dn": f"uni/tn-{tenant.dn}",
                    "name": tenant.name,
                    "nameAlias": tenant.nameAlias,
                    "descr": tenant.descr,
                    "rn": f"tn-{tenant.name}",
                    "status": "created",
                },
                "children": [
                    {
                        "tagAnnotation": {
                            "attributes": {
                                "key": "key_test",
                                "value": "value_test",
                                "status": "created,modified",
                            },
                            "children": [],
                        }
                    }
                ],
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
                content={"message": f"{response.json()}"},
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


@tenant_router.delete(
    "/{tenant_name}",
    dependencies=[Depends(JWTBearer())],
    description="Use this endpoint to delete tenants in the host")
async def delete_tenant(ip_address: str, tenant_name: str, request: Request):
    try:
        url = f"https://{ip_address}/api/node/mo/uni/tn-{tenant_name}.json"

        response = requests_session.delete(
            url=url,
            verify=False,
            cookies={"APIC-Cookie": request.headers.get("Authorization").split()[1]},
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
