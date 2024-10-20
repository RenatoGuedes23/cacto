import {
    HiHome, HiBuildingOffice, HiBuildingOffice2, HiCpuChip, HiDocumentText, HiMiniCog8Tooth
  } from "react-icons/hi2";
  import {
    TbPasswordFingerprint, TbDoorEnter
  } from "react-icons/tb";
  import {
    IoShieldCheckmark, IoAddOutline, IoListOutline, IoBusinessOutline, IoGitNetworkOutline
  } from "react-icons/io5";
  import { PiBridgeLight } from "react-icons/pi";
  import { LiaIndustrySolid } from "react-icons/lia";
  import { SiVmware } from "react-icons/si";
  import { BsArrowsCollapseVertical } from "react-icons/bs";
  import { FaFileCsv } from "react-icons/fa6";
  
export const sidebarRoutes = [
  { path: "/dashboard", label: "Home", icon: HiHome },
  {
    path: "/authenticate",
    label: "Authenticate",
    icon: TbPasswordFingerprint,
    badge: "1",
  },
  {
    label: "Tenant",
    icon: HiBuildingOffice2,
    children: [
      {
        label: "Tenant",
        icon: HiBuildingOffice,
        children: [
          { path: "/tenant", label: "Create", icon: IoAddOutline },
          { path: "/get-tenant", label: "Load", icon: IoListOutline },
          { path: "/create-tenant-from-file", label: "File", icon: FaFileCsv },
        ],
      },
      {
        label: "Application",
        icon: HiCpuChip,
        children: [
          { path: "/create-application", label: "Create", icon: IoAddOutline },
          { path: "/get-application", label: "Load", icon: IoListOutline },
        ],
      },
      {
        label: "Epg",
        icon: IoShieldCheckmark,
        children: [
          { path: "/create-epg", label: "Create", icon: IoAddOutline },
          { path: "/get-epg", label: "Load", icon: IoListOutline },
        ],
      },
      {
        label: "Bridge Domain",
        icon: IoBusinessOutline,
        children: [
          {
            path: "/create-bridge-domain",
            label: "Create",
            icon: IoAddOutline,
          },
          { path: "/get-bridge-domain", label: "Load", icon: IoListOutline },
          ,
        ],
      },
      {
        label: "Contract",
        icon: HiDocumentText,
        children: [
          { path: "/create-contract", label: "Create", icon: IoAddOutline },
          {
            path: "/associate-contract",
            label: "Associate Contract",
            icon: BsArrowsCollapseVertical,
          },
        ],
      },
      {
        label: "L3OUT",
        icon: PiBridgeLight,
        children: [
          { path: "/create-l3out", label: "Create", icon: IoAddOutline },
        ],
      },
    ],
  },
  {
    label: "Fabric",
    icon: LiaIndustrySolid,
  },
  {
    label: "Virtual Networking",
    icon: IoGitNetworkOutline,
    children: [
      {
        label: "VmWare",
        icon: SiVmware,
        children: [
          { path: "/create-vmware", label: "Create", icon: IoAddOutline },
          { path: "/get-vmware", label: "Load", icon: IoListOutline },
        ],
      },
      {
        label: "Port Group",
        icon: TbDoorEnter,
        children: [
          { path: "/create-portgroup", label: "Create", icon: IoAddOutline },
          { path: "/get-portgroup", label: "Load", icon: IoListOutline },
        ],
      },
    ],
  },
  { path: "/setting", label: "Setting", icon: HiMiniCog8Tooth },
];
