import { useState, useContext } from "react";
import { FloatingLabel, Button, Alert } from "flowbite-react";
import axiosInstance from "../../../api/localApi";
import Cookies from "js-cookie";
import { IpContext } from "../../../providers/ip";
import { ApiUrl } from "../../../utils/useApi";

const CreateTenant = () => {
  const { ip } = useContext(IpContext);
  const [inputValues, setInputValues] = useState({
    ip: ip || "",
    tenant_name: "",
    descr: "",
    dn: "",
    nameAlias: "",
    rn: ""
  });

  const [isSuccess, setIsSuccess] = useState(false);
  const [isError, setIsError] = useState(false);
  const [isErrorMessage, setErrorMessage] = useState("");

  const handleInputChange = (event, variant) => {
    setInputValues({
      ...inputValues,
      [variant]: event.target.value,
    });
  };

  const handleSubmit = async () => {
    setIsSuccess(false);
    setIsError(false);

    console.log(inputValues.name);
    try {
      const apiLocal = `${ApiUrl}/tenant/tenant?ip_address=${inputValues.ip}`;

      const response = await axiosInstance.post(
        apiLocal,
        {
          name: inputValues.tenant_name,
          descr: inputValues.descr,
          dn: inputValues.dn,
          nameAlias: inputValues.nameAlias,
          rn: inputValues.rn,
        },
        {
          headers: {
            Authorization: `Bearer ${localStorage.getItem("APIC-cookie")}`,
          },
        }
      );

      if (response.data) {
        console.log(response.data);
        setIsSuccess(true);
      }
    } catch (error) {
      console.error(error);
      console.log(error.request);
      setIsError(true);
    }
  };

  return (
    <div className="grid grid-flow-col justify-stretch space-x-4">
      <div>
        <FloatingLabel
          variant="filled"
          label="IP"
          value={inputValues.ip}
          onChange={(event) => handleInputChange(event, "ip")}
        />
        <FloatingLabel
          variant="filled"
          label="name"
          value={inputValues.tenant_name}
          onChange={(event) => handleInputChange(event, "tenant_name")}
        />
        <FloatingLabel
          variant="filled"
          label="Description"
          value={inputValues.descr}
          onChange={(event) => handleInputChange(event, "descr")}
        />
        <FloatingLabel
          variant="filled"
          label="Alias"
          value={inputValues.nameAlias}
          onChange={(event) => handleInputChange(event, "nameAlias")}
        />
        <FloatingLabel
          variant="filled"
          label="dn"
          value={inputValues.dn}
          onChange={(event) => handleInputChange(event, "dn")}
        />
        <FloatingLabel
          variant="filled"
          label="rn"
          value={inputValues.rn}
          onChange={(event) => handleInputChange(event, "rn")}
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
            <span className="font-medium">Request Sent</span> Tenent created
            with name {inputValues.tenant_name}
          </Alert>
        )}
        {isError && (
          <Alert
            color="info"
            className="mt-4"
            onDismiss={() => setIsSuccess(false)}
          >
            <span className="font-medium">Error</span> {isErrorMessage}
          </Alert>
        )}
      </div>
    </div>
  );
};

export default CreateTenant;
