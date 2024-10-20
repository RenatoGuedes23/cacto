import { createContext, useState } from 'react';
import useStorage from '../utils/useStorage'

// Criação de Contexto
export const IpContext = createContext({
  ip: null,
  setIp: () => {},
});

// criação do provider
const IpProvider = ({ children }) => {
    const [ip, setIp] = useStorage('ip');
  
    return (
      <IpContext.Provider value={{ip, setIp}}>
        {children}
      </IpContext.Provider>
    )
  }
  
  
export default IpProvider;