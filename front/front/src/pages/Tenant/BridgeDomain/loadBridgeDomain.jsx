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

const LoadBridgeDomain = () => {
  const { ip } = useContext(IpContext);
  const [data, setData] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [isResult, setIsResult] = useState(false);

  const [inputValues, setInputValues] = useState({
    ip: ip || "",
    arpFlood: "",
    children: [],
    descr: "",
    dn: "",
    mac: "",
    name: "",
    nameAlias: "",
    rn: "",
    status: "created",
    tenant_name: ""
  });

  const handleInputChange = (event, variant) => {
    setInputValues({
      ...inputValues,
      [variant]: event.target.value,
    });
  };

  const handleSubmit = async () => {
    setIsLoading(true);
    try {
      const apiLocal = `${ApiUrl}/tenant/bridge-domain/${inputValues.tenant_name}?ip_address=${inputValues.ip}`;

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
        </Table.Head>
        <Table.Head>
          <Table.HeadCell>Name</Table.HeadCell>
          <Table.HeadCell>MAC</Table.HeadCell>
          <Table.HeadCell>bcastP</Table.HeadCell>
          <Table.HeadCell>arpFlood</Table.HeadCell>
          <Table.HeadCell>monPolDn</Table.HeadCell>
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
                  {items.fvBD.attributes.name}
                </Table.Cell>
                <Table.Cell className="whitespace-nowrap font-medium text-gray-900 dark:text-white">
                  {items.fvBD.attributes.mac}
                </Table.Cell>
                <Table.Cell className="whitespace-nowrap font-medium text-gray-900 dark:text-white">
                  {items.fvBD.attributes.bcastP}
                </Table.Cell>
                <Table.Cell className="whitespace-nowrap font-medium text-gray-900 dark:text-white">
                  {items.fvBD.attributes.arpFlood}
                </Table.Cell>
                <Table.Cell className="whitespace-nowrap font-medium text-gray-900 dark:text-white">
                  {items.fvBD.attributes.monPolDn}
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
    </>
  );
};

export default LoadBridgeDomain;
