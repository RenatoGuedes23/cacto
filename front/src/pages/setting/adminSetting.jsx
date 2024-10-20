import { useContext, useState } from "react";
import { Button, FloatingLabel, Label} from "flowbite-react";
import { IpContext } from "../../providers/ip";

const AdminSetting = () => {
    const { ip, setIp} = useContext(IpContext);
    const [ipValue, setIpValue] = useState()

    const handleInputChange = (event) => {
      setIpValue(
        event.target.value,
      );
    };

    return (
    <div className="grid grid-flow-col justify-stretch space-x-4 p-4 m-4">
      <div>
        <Label> Current Ip: {ip}</Label>
        <FloatingLabel
          variant="filled"
          label="Ip"
          value={ipValue}
          onChange={(event) => handleInputChange(event)}
        />
        <Button color="success" onClick={() => {setIp(ipValue)}}>
          Enviar
        </Button>
      </div>
    </div>
  );
};

export default AdminSetting;
