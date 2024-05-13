import React, { useState } from 'react';

function FileUpload() {
  const [file, setFile] = useState(null);

  const handleFileChange = (e) => {
    const uploadedFile = e.target.files[0];
    setFile(uploadedFile);
  };

  return (
    <div>
      <input type="file" onChange={handleFileChange} accept=".pdf" />
      {file && (
        <div>
          <h2>Uploaded File :</h2>
          <embed src={URL.createObjectURL(file)} width="500" height="600" />
        </div>
      )}
    </div>
  );
}

function App() {
  return (
    <div className="App">
      <h1>PDF File Upload</h1>
      <FileUpload />
      <button>Calculate Score</button>
    </div>
  );
}

export default App;