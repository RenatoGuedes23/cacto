import { lazy } from 'react';
import NotFound from "../pages/notFound";
import Home from "../pages/home";
import Dashboard from "../pages/Dashboard";
import Login from "../pages/Login";
import Authenticate from "../pages/Authenticate/authModal";
import CreateTenant from "../pages/Tenant/Tenant/createTenant";
import LoadTenantFromFile from "../pages/Tenant/Tenant/LoadTenantFromFile";
import LoadTenant from "../pages/Tenant/Tenant/loadTenant";
import CreateApplication from "../pages/Tenant/Application/createApplication";
import LoadApplication from "../pages/Tenant/Application/loadApplication";
import CreateEpg from "../pages/Tenant/Epg/createEpg";
import LoadEpg from "../pages/Tenant/Epg/loadEpg";
import CreateContract from "../pages/Tenant/Contracts/createContract";
import CreateBridgeDomainModal from "../pages/Tenant/BridgeDomain/createBridgeDomainModal";
import LoadBridgeDomain from "../pages/Tenant/BridgeDomain/loadBridgeDomain";
import AssociateContract from "../pages/Tenant/Contracts/associateContract";
import CreateL3out from "../pages/Tenant/L3out/createL3out";
import AdminSetting from "../pages/setting/adminSetting";

import CreatePortGroup from "../pages/VirtualNetworking/PortGroup/createPortGroup";
import LoadPortGroup from "../pages/VirtualNetworking/PortGroup/loadPortGroup";
import CreateVmWare from "../pages/VirtualNetworking/VmWare/createVmWare";
import LoadVmWare from "../pages/VirtualNetworking/VmWare/loadVmWare";

import PrivateRoute from "../pages/PrivateRoutes";

export const pageRoutes = [
  {
    path: "/",
    element: <Home />,
  },
  {
    path: "/login",
    element: <Login />,
  },
  {
    path: "/dashboard",
    element: <PrivateRoute element={<Dashboard />}></PrivateRoute>,
  },
  {
    path: "/authenticate",
    element: <PrivateRoute element={<Authenticate />}></PrivateRoute>,
  },
  {
    path: "/create-tenant-from-file",
    element: <PrivateRoute element={<LoadTenantFromFile />}></PrivateRoute>,
  },
  {
    path: "/tenant",
    element: <PrivateRoute element={<CreateTenant />}></PrivateRoute>,
  },
  {
    path: "/get-tenant",
    element: <PrivateRoute element={<LoadTenant />}></PrivateRoute>,
  },
  {
    path: "/create-application",
    element: <PrivateRoute element={<CreateApplication />}></PrivateRoute>,
  },
  {
    path: "/get-application",
    element: <PrivateRoute element={<LoadApplication />}></PrivateRoute>,
  },
  {
    path: "/create-epg",
    element: <PrivateRoute element={<CreateEpg />}></PrivateRoute>,
  },
  {
    path: "/get-epg",
    element: <PrivateRoute element={<LoadEpg />}></PrivateRoute>,
  },
  {
    path: "/create-bridge-domain",
    element: <PrivateRoute element={<CreateBridgeDomainModal />}></PrivateRoute>,
  },
  {
    path: "/get-bridge-domain",
    element: <PrivateRoute element={<LoadBridgeDomain />}></PrivateRoute>,
  },
  {
    path: "/create-contract",
    element: <PrivateRoute element={<CreateContract />}></PrivateRoute>,
  },
  {
    path: "/associate-contract",
    element: <PrivateRoute element={<AssociateContract />}></PrivateRoute>,
  },
  {
    path: "/create-l3out",
    element: <PrivateRoute element={<CreateL3out />}></PrivateRoute>,
  },
  {
    path: "/create-l3out",
    element: <PrivateRoute element={<CreateL3out />}></PrivateRoute>,
  },
  {
    path: "/setting",
    element: <PrivateRoute element={<AdminSetting />}></PrivateRoute>,
  },
  {
    path: "/create-vmware",
    element: <PrivateRoute element={<CreateVmWare />}></PrivateRoute>,
  },
  {
    path: "/get-vmware",
    element: <PrivateRoute element={<LoadVmWare />}></PrivateRoute>,
  },
  {
    path: "/create-portgroup",
    element: <PrivateRoute element={<CreatePortGroup />}></PrivateRoute>,
  },
  {
    path: "/get-portgroup",
    element: <PrivateRoute element={<LoadPortGroup />}></PrivateRoute>,
  },
  {
    path: "/*",
    element: <NotFound />,
  },
];
