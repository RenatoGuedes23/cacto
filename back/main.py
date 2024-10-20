#!/usr/bin/python
# -*- encoding: utf-8 -*-
import uvicorn

from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from fastapi import FastAPI
from starlette.config import Config
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.sessions import SessionMiddleware
from config.middleware import log_middleware

from src.authenticate.router import autenticate_router
from config.database.base_db import PostgreConnectionHandler


# TENANT
from src.tenant.application.router import application_router
from src.tenant.tenant.router import tenant_router
from src.tenant.epg.router import epg_router
from src.tenant.bridge_domain.router import bridge_domain_router
from src.tenant.contract.router import contract_router
from src.tenant.vrf.router import vrf_router
from src.tenant.l3out.router import l3out_router

# FABRIC
from src.fabric.physical_interface.router import physical_interface_router
from src.fabric.pools.vlan.router import vlan_router

# VIRTUAL_NETWORKING
from src.virtual_networking.portgroup.router import portgroup_router
from src.virtual_networking.vmware.router import vmware_router

# CONFIGURATION
from config.logger.base_logger import logger

# DBConnection = PostgreConnectionHandler()


config = Config(".env")  # parse .env file for env variables

ENVIRONMENT = config("ENVIRONMENT")  # get current env name
SHOW_DOCS_ENVIRONMENT = ("local", "staging", "dev")  # explicit list of allowed envs

app_configs = {"title": "NTT Cisco API"}
if ENVIRONMENT not in SHOW_DOCS_ENVIRONMENT:
    app_configs["openapi_url"] = None

app = FastAPI(**app_configs)

FastAPIInstrumentor.instrument_app(app)

app.add_middleware(middleware_class=BaseHTTPMiddleware, dispatch=log_middleware)
app.add_middleware(SessionMiddleware, secret_key="APIC-Cookie", max_age=None)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# include routers:
app.include_router(autenticate_router)

app.include_router(tenant_router, prefix='/tenant')
app.include_router(application_router, prefix='/tenant')
app.include_router(epg_router, prefix='/tenant')
app.include_router(bridge_domain_router, prefix='/tenant')
app.include_router(contract_router, prefix='/tenant')
app.include_router(vrf_router, prefix='/tenant')
app.include_router(l3out_router, prefix='/tenant')

app.include_router(physical_interface_router, prefix='/fabric')
app.include_router(vlan_router, prefix='/fabric')

app.include_router(portgroup_router, prefix='/virtual_net')
app.include_router(vmware_router, prefix='/virtual_net')



if __name__ == "__main__":
    
    # # migrations of models
    # if "makemigrations" in sys.argv:
    #     DBConnection.check_db_structure()
    #     sys.exit()
        
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )