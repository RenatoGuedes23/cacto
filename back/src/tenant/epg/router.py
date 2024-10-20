import json
from fastapi import APIRouter, Depends, status, Request, Response, HTTPException
from fastapi.responses import JSONResponse

from config.security.security import JWTBearer
from src.tenant.epg.schemas import EpgSchemaImput, EpgSchemaOutput

from config.request.base_session import requests_session
from config.logger.base_logger import logger


epg_router = APIRouter(
    prefix="/epg",
    tags=["epg"],
    responses={404: {"description": "Not found"}},
)


@epg_router.get(
    "/{tenant_name}/{app_name}",
    response_model=EpgSchemaOutput,
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(JWTBearer())],
)
async def get_epg(
    ip_address: str,
    tenant_name: str,
    app_name: str,
    request: Request):
    try:
        url = f"https://{ip_address}/api/node/mo/uni/tn-{tenant_name}/ap-{app_name}.json?query-target=subtree&target-subtree-class=fvAEPg"

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


@epg_router.post(
    "",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(JWTBearer())])
async def create_epg(
    epg: EpgSchemaImput,
    ip_address: str,
    request: Request,
):
    try:
        url = f"https://{ip_address}/api/node/mo/uni/tn-{epg.tenant_name}/ap-{epg.application_name}/epg-{epg.epg_name}.json"

        request_body = {
            "fvAEPg": {
                "attributes": {
                    "dn": f"uni/tn-{epg.tenant_name}/ap-{epg.application_name}/epg-{epg.epg_name}",
                    "name": f"{epg.epg_name}",
                    "nameAlias": f"{epg.alias}",
                    "rn": f"epg-{epg.epg_name}",
                    "status": "created",
                },
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


@epg_router.delete(
    "/{tenent_name}/{apication_name}",
    dependencies=[Depends(JWTBearer())])
async def get_application(
    ip_address: str,
    tenent_name: str,
    apication_name: str,
    request: Request
):
    try:
        url = f"https://{ip_address}/api/node/mo/uni/tn-{tenent_name}/ap-{apication_name}.json"

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
