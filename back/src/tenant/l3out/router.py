from fastapi import APIRouter, Depends, status, Request, Response, HTTPException
from fastapi.responses import JSONResponse

from config.request.base_session import requests_session
from config.logger.base_logger import logger
from config.security.security import JWTBearer
from src.tenant.l3out.schemas import L3outSchemaImput, L3outSchemaOutput

l3out_router = APIRouter(
    prefix="/l3out",
    tags=["l3out"],
    responses={404: {"description": "Not found"}},
)



@l3out_router.get(
    "/{tenant_name}",
    response_model=L3outSchemaOutput,
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(JWTBearer())],
)
async def get_epg(
    ip_address: str,
    tenant_name: str,
    request: Request):
    try:

        url = f"https://{ip_address}/api/node/mo/uni/tn-{tenant_name}.json?"\
            "query-target=children&target-subtree-class=l3extOut&query-target-filter=and"\
            "(and(not(wcard(l3extOut.dn,%22__ui_%22)),not(wcard(l3extOut.annotation,%22shadow:yes%22))"\
            ",not(wcard(l3extOut.annotation,%22hidden:true%22))),eq(l3extOut.mplsEnabled,%22no%22))"\
            "&rsp-subtree-class=bgpExtP,ospfExtP,eigrpExtP,pimExtP,l3extRsEctx&order-by=l3extOut.name|asc"
        
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



@l3out_router.post(
    "",
    dependencies=[Depends(JWTBearer())],
    description="Use this endpoint to create a l3out",
)
async def create_l3out(
    l3out: L3outSchemaImput,
    ip_address: str,
    request: Request,
):
    try:
        url = f"https://{ip_address}/api/node/mo/uni/tn-{l3out.tenant_name}/out-{l3out.l3out_name}.json"

        request_body = {
            "l3extOut": {
                "attributes": {
                    "dn": f"uni/tn-{l3out.tenant_name}/out-{l3out.l3out_name}",
                    "name": f"{l3out.l3out_name}",
                    "rn": f"out-{l3out.l3out_name}",
                    "status": "created",
                },
                "children": [
                    {
                        "l3extRsEctx": {
                            "attributes": {"tnFvCtxName": f"{l3out.vrf}"},
                            "children": [],
                        }
                    },
                    {
                        "l3extRsL3DomAtt": {
                            "attributes": {
                                "tDn": f"uni/l3dom-{l3out.ext_dom}",
                                "status": "created",
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



@l3out_router.delete(
    "/{tenant_name}/{l3out_name}",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(JWTBearer())],
)
async def delete_l3out(
    ip_address: str,
    tenant_name: str,
    l3out_name: str,
    request: Request):
    try:
        url = f"https://{ip_address}/api/node/mo/uni/tn-{tenant_name}/out-{l3out_name}.json"
        
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

