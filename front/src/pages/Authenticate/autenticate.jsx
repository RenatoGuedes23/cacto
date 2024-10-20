import { useState, useContext } from "react";
import { FloatingLabel, Button, Alert } from "flowbite-react";
import axiosInstance from "../../api/localApi";
import Cookies from "js-cookie";
import { IpContext } from "../../providers/ip";

import { ApiUrl } from "../../utils/useApi";

function Autenticate() {
  const { ip } = useContext(IpContext);
  const [inputValues, setInputValues] = useState({
    ip: ip || "",
    name: "",
    pwd: "",
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
    setIsSuccess(false);
    setIsError(false);
    try {
      const apiLocal = `${ApiUrl}/autenticate?ip_address=`;
      console.log(apiLocal + inputValues.ip)


      const response = await axiosInstance({
        method: 'post',
        url: apiLocal + inputValues.ip,
        headers: {},
        data: {
          name: inputValues.name,
          pwd: inputValues.pwd,
        }
      });

      if (response.data && response.data.token) {
        localStorage.setItem("APIC-Cookie", response.data.token);
        axiosInstance.defaults.headers["Authorization"] = response.data.token;
        Cookies.set("APIC-Cookie", response.data.token);
        setToken(response.data.token);
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
            label="name"
            value={inputValues.name}
            onChange={(event) => handleInputChange(event, "name")}
          />
          <FloatingLabel
            variant="filled"
            label="pwd"
            value={inputValues.pwd}
            onChange={(event) => handleInputChange(event, "pwd")}
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
              <span className="font-medium">Request Sent</span> APIC-Token was
              retrieved
            </Alert>
          )}
          {isError && (
            <Alert
              color="info"
              className="mt-4"
              onDismiss={() => setIsSuccess(false)}
            >
              <span className="font-medium">Error</span> No token
            </Alert>
          )}
        </div>
      </div>
    </div>
  );
}

export default Autenticate;
