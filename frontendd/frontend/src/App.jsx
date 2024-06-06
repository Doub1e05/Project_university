import axios from "axios";
import { useEffect, useState } from "react";
import { BrowserRouter } from "react-router-dom"; // Импортируем BrowserRouter
import "./App.css";
import Cookies from 'js-cookie';
import StudentApp from "./StudentApp"; // Импортируем компонент StudentApp
import TeacherApp from "./TeacherApp";
import logo from './assets/Source/Image/f80500c5-3d98-4dc0-b2a3-be256e2078e8.jpg';

function App() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [currentUser, setCurrentUser] = useState(false);
  const [profileData, setProfileData] = useState(null);

  useEffect(() => {
    const getProfile = async () => {
      try {
        const res = await axios.get(
          "http://localhost:8000/api/profile/",
          { withCredentials: true }
        );

        if (res.status === 200) {
          setCurrentUser(true);
          setProfileData(res.data);
        } else {
          setCurrentUser(false);
          console.log("Profile request failed with status:", res.status);
        }
      } catch (error) {
        setCurrentUser(false);
        console.log(error);
      }
    };
    getProfile();
  }, []);

  const handleChange = (event) => {
    const { name, value } = event.target;
    if (name === "username") setUsername(value);
    if (name === "password") setPassword(value);
  };

  const submitLogin = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post(
        "http://localhost:8000/api/login/",
        {
          login: username,
          password: password,
        },
        { withCredentials: true }
      );
      if (res.status === 200) {
        setCurrentUser(true);
        // Fetch profile data after successful login
        const profileRes = await axios.get(
          "http://localhost:8000/api/profile/",
          { withCredentials: true }
        );
        setProfileData(profileRes.data);
      } else {
        console.log("Login failed with status:", res.status);
      }
    } catch (error) {
      console.log(error);
    }
  };

  const submitLogout = async (e) => {
    e.preventDefault();
    try {
      const csrftoken = Cookies.get('csrftoken');
      const res = await axios.post(
        "http://localhost:8000/api/logout/",
        null,
        {
          withCredentials: true,
          headers: {
            'X-CSRFToken': csrftoken
          }
        }
      );
      if (res.status === 200) {
        setCurrentUser(false);
        Cookies.remove('sessionid');
      } else {
        console.log("Logout failed with status:", res.status);
      }
    } catch (error) {
      console.log(error);
    }
  };

  if (currentUser){
    return (
      <BrowserRouter>
        <TeacherApp />
      </BrowserRouter>
    );
  }
  
  return (
    <>
      <div className="wrapper">
        <div className="back"></div>
        <div className="auth">
          <h2 className="auth-title">АВТОРИЗАЦИЯ</h2>
          <form onSubmit={submitLogin}>
            <label>
              <div className="title-input">Логин:</div>
              <input className='auth-input' type="text" name="username" value={username} onChange={handleChange} />
            </label>
            <label>
            <div className="title-input">Пароль:</div>
              <input className='auth-input' type="password" name="password" value={password} onChange={handleChange} />
            </label>
            <button className='auth-btn' type="submit">Войти</button>
          </form>
          <div className="alt-login">
            <div className="alt-login-title">войти с помощью</div>
            <img src={logo} alt="logo" className="logo-icon" />
          </div>
        </div>
      </div>    
    </>
  );
}

export default App;
