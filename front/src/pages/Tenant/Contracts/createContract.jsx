import { useContext, useState } from "react";
import { FloatingLabel, Button, Alert } from "flowbite-react";
import axiosInstance from "../../../api/localApi";
import { IpContext } from "../../../providers/ip";

import { ApiUrl } from "../../../utils/useApi";

function CreateContract() {
  const { ip } = useContext(IpContext);
  const [inputValues, setInputValues] = useState({
    ip: ip || "",
    tenant_name: "",
    application_name: "",
    epg_name: "",
    contract_name: "",
  });

  const [successMessage, setSuccessMessage] = useState("");
  const [errorMessage, setErrorMessage] = useState("");

  const handleInputChange = (event, variant) => {
    setInputValues({
      ...inputValues,
      [variant]: event.target.value,
    });
  };

  const handleSubmit = async () => {
    console.log(inputValues);
    setSuccessMessage("");
    setErrorMessage("");

    try {
      const apiLocal = `${ApiUrl}/tenant/contract?ip_address=${inputValues.ip}`;

      const response = await axiosInstance.post(apiLocal, {
        tenant_name: inputValues.tenant_name,
        application_name: inputValues.application_name,
        epg_name: inputValues.epg_name,
        contract_name: inputValues.contract_name,
      }, {
        headers: { Authorization: `Bearer ${localStorage.getItem("APIC-cookie")}` }
      });

      if (response.data) {
        setSuccessMessage("Contract was created successfully");
      }
    } catch (error) {
      console.error(error);
      setErrorMessage("Contract creation error");
    }
  };

  return (
    <div className="flex flex-col">
      <div>
        <FloatingLabel
          variant="filled"
          label="IP"
          value={inputValues.ip}
          name="ip"
          onChange={(event) => handleInputChange(event, "ip")}
        />
        <FloatingLabel
          variant="filled"
          label="Tenant Name"
          value={inputValues.tenant_name}
          name="tenant"
          onChange={(event) => handleInputChange(event, "tenant_name")}
        />
        <FloatingLabel
          variant="filled"
          label="Application Name"
          value={inputValues.application_name}
          name="application_name"
          onChange={(event) => handleInputChange(event, "application_name")}
        />
        <FloatingLabel
          variant="filled"
          label="EPG Name"
          value={inputValues.epg_name}
          name="epg_name"
          onChange={(event) => handleInputChange(event, "epg_name")}
        />
        <FloatingLabel
          variant="filled"
          label="Contract Name"
          value={inputValues.contract_name}
          name="contract"
          onChange={(event) => handleInputChange(event, "contract_name")}
        />
        <Button color="success" onClick={handleSubmit}>
          Enviar
        </Button>
        {successMessage && (
          <Alert color="success" className="mt-4" onDismiss={() => setSuccessMessage("")}>
            <span className="font-medium">Request Sent</span> {successMessage}
          </Alert>
        )}
        {errorMessage && (
          <Alert color="failure" className="mt-4" onDismiss={() => setErrorMessage("")}>
            <span className="font-medium">Error</span> {errorMessage}
          </Alert>
        )}
      </div>
    </div>
  );
}

export default CreateContract;
