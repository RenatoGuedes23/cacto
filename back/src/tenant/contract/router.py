from fastapi import APIRouter, Depends, status, Request, Response, HTTPException
from fastapi.responses import JSONResponse

from config.security.security import JWTBearer
from src.tenant.contract.schemas import AssociateContract, ConsumedContractEpgImput, DeleteConsumedContractEpgImput

from config.request.base_session import requests_session
from config.logger.base_logger import logger

contract_router = APIRouter(
    prefix="/contract",
    tags=["contract"],
    responses={404: {"description": "Not found"}},
)


@contract_router.post(
    "",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(JWTBearer())])
async def create_contract(
    ip_address: str,
    contract: ConsumedContractEpgImput,
    request: Request
):
    try:
        url = f"https://{ip_address}/api/node/mo/uni/tn-{contract.tenant_name}/brc-{contract.contract_name}.json"

        request_body = {
            "vzBrCP": {
                "attributes": {
                    "dn": f"uni/tn-{contract.tenant_name}/brc-{contract.contract_name}",
                    "name": f"{contract.contract_name}",
                    "scope": "tenant",
                    "rn": f"brc-{contract.contract_name}",
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


@contract_router.post(
    "/associate-contract-as-provided",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(JWTBearer())]
    )
async def associate_contract_as_provided(
    ip_address: str,
    contract: AssociateContract,
    request: Request,
):
    try:
        url = f"https://{ip_address}/api/node/mo/uni/"\
            f"tn-{contract.tenant_name}/"\
            f"out-{contract.l3out_name}/instP-{contract.ext_epg_name}.json"

        request_body = {
            "fvRsProv": {
                "attributes": {
                    "tnVzBrCPName": f"{contract.contract_name}",
                    "status": "created,modified",
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


@contract_router.post(
    "/associate-consumed-contract-to-epg",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(JWTBearer())]
)
async def associate_consumed_contract_to_epg(
    ip_address: str,
    contract: ConsumedContractEpgImput,
    request: Request,
):
    try:
        url = f"https://{ip_address}/api/node/mo/uni/tn-{contract.tenant_name}/ap-{contract.application_name}/epg-{contract.epg_name}.json"

        request_body = {
            "fvRsIntraEpg": {
                "attributes": {
                    "tnVzBrCPName": f"{contract.contract_name}",
                    "status": "created,modified",
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


@contract_router.delete(
    "/associate-consumed-contract-to-epg/{tenant_name}/{application_name}/{epg_name}/{contract_name}",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(JWTBearer())]
)
async def associate_consumed_contract_to_epg(
    ip_address: str,
    tenant_name: str,
    application_name: str,
    epg_name: str,
    contract_name: str,
    request: Request,
):

    try:
        url = f"https://{ip_address}/api/node/mo/uni/tn-{tenant_name}/ap-{application_name}/epg-{epg_name}/rsintraEpg-{contract_name}.json"

        request_body = {
            "fvRsIntraEpg": {
                "attributes": {
                    "dn": f"uni/tn-{tenant_name}/ap-{application_name}/epg-{epg_name}/rsintraEpg-{contract_name}",
                    "status": status,
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
