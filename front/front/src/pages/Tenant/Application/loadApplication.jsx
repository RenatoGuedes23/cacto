import { useContext, useState } from "react";
import {
  Table,
  Button,
  Modal,
  Label,
  TextInput,
  Spinner,
} from "flowbite-react";
import axiosInstance from "../../../api/localApi";
import { IpContext } from "../../../providers/ip";

import { ApiUrl } from "../../../utils/useApi";

const LoadApplication = () => {
  const { ip } = useContext(IpContext);
  const [data, setData] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [isResult, setIsResult] = useState(false);

  const [inputValues, setInputValues] = useState({
    ip: ip || "",
    tenant_name: "",
    application_name: ""
  });

  const deleteRow = (targetId) => {
    const newArr = [...data];
    newArr.splice(targetId, 1);
    setData(newArr);
  };

  const handleInputChange = (event, variant) => {
    setInputValues({
      ...inputValues,
      [variant]: event.target.value,
    });
  };

  const handleSubmit = async () => {
    setIsLoading(true);
    try {
      const apiLocal = `${ApiUrl}/tenant/application/${inputValues.tenant_name}?ip_address=${inputValues.ip}`;

      const response = await axiosInstance.get(apiLocal, {
        headers: { Authorization: `Bearer ${localStorage.getItem("APIC-cookie")}` }
      });

      if (response.data) {
        setIsLoading(false);
        setData(response.data);
        setIsResult(true);
      }
    } catch (error) {
      console.error(error);
      setIsLoading(false);
      setIsResult(false);
    }
  };

  return (
    <>
      <div className="flex max-w-md flex-col gap-4 mb-4">
        <div>
          <div className="mb-2 block">
            <Label htmlFor="small" value="IP Address" />
          </div>
          <TextInput
            id="small"
            type="text"
            sizing="sm"
            value={inputValues.ip}
            onChange={(event) => handleInputChange(event, "ip")}
          />
          <div className="mb-2 block">
            <Label htmlFor="small" value="Tenant Name" />
          </div>
          <TextInput
            id="small"
            type="text"
            sizing="sm"
            onChange={(event) => handleInputChange(event, "tenant_name")}
          />
        </div>
        <Button color="success" onClick={handleSubmit}>
          Enviar
        </Button>
      </div>
      <div>
          {data.totalCount && (
            <p>Total Count: {data.totalCount}</p>
          )}
          </div>
      <Table hoverable>
        <Table.Head>
          <Table.HeadCell>Results</Table.HeadCell>
          <Table.HeadCell></Table.HeadCell>
        </Table.Head>
        <Table.Body className="divide-y">
          {isLoading && (
            <Spinner aria-label="Extra large spinner example" size="xl" />
          )}
          

          {isResult && data.imdata.length > 0 ? (
            data.imdata.map((items, index) => (
              <Table.Row
                key={index}
                className="bg-white dark:border-gray-700 dark:bg-gray-800"
              >
                <Table.Cell className="whitespace-nowrap font-medium text-gray-900 dark:text-white">
                  {items.fvAp.attributes.name}
                </Table.Cell>
                <Table.Cell>
                  <a
                    onClick={(e) => deleteRow(e.target.id)}
                    className="float-right mr-20 font-medium text-red-600 hover:underline dark:text-red-500"
                  >
                    Remove
                  </a>
                </Table.Cell>
              </Table.Row>
            ))
          ) : (
            <Table.Row className="bg-white dark:border-gray-700 dark:bg-gray-800">
              <Table.Cell className="whitespace-nowrap font-medium text-gray-900 dark:text-white">
                <p>You don't have any Application Created</p>
              </Table.Cell>
            </Table.Row>
          )}
        </Table.Body>
      </Table>
    </>
  );
};

export default LoadApplication;
