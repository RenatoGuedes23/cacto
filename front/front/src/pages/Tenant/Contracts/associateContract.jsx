import { useContext, useState } from "react";
import { FloatingLabel, Button, Alert } from "flowbite-react";
import axiosInstance from "../../../api/localApi";
import { IpContext } from "../../../providers/ip";

function AssociateContract() {
  const { ip } = useContext(IpContext);
  const [inputValues, setInputValues] = useState({
    ip: ip || "",
    tenant_name: "",
    l3out_name: "",
    ext_epg_name: "",
    contract_name: "",
  });

  const [errors, setErrors] = useState({});
  const [successMessage, setSuccessMessage] = useState("");
  const [errorMessage, setErrorMessage] = useState("");

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setInputValues((prevValues) => ({
      ...prevValues,
      [name]: value,
    }));
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

    setSuccessMessage("");
    setErrorMessage("");

    try {
      const apiLocal = `${ApiUrl}/tenant/contract/associate-contract-as-provided?ip_address=${inputValues.ip}`;

      const response = await axiosInstance.post(apiLocal, {
        tenant_name: inputValues.tenant_name,
        l3out_name: inputValues.l3out_name,
        ext_epg_name: inputValues.ext_epg_name,
        contract_name: inputValues.contract_name,
      }, {
        headers: { Authorization: `Bearer ${localStorage.getItem("APIC-cookie")}` }
      });

      if (response.data) {
        setSuccessMessage("Contract was associated successfully");
      }
    } catch (error) {
      console.error(error);
      setErrorMessage("Failed to associate the contract");
    }
  };

  return (
    // <div className="flex flex-col items-center p-4">
    <div>
      <div className="w-full ">
        {["ip", "tenant_name", "l3out_name", "ext_epg_name", "contract_name"].map((field) => (
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
        <Button color="success" onClick={handleSubmit}>
          Associate Contract
        </Button>
        {successMessage && (
          <Alert color="success" className="mt-4" onDismiss={() => setSuccessMessage("")}>
            <span className="font-medium">Success: </span>{successMessage}
          </Alert>
        )}
        {errorMessage && (
          <Alert color="failure" className="mt-4" onDismiss={() => setErrorMessage("")}>
            <span className="font-medium">Error: </span>{errorMessage}
          </Alert>
        )}
      </div>
    </div>
  );
}

export default AssociateContract;
