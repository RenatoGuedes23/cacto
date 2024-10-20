import { useContext, useState } from "react";
import { FloatingLabel, Button, Alert } from "flowbite-react";
import axiosInstance from "../../../api/localApi";
import Cookies from "js-cookie";
import { IpContext } from "../../../providers/ip";

import { ApiUrl } from "../../../utils/useApi";

function CreateBridgeDomainModal() {
  const { ip } = useContext(IpContext);
  const [inputValues, setInputValues] = useState({
    ip: ip || "",
    arpFlood: "",
    children: [],
    descricao: "",
    dn: "",
    mac: "",
    name: "",
    nameAlias: "",
    rn: "",
    status: "created",
    tenant_name: ""
  });

  const [isSuccess, setIsSuccess] = useState(false);
  const [isError, setIsError] = useState(false);
  const [errors, setErrors] = useState({});

  const handleInputChange = (event, variant) => {
    setInputValues({
      ...inputValues,
      [variant]: event.target.value,
    });
  };

  const validateInputs = () => {
    const newErrors = {};
    Object.keys(inputValues).forEach((key) => {
      if (!inputValues[key]) {
        newErrors[key] = "This field is required";
      }
    });
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = async () => {
    if (!validateInputs()) {
      setErrorMessage("Please fill in all the fields.");
      return;
    }
    setIsSuccess(false);
    setIsError(false);
    try {
      const apiLocal = `${ApiUrl}/tenant/bridge-domain?ip_address=${inputValues.ip}`;

      const response = await axiosInstance.post(apiLocal, {
        arpFlood: inputValues.arpFlood,
        children: inputValues.children,
        descr: inputValues.descricao,
        dn: inputValues.dn,
        mac: inputValues.mac,
        name: inputValues.name,
        nameAlias: inputValues.nameAlias,
        rn: inputValues.rn,
        status: inputValues.status,
        tenant_name: inputValues.tenant_name,
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
        {["ip", "tenant_name", "name", "descricao", "dn", "alias", "rn"].map((field) => (
          <div key={field} className="mb-4">
            <FloatingLabel
              variant="filled"
              label={field.replace("_", " ").toUpperCase()}
              value={inputValues[field]}
              name={field}
              onChange={handleInputChange}
              className={errors[field] ? "border-red-500" : ""}
            />
            {errors[field] && <p className="text-red-500 text-sm mt-1">{errors[field]}</p>}
          </div>
        ))}
        
          <FloatingLabel
            variant="filled"
            label="MAC"
            helperText="00:22:BD:F8:19:FF"
            value={inputValues.mac}
            onChange={(event) => handleInputChange(event, "mac")}
          />
          <FloatingLabel
            variant="filled"
            label="arp Flood"
            value={inputValues.arpFlood}
            onChange={(event) => handleInputChange(event, "arpFlood")}
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
};

export default CreateBridgeDomainModal;
