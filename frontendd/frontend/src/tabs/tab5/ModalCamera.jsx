// ModalCamera.jsx

import React, { useState, useEffect, useRef } from 'react';
import { Modal, Button } from 'react-bootstrap';
import axios from 'axios';
import './ModalCamera.css';

const ModalCamera = ({ show, onClose }) => {
  const [imageData, setImageData] = useState(null);
  const [resultData, setResultData] = useState(null);
  const videoRef = useRef(null);
  const canvasRef = useRef(null);

  useEffect(() => {
    if (show) {
      startCamera();
    } else {
      stopCamera();
    }
  }, [show]);

  const startCamera = async () => {
    try {
      const mediaStream = await navigator.mediaDevices.getUserMedia({ video: true });
      videoRef.current.srcObject = mediaStream;
      videoRef.current.play();
    } catch (error) {
      console.error('Error accessing camera:', error);
    }
  };

  const stopCamera = () => {
    if (videoRef.current && videoRef.current.srcObject) {
      const tracks = videoRef.current.srcObject.getTracks();
      tracks.forEach(track => track.stop());
    }
  };

  const handleCapture = () => {
    const canvas = canvasRef.current;
    const video = videoRef.current;
    const ctx = canvas.getContext('2d');

    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
    const capturedImage = canvas.toDataURL('image/png');
    setImageData(capturedImage);

    const dataURLtoFile = (dataurl, filename) => {
      const arr = dataurl.split(','), mime = arr[0].match(/:(.*?);/)[1];
      const bstr = atob(arr[1]);
      let n = bstr.length;
      const u8arr = new Uint8Array(n);
      while (n--) {
        u8arr[n] = bstr.charCodeAt(n);
      }
      return new File([u8arr], filename, { type: mime });
    }

    const file = dataURLtoFile(capturedImage, 'capture.png');

    const formData = new FormData();
    formData.append('image', file);

    axios.post('http://localhost:8000/api/process_image/', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    }).then(response => {
      setResultData(response.data.digits);
    }).catch(error => {
      console.error('Error uploading image:', error);
    });
  };

  const handleClose = () => {
    setImageData(null);
    setResultData(null);
    onClose();
    stopCamera();
  };

  return (
    <Modal show={show} onHide={handleClose} centered>
      <Modal.Header closeButton>
        <Modal.Title>Камера</Modal.Title>
      </Modal.Header>
      <Modal.Body>
        <div className="camera-container">
          {imageData ? (
            <div className="captured-image">
              <img src={imageData} alt="Captured" />
              {resultData && (
                <div className="result">
                  <h4>Распознанные цифры:</h4>
                  <p>{resultData.join(', ')}</p>
                </div>
              )}
            </div>
          ) : (
            <video ref={videoRef} className="video-stream" />
          )}
          <canvas ref={canvasRef} style={{ display: 'none' }} />
        </div>
      </Modal.Body>
      <Modal.Footer>
        <Button variant="secondary" onClick={handleClose}>Закрыть</Button>
        {!imageData && (
          <Button variant="primary" onClick={handleCapture}>Сделать фото</Button>
        )}
      </Modal.Footer>
    </Modal>
  );
};

export default ModalCamera;
