import { useContext, useState } from "react";
import { FloatingLabel, Button, Alert } from "flowbite-react";
import axiosInstance from "../../../api/localApi";
import Cookies from "js-cookie";
import { IpContext } from "../../../providers/ip";

function CreateVmWare() {
  const { ip } = useContext(IpContext);
  const [inputValues, setInputValues] = useState({
    ip_address: ip,
    vmware_name: ""
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
      const apiLocal = `http://localhost:8000/vmware`;

      const response = await axiosInstance({
        method: "post",
        url: apiLocal,
        headers: { Authorization: localStorage.getItem("APIC-cookie") },
        data: {
          "ip_address": inputValues.ip_address,
          "vmware_name": inputValues.vmware_name
        }
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
            label="ip_address"
            value={inputValues.ip_address}
            // onChange={(event) => handleInputChange(event, "ip")}
          />
          <FloatingLabel
            variant="filled"
            label="VMware Name"
            value={inputValues.tenent}
            onChange={(event) => handleInputChange(event, "vmware_name")}
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
              <span className="font-medium">Request Sent</span> VMware was
              created successfully"
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

export default CreateVmWare;
