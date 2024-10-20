import json
from typing import Annotated
from fastapi import APIRouter, Depends, Header, status, Request, HTTPException
from fastapi.responses import JSONResponse

from config.request.base_session import requests_session
from config.logger.base_logger import logger
from config.security.security import JWTBearer
from src.tenant.application.schemas import (
    ApplicationSchemaImput,
    ApplicationSchemaOutput,
)

application_router = APIRouter(
    prefix="/application",
    tags=["application"],
    responses={404: {"description": "Not found"}},
)

Headers = Annotated[list[str] | None, Header()]


@application_router.get(
    "/{tenant_name}",
    response_model=ApplicationSchemaOutput,
    dependencies=[Depends(JWTBearer())],
)
async def get_application(
    ip_address: str,
    tenant_name: str,
    request: Request,
):
    try:
        url = f"https://{ip_address}/api/node/mo/uni/tn-{tenant_name}.json?query-target=children&target-subtree-class=fvAp"

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


@application_router.post(
    "", status_code=status.HTTP_200_OK, dependencies=[Depends(JWTBearer())]
)
async def create_application(
    application: ApplicationSchemaImput, ip_address: str, request: Request
):
    try:

        url = (
            f"https://{ip_address}/api/node/mo/uni/tn-{application.tenant_name}"
            f"/ap-{application.application_name}.json"
        )

        request_body = {
            "fvAp": {
                "attributes": {
                    "dn": f"uni/tn-{application.tenant_name}/ap-{application.application_name}",
                    "name": f"{application.application_name}",
                    "nameAlias": f"{application.alias}",
                    "rn": f"ap-{application.application_name}",
                    "status": "created",
                },
                "children": [
                    {
                        "fvRsApMonPol": {
                            "attributes": {
                                "tnMonEPGPolName": "default",
                                "status": "created,modified",
                            }
                        }
                    }
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


@application_router.delete(
    "/{tenent_name}/{apication_name}", dependencies=[Depends(JWTBearer())]
)
async def get_application(
    ip_address: str, tenent_name: str, apication_name: str, request: Request
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
