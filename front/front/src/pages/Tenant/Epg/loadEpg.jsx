import { useContext, useState } from "react";
import {
  Table,
  Button,
  Label,
  TextInput,
  Spinner,
  Alert,
} from "flowbite-react";
import axiosInstance from "../../../api/localApi";
import { IpContext } from "../../../providers/ip";

import { ApiUrl } from "../../../utils/useApi";

const LoadEpg = () => {
  const { ip } = useContext(IpContext);
  const [data, setData] = useState([]);
  const [isResult, setIsResult] = useState(true);
  const [isLoading, setIsLoading] = useState(false);
  const [isFirstLoad, setIsFirstLoad] = useState(true);
  const [errorMessage, setErrorMessage] = useState("");

  const [inputValues, setInputValues] = useState({
    ip: ip || "",
    tenant_name: "",
    application_name: "",
  });

  const deleteRow = (targetId) => {
    setData((prevData) => prevData.filter((_, index) => index !== targetId));
  };

  const handleInputChange = (event, variant) => {
    setInputValues((prevValues) => ({
      ...prevValues,
      [variant]: event.target.value,
    }));
  };

  const handleSubmit = async () => {
    setIsLoading(true);
    setIsFirstLoad(false);
    setErrorMessage("");
    try {
      const apiLocal = `${ApiUrl}/tenant/epg/${inputValues.tenant_name}/${inputValues.application_name}?ip_address=${inputValues.ip}`;
      const response = await axiosInstance.get(apiLocal, {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("APIC-cookie")}`,
        },
      });

      if (response.data) {
        setData(response.data);
        setIsResult(true);
      } else {
        setData([]);
        setIsResult(false);
      }
    } catch (error) {
      console.error(error);
      setErrorMessage("Failed to load EPG data. Please try again.");
      setIsResult(false);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <>
      <div className="flex max-w-md flex-col gap-4 mb-4">
        <div>
          <div className="mb-2 block">
            <Label htmlFor="ip_address" value="IP Address" />
          </div>
          <TextInput
            id="ip_address"
            type="text"
            sizing="sm"
            value={inputValues.ip}
            onChange={(event) => handleInputChange(event, "ip")}
          />
          <div className="mb-2 block">
            <Label htmlFor="tenant_name" value="Tenant Name" />
          </div>
          <TextInput
            id="tenant_name"
            type="text"
            sizing="sm"
            value={inputValues.tenant_name}
            onChange={(event) => handleInputChange(event, "tenant_name")}
          />
          <div className="mb-2 block">
            <Label htmlFor="application_name" value="Application Name" />
          </div>
          <TextInput
            id="application_name"
            type="text"
            sizing="sm"
            value={inputValues.application_name}
            onChange={(event) => handleInputChange(event, "application_name")}
          />
        </div>
        <Button color="success" onClick={handleSubmit}>
          Submit
        </Button>
      </div>
      {isLoading && (
        <div className="flex justify-center items-center my-4">
          <Spinner aria-label="Loading spinner" size="xl" />
        </div>
      )}
      {!isFirstLoad && errorMessage && (
        <Alert color="failure" className="mt-4">
          <span className="font-medium">Error: </span>
          {errorMessage}
        </Alert>
      )}
      <div>
        {data.totalCount && <p>Total Count: {data.totalCount}</p>}
        {data.imdata && (
        <Table hoverable>
          <Table.Head>
            <Table.HeadCell>Name</Table.HeadCell>
            <Table.HeadCell>dn</Table.HeadCell>
            <Table.HeadCell>configSt</Table.HeadCell>
            <Table.HeadCell>userdom</Table.HeadCell>
            <Table.HeadCell>shutdown</Table.HeadCell>
          </Table.Head>
          <Table.Body className="divide-y">
            {isLoading && (
              <Spinner aria-label="Extra large spinner" size="xl" />
            )}

            {data.imdata && data.imdata.length > 0 ? (
              data.imdata.map((items, index) => (
                <Table.Row
                  key={index}
                  className="bg-white dark:border-gray-700 dark:bg-gray-800"
                >
                  <Table.Cell className="whitespace-nowrap font-medium text-gray-900 dark:text-white">
                    {items.fvAEPg.attributes.name}
                  </Table.Cell>
                  <Table.Cell className="whitespace-nowrap font-medium text-gray-900 dark:text-white">
                    {items.fvAEPg.attributes.dn}
                  </Table.Cell>
                  <Table.Cell className="whitespace-nowrap font-medium text-gray-900 dark:text-white">
                    {items.fvAEPg.attributes.configSt}
                  </Table.Cell>
                  <Table.Cell className="whitespace-nowrap font-medium text-gray-900 dark:text-white">
                    {items.fvAEPg.attributes.userdom}
                  </Table.Cell>
                  <Table.Cell className="whitespace-nowrap font-medium text-gray-900 dark:text-white">
                    {items.fvAEPg.attributes.shutdown}
                  </Table.Cell>
                </Table.Row>
              ))
            ) : (
              <Table.Row className="bg-white dark:border-gray-700 dark:bg-gray-800">
                <Table.Cell className="whitespace-nowrap font-medium text-gray-900 dark:text-white">
                  <p>You don't have any Bridge Domains Created</p>
                </Table.Cell>
              </Table.Row>
            )}
          </Table.Body>
        </Table>
        )}
      </div>
    </>
  );
};

export default LoadEpg;
