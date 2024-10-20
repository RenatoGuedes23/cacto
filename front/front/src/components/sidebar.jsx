import { Link, useNavigate } from "react-router-dom";
import { Sidebar } from "flowbite-react";
import { sidebarRoutes } from "./sidebarRoutes";

import { useAuth } from "../providers/AuthContext";

import { TbDoorEnter } from "react-icons/tb";

const SidebarItem = ({ path, label, icon: Icon, badge }) => (
  <Sidebar.Item as={Link} to={path} icon={Icon} label={badge}>
    {label}
  </Sidebar.Item>
);

const SidebarCollapse = ({ label, icon: Icon, children }) => (
  <Sidebar.Collapse icon={Icon} label={label}>
    {children &&
      children.map((item, index) => (
        <div key={index}>
          {item.children ? (
            <SidebarCollapse {...item} />
          ) : (
            <SidebarItem {...item} />
          )}
        </div>
      ))}
  </Sidebar.Collapse>
);

const SideBarLinks = () => {
  const { logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate("/");
  };
  return (
    <div className="h-screen">
      <Sidebar aria-label="Default sidebar example" className="h-full w-full">
        <Sidebar.Items>
          <Sidebar.ItemGroup>
            {sidebarRoutes.map((route, index) => (
              <div key={index}>
                {route.children ? (
                  <SidebarCollapse {...route} />
                ) : (
                  <SidebarItem {...route} />
                )}
              </div>
            ))}
            <Sidebar.Item
              className="w-full text-left"
              as="button"
              onClick={handleLogout}
              icon={TbDoorEnter}
            >
              Logout
            </Sidebar.Item>
          </Sidebar.ItemGroup>
        </Sidebar.Items>
      </Sidebar>
    </div>
  );
};

export default SideBarLinks;
