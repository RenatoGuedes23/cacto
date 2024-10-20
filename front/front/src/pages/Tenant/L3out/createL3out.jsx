import { useContext, useState } from "react";
import { FloatingLabel, Button, Alert } from "flowbite-react";
import axiosInstance from "../../../api/localApi";
import { IpContext } from "../../../providers/ip";

import { ApiUrl } from "../../../utils/useApi";

function CreateL3out() {
  const { ip } = useContext(IpContext);
  const [inputValues, setInputValues] = useState({
    ip: ip || "",
    tenant_name: "",
    l3out_name: "",
    vrf: "",
    ext_dom: "",
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
      const apiLocal = `${ApiUrl}/tenant/l3out?ip_address=${inputValues.ip}`;
      const response = await axiosInstance.post(apiLocal, {
        tenant_name: inputValues.tenant_name,
        vrf: inputValues.vrf,
        l3out_name: inputValues.l3out_name,
        ext_dom: inputValues.ext_dom,
      }, {
        headers: { Authorization: `Bearer ${localStorage.getItem("APIC-cookie")}` }
      });

      if (response.data) {
        console.log(response.data);
        setSuccessMessage(`L3out was created successfully with name=${inputValues.l3out_name}`);
      }
    } catch (error) {
      console.error(error);
      setErrorMessage("L3out was not created");
    }
  };

  return (
    <div className="flex flex-col">
      <div>
        <FloatingLabel
          variant="filled"
          label="IP"
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
          label="L3OUT Name"
          value={inputValues.l3out_name}
          onChange={(event) => handleInputChange(event, "l3out_name")}
        />
        <FloatingLabel
          variant="filled"
          label="VRF"
          value={inputValues.vrf}
          onChange={(event) => handleInputChange(event, "vrf")}
        />
        <FloatingLabel
          variant="filled"
          label="EXT_DOM"
          value={inputValues.ext_dom}
          onChange={(event) => handleInputChange(event, "ext_dom")}
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

export default CreateL3out;
