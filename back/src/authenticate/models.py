from pydantic import BaseModel
from typing import Any


class AutenticateResponseModel(BaseModel):
    token: str = ""
    status_code: Any


class OkResponse(AutenticateResponseModel):
    pass


class ErrorResponse(AutenticateResponseModel):
    detail: str
