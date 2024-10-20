import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import MenuIcon from "@mui/icons-material/Menu";
import AddAPhotoIcon from '@mui/icons-material/AddAPhoto';
import ExitToAppIcon from "@mui/icons-material/ExitToApp";
import AssignmentIndIcon from '@mui/icons-material/AssignmentInd';
import { sidebarRoutes } from "./sidebarRoutes";
import { useAuth } from "../providers/AuthContext";
import ExpandLessIcon from '@mui/icons-material/ExpandLess';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';

export const NewSidebar = () => {
  const [isCollapsed, setIsCollapsed] = useState(false);
  const [openSubmenus, setOpenSubmenus] = useState({});
  const { logout, user } = useAuth();
  const navigate = useNavigate();

  const toggleSidebar = () => {
    setIsCollapsed(!isCollapsed);
  };

  const toggleSubmenu = (label) => {
    setOpenSubmenus((prev) => ({
      ...prev,
      [label]: !prev[label],
    }));
  };


  const handleLogout = () => {
    logout();
    navigate("/");
  };

  return (
    <div
      className={`${
        isCollapsed ? "w-20" : "w-64"
      } bg-gray-800 text-white min-h-screen h-full duration-300 flex flex-col relative`}
    >
      <div className="flex items-center justify-between p-4">
      {!isCollapsed && <span className="ml-2 text-xl font-bold">NTT</span>}
        <div className="flex items-center">
          <button onClick={toggleSidebar}>
            <MenuIcon className="text-white" />
          </button>
          
        </div>
      </div>

      <div className="p-4 flex items-center">
        <AssignmentIndIcon />
        {/* <img
          src={logo}
          alt="img"
          className={`${
            isCollapsed ? "w-8" : "w-12"
          } rounded-full duration-300`}
        ></img> */}
        {!isCollapsed && (
          <div className="ml-3">
            <p className="font-bold">{user}</p>
            <p>role</p>
          </div>
        )}
      </div>

      <ul className="mt-4 flex-grow overflow-y-auto pb-16">
        {sidebarRoutes.map((item) => {
          const IconComponent = item.icon;
          return (
            <li key={item.label}>
              <Link
                to={item.path || "#"}
                className="flex items-center justify-between px-4 py-2 hover:bg-gray-700 cursor-pointer"
                onClick={() => item.children && toggleSubmenu(item.label)}
              >
              <div
                className="flex items-center space-x-3"
              >
                  {IconComponent && <IconComponent className="w-6 h-6" />}
                  {!isCollapsed && <span>{item.label}</span>}
                {item.children && !isCollapsed && (
                  <span>{openSubmenus[item.label] ? <ExpandLessIcon /> : <ExpandMoreIcon />}</span>
                )}
              </div>
              
              </Link>

              {item.children && openSubmenus[item.label] && !isCollapsed && (
                <ul className="ml-4">
                  {item.children.map((subItem) => {
                    const SubIcon = subItem.icon;
                    return (
                      <li key={subItem.label}>
                        <Link
                          to={subItem.path}
                          className="flex items-center space-x-3 p-2 hover:bg-gray-600"
                        >
                          {SubIcon && <SubIcon className="w-5 h-5" />}
                          {!isCollapsed && <span>{subItem.label}</span>}
                        </Link>
                        {subItem.children && (
                          <ul className="ml-4">
                            {subItem.children.map((childItem) => {
                              const ChildIcon = childItem.icon;
                              return (
                                <li key={childItem.label}>
                                  <Link
                                    to={childItem.path}
                                    className="flex items-center space-x-3 p-2 hover:bg-gray-500"
                                  >
                                    {ChildIcon && (
                                      <ChildIcon className="w-4 h-4" />
                                    )}
                                    {!isCollapsed && (
                                      <span>{childItem.label}</span>
                                    )}
                                  </Link>
                                </li>
                              );
                            })}
                          </ul>
                        )}
                      </li>
                    );
                  })}
                </ul>
              )}
            </li>
          );
        })}
      </ul>

      <div className="absolute bottom-0 left-0 w-full">
        <button onClick={handleLogout} className="w-full flex items-center justify-center space-x-3 p-4 bg-red-600 hover:bg-red-700 text-white">
          <ExitToAppIcon />
          {!isCollapsed && <span>Logout</span>}
        </button>
      </div>
    </div>
  );
};
