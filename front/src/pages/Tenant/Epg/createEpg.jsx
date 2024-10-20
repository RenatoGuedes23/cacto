import { useContext, useState } from "react";
import { FloatingLabel, Button, Alert } from "flowbite-react";
import axiosInstance from "../../../api/localApi";
import Cookies from "js-cookie";
import { IpContext } from "../../../providers/ip";

import { ApiUrl } from "../../../utils/useApi";

function CreateEpg() {
  const { ip } = useContext(IpContext);
  const [inputValues, setInputValues] = useState({
    ip: ip || "",
    tenant_name: "",
    application_name: "",
    epgName: "",
    alias: "",
    bdName: "",
  });

  const [isSuccess, setIsSuccess] = useState(false);
  const [isError, setIsError] = useState(false);
  const [token, setToken] = useState("");

  const handleInputChange = (event, variant) => {
    setInputValues({
      ...inputValues,
      [variant]: event.target.value,
    });
  };

  const handleSubmit = async () => {
    console.log(inputValues);
    setIsSuccess(false);
    setIsError(false);
    try {
      const apiLocal = `${ApiUrl}/tenant/epg?ip_address=${inputValues.ip}`;

      const response = await axiosInstance.post(apiLocal, {
        tenant_name: inputValues.tenant_name,
        application_name: inputValues.application_name,
        epg_name: inputValues.epgName,
        alias: inputValues.alias,
        bd_name: inputValues.bdName,
      }, {
        headers: { Authorization: `Bearer ${localStorage.getItem("APIC-cookie")}` }
      });

      if (response.data) {
        setIsSuccess(true);
      }
    } catch (error) {
      console.error(error);
      setIsError(true);
    }
  };

  return (
    <div className="flex flex-col">
      <div className="">
        <div>
          <FloatingLabel
            variant="filled"
            label="ip"
            value={inputValues.ip}
            onChange={(event) => handleInputChange(event, "ip")}
          />
          <FloatingLabel
            variant="filled"
            label="Tenant Name"
            value={inputValues.tenant_name}
            onChange={(event) => handleInputChange(event, "tenant_name")}
          />
          <FloatingLabel
            variant="filled"
            label="Aplication Name"
            value={inputValues.application_name}
            onChange={(event) => handleInputChange(event, "application_name")}
          />
          <FloatingLabel
            variant="filled"
            label="Epg Name"
            value={inputValues.epgName}
            onChange={(event) => handleInputChange(event, "epgName")}
          />
          <FloatingLabel
            variant="filled"
            label="Alias"
            value={inputValues.alias}
            onChange={(event) => handleInputChange(event, "alias")}
          />
          <FloatingLabel
            variant="filled"
            label="Database Name"
            value={inputValues.bdName}
            onChange={(event) => handleInputChange(event, "bdName")}
          />
          <Button color="success" onClick={handleSubmit}>
            Enviar
          </Button>
          {isSuccess && (
            <Alert
              color="success"
              className="mt-4"
              onDismiss={() => setIsSuccess(false)}
            >
              <span className="font-medium">Request Sent</span> EPG was
              created successfully
            </Alert>
          )}
          {isError && (
            <Alert
              color="info"
              className="mt-4"
              onDismiss={() => setIsSuccess(false)}
            >
              <span className="font-medium">Error</span> Contract Error
            </Alert>
          )}
        </div>
      </div>
    </div>
  );
}

export default CreateEpg;
