// src/App.jsx
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import SideBarLinks from "./components/sidebar";
import IpProvider from "./providers/ip";
import PrivateRoute from "./pages/PrivateRoutes";
import { AuthProvider, useAuth } from "./providers/AuthContext";
import { useLocation } from "react-router-dom";
import { pageRoutes } from "./routes/pageRoutes";
import { NewSidebar } from "./components/newSidebar";

function App() {
  return (
    <Router>
      <AuthProvider>
        <IpProvider>
          <div className="h-screen flex">
            <AuthenticatedApp />
          </div>
        </IpProvider>
      </AuthProvider>
    </Router>
  );
}

const AuthenticatedApp = () => {
  const { isAuthenticated } = useAuth();
  const location = useLocation();

  return (
    <>
      {isAuthenticated && location.pathname !== "/" && <SideBarLinks className="w-1/4 h-full" />}
      {/* {isAuthenticated && location.pathname !== "/" && <NewSidebar />} */}
      <div className="w-full p-4">
        <div className="h-full p-6">
          <Routes>
            {pageRoutes.map((route) => {
              return (
                <Route
                  key={route.path}
                  path={route.path}
                  element={route.element}
                />
              );
            })}
          </Routes>
        </div>
      </div>
    </>
  );
};

export default App;
