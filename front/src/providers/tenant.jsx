import React, {createContext, useState} from "react";
import { renderToStaticMarkup } from "react-dom/server";

export const TenantContext = createContext();

export const TenantProvider = ({children}) => {
    const [tenant, setTanant] = useState()
    const [tenantList, setTanantList] = useState([])

    return (
        <TenantContext.Provider value={{tenant, setTanant, tenantList, setTanantList}}>
            {children}
        </TenantContext.Provider>
    )
}