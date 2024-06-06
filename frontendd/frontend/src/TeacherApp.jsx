import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Routes, Route, Link } from 'react-router-dom';
import AccountLabel from './account/Account';
import Tab5 from './tabs/tab5/tab5';
import InProc from './tabs/procc';
import './AuthApp.css';
import Cookies from 'js-cookie';
import App from './App.jsx';

import icon1 from './assets/Source/Icon/free-icon-gearwheel-3311767.png';
import icon2 from './assets/Source/Icon/free-icon-note-3311727.png';
import icon3 from './assets/Source/Icon/free-icon-notification-bell-3311730.png';
import icon4 from './assets/Source/Icon/free-icon-profile-3311746.png';

import icon1_a from './assets/Source/Icon/gear-a.png';
import icon2_a from './assets/Source/Icon/note-a.png';
import icon3_a from './assets/Source/Icon/bell-a.png';
import icon4_a from './assets/Source/Icon/prof-a.png';

function TeacherApp(props) {
  const [activeTab, setActiveTab] = useState('tab5');
  const [name, setName] = useState("");
  const [role, setRole] = useState("");
  const [currentUser, setCurrentUser] = useState();
  const [username, setUsername] = useState("")
  const [password, setPassword] = useState("")
  const [profileData, setProfileData] = useState(null)
  const [subjectsData, setSubjectsData] = useState(null)

  const handleTabClick = (tabId) => {
    setActiveTab(tabId);
  };

  useEffect(() => {
    const fetchProfile = async () => {
      try {
        const res = await axios.get(
          "http://localhost:8000/api/profile", 
          { withCredentials: true }
        );

        if (res.status === 200) {
          setCurrentUser(true)
          setProfileData(res.data)
        } else {
          setCurrentUser(false)
          console.log("Profile request failed with status:", res.status)
        }
      } catch (error) {
        setCurrentUser(false)
        console.log(error)
      }
    }
    fetchProfile()
  }, [])

  const handleExitClick = async (e) => {
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
        setCurrentUser(false);
        Cookies.remove('sessionid');
    } catch (error) {
      console.log(error);
    }
  };
  if (!currentUser){
    <App/>
  } 
  else{
   return (
    <>
      <div className="wrapper">
        <div className="back"></div>
        <div className="container">
          <div className="left-w">
            <div className="top-cont">
              {activeTab === 'tab5' && <h2 className='title'>ГЛАВНАЯ • ПРОВЕРКА РАБОТ</h2>}
              {activeTab === 'tab6' && <h2 className='title'>ГЛАВНАЯ • СПИСКИ РАБОТ</h2>}
              {activeTab === 'tab4' && <h2 className='title'>ГЛАВНАЯ • О СЕБЕ</h2>}
            </div>
            <div className="mid-cont">
              <div className="tab-contents">
                <Routes>
                  <Route path="/verification" element={<Tab5 />} />
                  <Route path="/list" element={<InProc />} />
                  <Route path="/about-me" element={<InProc />} />
                </Routes>
              </div>
            </div>
            <div className="end-cont">
              <span>© Copyright 2024 «VyatFlow» — Все права защищены.</span>
            </div>
          </div>

          <div className="right-w">
            <div className="top-cont">
              <AccountLabel name='Пахарева И.В.' role="Преподаватель" />
            </div>
            <div className="mid-cont">
              <div className="tabs">
                <Link to="/verification">
                  <button onClick={() => handleTabClick('tab5')} className={`tab-btn ${activeTab === 'tab5' ? 'active' : ''}`}>
                    <img className='tab-icon' src={activeTab === 'tab5' ? icon1_a : icon1} alt='nope'></img>
                    <span className='tab-title'>ПРОВЕРКА РАБОТ</span>
                  </button>
                </Link>

                <Link to="/list">
                  <button onClick={() => handleTabClick('tab6')} className={`tab-btn ${activeTab === 'tab6' ? 'active' : ''}`}>
                    <img className='tab-icon' src={activeTab === 'tab6' ? icon2_a : icon2} alt='nope'></img>
                    <span className='tab-title'>СПИКСКИ РАБОТ</span>
                  </button>
                </Link>

                <Link to="/about-me">
                  <button onClick={() => handleTabClick('tab4')} className={`tab-btn ${activeTab === 'tab4' ? 'active' : ''}`}>
                    <img className='tab-icon' src={activeTab === 'tab4' ? icon4_a : icon4} alt='nope'></img>
                    <span className='tab-title'>О СЕБЕ</span>
                  </button>
                </Link>

              </div>
            </div>
            <div className="end-cont">
              <button className="exit-btn" onClick={handleExitClick}>ВЫЙТИ</button>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
}

export default TeacherApp;
