
import { Button, Modal, Select } from "flowbite-react";
import { useState } from "react";

import Autenticate from "./autenticate";

function Authenticate() {
  const [openModal, setOpenModal] = useState(true);
  const [modalPlacement, setModalPlacement] = useState('center')

  return (
    <>
      <Modal
        show={openModal}
        position={modalPlacement}
        onClose={() => setOpenModal(false)}
      >
        <Modal.Header>Terms of Service</Modal.Header>
        <Modal.Body>
          <div className="space-y-6 p-6">
            <p className="text-base leading-relaxed text-gray-500 dark:text-gray-400">
              Welcome to our innovative NTT! This project is in its
              experimental phase and is designed to interact with the Cisco API.
              We appreciate your participation and feedback as we continue to
              develop and refine this initiative. I hope this version conveys
              the message more effectively. Let me know if you need further
              assistance!
            </p>
          </div>
        </Modal.Body>
        <Modal.Footer>
          <Button onClick={() => setOpenModal(false)}>I accept</Button>
          <Button color="gray" onClick={() => setOpenModal(false)}>
            Decline
          </Button>
        </Modal.Footer>
      </Modal>
      <Autenticate></Autenticate>
    </>
  );
}

export default Authenticate;