import React, { useState } from "react";
import { Button, FileInput, Label, Progress } from "flowbite-react";

function timeout(delay) {
  return new Promise((res) => setTimeout(res, delay));
}

const LoadTenantFromFile = () => {
  const [selectedFile, setSelectedFile] = useState();

  const [submitBar, setSubmitBar] = useState(false);
  const [submitBarValue, setSubmitBarValue] = useState(0);

  function startTimer(value) {
    setTimeout(function () {
      // Start the timer
      setSubmitBarValue(value); // After 1 second, set render to true
    }, 2000);
  }  

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleSubmit = () => {
    // if (!selectedFile) {
    //   alert("Please select a file first");
    //   return;
    // }
    startTimer(100)

    setSubmitBar(true);
    // todo: add send to server when api is ready
    console.log(selectedFile);
  };

  return (
    <div className="w-full items-center justify-center">
      <div className="flex flex-col space-y-4">
        <Label
          htmlFor="dropzone-file"
          className="flex h-64 w-full cursor-pointer flex-col items-center justify-center rounded-lg border-2 border-dashed border-gray-300 bg-gray-50 hover:bg-gray-100 dark:border-gray-600 dark:bg-gray-700 dark:hover:border-gray-500 dark:hover:bg-gray-600"
        >
          <div className="flex flex-col items-center justify-center pb-6 pt-5">
            <svg
              className="mb-4 h-8 w-8 text-gray-500 dark:text-gray-400"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 20 16"
            >
              <path
                stroke="currentColor"
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="2"
                d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2"
              />
            </svg>
            <p className="mb-2 text-sm text-gray-500 dark:text-gray-400">
              <span className="font-semibold">Click to upload</span> or drag and
              drop
            </p>
            <p className="text-xs text-gray-500 dark:text-gray-400">
              SVG, PNG, JPG or GIF (MAX. 800x400px)
            </p>
          </div>
          <FileInput
            id="dropzone-file"
            className="hidden"
            onChange={handleFileChange}
          />
        </Label>
        <Button color="success" onClick={handleSubmit}>
          Submit File
        </Button>
        {submitBar && (
          <Progress
            progress={submitBarValue}
            progressLabelPosition="outside"
            textLabel="Submit Progress"
            textLabelPosition="outside"
            size="md"
            labelProgress
            labelText
          />
        )}
      </div>
    </div>
  );
};

export default LoadTenantFromFile;
