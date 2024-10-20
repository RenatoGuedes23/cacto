import time
import logging

from fastapi import Request
from config.logger.base_logger import logger


async def log_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    log_dict = {
        "requested_url": request.url.path,
        "requested_method": request.method,
        "time": process_time,
        "service": str(request.url),
        "status_code": response.status_code,
    }

    logger.info(log_dict)
    return response
