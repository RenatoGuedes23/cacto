from fastapi import APIRouter, Depends, status, Request, Response, HTTPException
from fastapi.responses import JSONResponse

from config.request.base_session import requests_session
from config.logger.base_logger import logger

from config.security.security import JWTBearer
from src.fabric.physical_interface.schemas import (
    EnablePhysicalInterfaceSchema,
    DisablePhysicalInterfaceSchema)

physical_interface_router = APIRouter(
    prefix="/physical_interface",
    tags=["physical_interface"],
    responses={404: {"description": "Not found"}},
)


@physical_interface_router.post(
    "/enable",
    dependencies=[Depends(JWTBearer())],
    description="Use this endpoint to enable a eth",
)
async def enable_eth_port(
    ip_address: str,
    physical_interface: EnablePhysicalInterfaceSchema,
    request: Request,
):
    try:
        url = f"https://{ip_address}/api/node/mo/uni/fabric/outofsvc.json"

        request_body = {
            "fabricRsOosPath": {
                "attributes": {
                    "dn": f"uni/fabric/outofsvc/rsoosPath-[topology/pod-{physical_interface.pod_name}/"\
                        f"paths-{physical_interface.leaf_name}/pathep-[{physical_interface.eth_port_name}]]",
                    "status": "deleted",
                },
                "children": [],
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


@physical_interface_router.post(
    "/disable",
    dependencies=[Depends(JWTBearer())],
    description="Use this endpoint to disable a eth",
)
async def disable_eth_port(
    ip_address: str,
    physical_interface: DisablePhysicalInterfaceSchema,
    request: Request,
):
    try:
        url = f"https://{ip_address}/api/node/mo/uni/fabric/outofsvc.json"

        request_body = {
            "fabricRsOosPath": {
                "attributes": {
                    "tDn": f"topology/pod-{physical_interface.pod_name}/"\
                        f"paths-{physical_interface.leaf_name}/pathep-[{physical_interface.eth_port_name}]",
                    "lc": "blacklist",
                },
                "children": [],
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


@physical_interface_router.get(
    "/{pod_name}/{leaf_name}",
    dependencies=[Depends(JWTBearer())],
    description="Use this endpoint to list all physical interfaces",
)
async def list_tenent(
    ip_address: str,
    pod_name: str,
    leaf_name: str,
    request: Request,
):
    url = f"https://{ip_address}/api/node/class/topology/pod-{pod_name}/"\
        f"node-{leaf_name}/l1PhysIf.json"

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
