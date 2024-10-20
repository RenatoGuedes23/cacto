from fastapi import FastAPI, APIRouter, status, Request, Response, HTTPException

from config.request.base_session import requests_session
from config.logger.base_logger import logger
from src.authenticate.schemas import ApicLoginSchema
from src.authenticate.models import AutenticateResponseModel, OkResponse, ErrorResponse

# Definir a aplicação FastAPI
app = FastAPI()

# Definir rota de status
@app.get("/status")
async def status():
    return {"status": "ok"}

autenticate_router = APIRouter(
    prefix="/autenticate",
    tags=["autenticate"],
    responses={404: {"description": "Not found"}},
)

@autenticate_router.post(
    "",
    status_code=status.HTTP_200_OK,
    response_model=AutenticateResponseModel,
    description="Use this endpoint to call cisco apic api and retrieve your token",
    responses={
        status.HTTP_200_OK: {
            "model": OkResponse,
            "description": "Ok Response",
        },
        status.HTTP_401_UNAUTHORIZED: {
            "model": ErrorResponse,
            "description": "Creates something from user request ",
        },
        status.HTTP_400_BAD_REQUEST: {
            "model": ErrorResponse,
            "description": "Creates something from user request ",
        },
    },
)
async def autenticate(
    ip_address: str, login: ApicLoginSchema, response: Response, request: Request
) -> AutenticateResponseModel:
    try:
        url = f"https://{ip_address}/api/aaaLogin.json"
        login_dict = {"aaaUser": {"attributes": {"name": login.name, "pwd": login.pwd}}}
        r = requests_session.post(url=url, json=login_dict, verify=False)
        logger.error(f"request to apic was completed with response {r.json()}")

        if r.status_code != 200:
            logger.error("status code is not 200")
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="could not get token from APIC",
            )
        response_dict = r.json()
        logger.info(response_dict)
        token = response_dict["imdata"][0]["aaaLogin"]["attributes"]["token"]

        response.set_cookie(key="APIC-Cookie", value=token, httponly=True)
        request.session["APIC-Cookie"] = token

        return OkResponse(token=token, status_code=200)

    except Exception as e:
        logger.error(f"Error occurred: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Request cannot be completed with the current parameters",
        )

# Incluir o APIRouter na aplicação FastAPI
app.include_router(autenticate_router)
