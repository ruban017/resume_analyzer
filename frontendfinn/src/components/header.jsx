import React,{useState} from "react";
import axios from 'axios';
// import {Result} from './result';
// import uploadImg from "./upl.png";

function FileUpload() {
  const [file, setFile] = useState(null);
  const [jd, setJd] = useState(null);
  // const [score, setScore] = useState('');
  const [imageUrl, setImageUrl] = useState('');

  const handleFileChange = (e) => {
    const uploadedFile = e.target.files[0];
    setFile(uploadedFile);
  };

  const handleInputChange = (event) => {
    const jdd = event.target.value; 
    setJd(jdd);
}
  const formData = new FormData();
  formData.append('resume', file);
  formData.append('desc', jd);

  const handleCalculateScore = async () => {
    console.log("CLicked!!!!!!!!!!!!!!")
      try {
        const response = await axios.post('https://resume-analyzer-8l4f.onrender.com/', formData,{
          headers: {
            "Content-Type": "multipart/form-data",
          },
          responseType:'blob'
        });
        const data = await response.data;
        // console.log(data.score);
        const url = URL.createObjectURL(data);
        // setScore(data.score);
        // console.log('Image URL:',url);
        setImageUrl(url);

        } catch (error) {
        console.error('Error:', error);
    }
};

  return (
    <div>
      <input type="file" className="" onChange={handleFileChange} accept=".pdf" />
      <textarea id="inp" placeholder="Enter the Job Description" className="" onChange={handleInputChange}/>
      {file && (
        <div>
          <h2>Uploaded File:</h2>
          <embed src={URL.createObjectURL(file)} width="500" height="600" />
        </div>
      )}
      <div>
      <button className = " page-scroll" id="butt" onClick={handleCalculateScore}>Calculate Score</button>
      </div>
      {imageUrl && <img className="mt-30px" src={imageUrl} alt="Generated Chart" />}

      {/* {score !== null && <p className="mt-30px" id='butt'>Calculated Score: {score.toFixed(3)}</p>} */}

    </div>
      // <div className="app">
      //   <div className="parent">
      //     <div className="file-upload">
      //       {/* <img src={uploadImg} alt="upload" /> */}
      //       <h3>Click box to upload</h3>
      //       <p>Maximun file size 10mb</p>
      //       <input type="file" />
      //     </div>
      //   </div>
      // </div>
    );
}

export const Header = (props) => {
  return (
    <header id="header">
      <div className="intro">
        <div className="overlay">
          <div className="container">
            <div className="row">
              <div className="col-md-8 col-md-offset-2 intro-text">
                <h1>
                  {props.data ? props.data.title : "Loading"}
                  <span></span>
                </h1>
                <p>{props.data ? props.data.paragraph : "Loading"}</p>
                <div id="main" className="btn btn-custom btn-lg page-scroll">
                  {/* <h1>PDF File Upload</h1> */}
                    <FileUpload />
                      </div>
                {/* <a
                  href="#features"
                  className="btn btn-custom btn-lg page-scroll"
                >
                  Upload file
                </a>{" "} */}
              </div>
            </div>
          </div>
        </div>
      </div>
    </header>
  );
};
