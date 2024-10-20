import { useContext, useState } from "react";
import { FloatingLabel, Button, Alert } from "flowbite-react";
import axiosInstance from "../../../api/localApi";
import Cookies from "js-cookie";
import { IpContext } from "../../../providers/ip";

import { ApiUrl } from "../../../utils/useApi";

function CreateApplication() {
  const { ip } = useContext(IpContext);
  const [inputValues, setInputValues] = useState({
    ip: ip || "",
    tenant_name: "",
    application_name: "",
    alias: ""
  });

  const [isSuccess, setIsSuccess] = useState(false);
  const [isError, setIsError] = useState(false);

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
      const apiLocal = `${ApiUrl}/tenant/application?ip_address=${inputValues.ip}`;

      const response = await axiosInstance.post(apiLocal, {
        tenant_name: inputValues.tenant_name,
        application_name: inputValues.application_name,
        alias: inputValues.alias,
      }, {
        headers: { Authorization: `Bearer ${localStorage.getItem("APIC-cookie")}` }
      });

      if (response.data) {
        console.log(response.data)
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
            label="Tenent Name"
            value={inputValues.tenant_name}
            onChange={(event) => handleInputChange(event, "tenant_name")}
          />
          <FloatingLabel
            variant="filled"
            label="Application Name"
            value={inputValues.application_name}
            onChange={(event) => handleInputChange(event, "application_name")}
          />
          <FloatingLabel
            variant="filled"
            label="Alias"
            value={inputValues.alias}
            onChange={(event) => handleInputChange(event, "alias")}
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
              <span className="font-medium">Request Sent</span> Application was
              created successfully
            </Alert>
          )}
          {isError && (
            <Alert
              color="info"
              className="mt-4"
              onDismiss={() => setIsSuccess(false)}
            >
              <span className="font-medium">Error</span> Could not create application
            </Alert>
          )}
        </div>
      </div>
    </div>
  );
}

export default CreateApplication;
