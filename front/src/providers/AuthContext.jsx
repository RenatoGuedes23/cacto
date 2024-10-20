import React, { createContext, useContext, useState, useEffect } from 'react';
import { useLocalStorage } from './useLocalStorage';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [isAuthenticated, setIsAuthenticated] = useLocalStorage('isAuthenticated', false);
  const [lastLoginTime, setLastLoginTime] = useLocalStorage('lastLoginTime', null);
  const [user, setUser] = useLocalStorage('user', null);

  useEffect(() => {
    const checkTimestamp = () => {
      const currentTime = new Date().getTime();
      const thirtyMinutes = 5 * 60 * 1000;

      if (lastLoginTime && currentTime - lastLoginTime > thirtyMinutes) {
        setIsAuthenticated(false);
        setLastLoginTime(null);
        localStorage.removeItem('isAuthenticated');
        localStorage.removeItem('lastLoginTime');
      }
    };

    checkTimestamp();
  }, [lastLoginTime, setIsAuthenticated, setLastLoginTime]);

  const login = (email, password) => {
    if (email === 'admin' && password === '123') {
      setIsAuthenticated(true);
      setUser(email);
      setLastLoginTime(new Date().getTime());
    } else {
      throw new Error('Invalid credentials');
    }
  };

  const logout = () => {
    setIsAuthenticated(false);
    setLastLoginTime(null);
    localStorage.removeItem('lastLoginTime');
  };

  return (
    <AuthContext.Provider value={{ isAuthenticated, login, logout, user }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  return useContext(AuthContext);
};
