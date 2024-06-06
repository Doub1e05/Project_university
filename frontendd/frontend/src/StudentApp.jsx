import React, { useState } from 'react';
import { Routes, Route, Link, BrowserRouter,useNavigate } from 'react-router-dom'; // Импортируем BrowserRouter
import AccountLabel from './account/Account';
import Tab1 from './tabs/tab1/tab1';
import Tab3 from './tabs/tab3/tab3';
import InProc from './tabs/procc';

import icon1 from './assets/Source/Icon/free-icon-gearwheel-3311767.png';
import icon2 from './assets/Source/Icon/free-icon-note-3311727.png';
import icon3 from './assets/Source/Icon/free-icon-notification-bell-3311730.png';
import icon4 from './assets/Source/Icon/free-icon-profile-3311746.png';
import './AuthApp.css'
import './App.css'


import icon1_a from './assets/Source/Icon/gear-a.png';
import icon2_a from './assets/Source/Icon/note-a.png';
import icon3_a from './assets/Source/Icon/bell-a.png';
import icon4_a from './assets/Source/Icon/prof-a.png';

function StudentApp() {
  const [activeTab, setActiveTab] = useState('tab1');
  const navigate = useNavigate();

  const handleTabClick = (tabId) => {
    setActiveTab(tabId);
  };

  const handleExitClick = () => {
    // Обработка выхода
  };

  return (
    <>
      <div className="wrapper">
        <div className="back"></div>
        <div className="container">
          <div className="left-w">
            <div className="top-cont">
              {activeTab === 'tab1' && <h2 className='title'>ГЛАВНАЯ • ПОЛУЧЕНИЕ ID</h2>}
              {activeTab === 'tab2' && <h2 className='title'>ГЛАВНАЯ • УСПЕВАЕМОСТЬ</h2>}
              {activeTab === 'tab3' && <h2 className='title'>ГЛАВНАЯ • УВЕДОМЛЕНИЯ</h2>}
              {activeTab === 'tab4' && <h2 className='title'>ГЛАВНАЯ • О СЕБЕ</h2>}
            </div>
            <div className="mid-cont">
              <div className="tab-contents">
                <Routes>
                  <Route path="/get-id" element={<Tab1 />} />
                  <Route path="/academic-performance" element={<InProc />} />
                  <Route path="/notifications" element={<Tab3 />} />
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
              {/* Тут предполагается передача name и role */}
              <AccountLabel name="fdafsa" role="Student"/>
            </div>
            <div className="mid-cont">
              <div className="tabs">
                <Link to="/get-id">
                  <button onClick={() => handleTabClick('tab1')} className={`tab-btn ${activeTab === 'tab1' ? 'active' : ''}`}>
                      <img className='tab-icon' src={activeTab === 'tab1' ? icon1_a : icon1} alt='nope'></img>
                      <span className='tab-title'>ПОЛУЧЕНИЕ ID</span>
                  </button>
                </Link>

                <Link to="/academic-performance">
                  <button onClick={() => handleTabClick('tab2')} className={`tab-btn ${activeTab === 'tab2' ? 'active' : ''}`}> 
                      <img className='tab-icon' src={activeTab === 'tab2' ? icon2_a : icon2} alt='nope'></img>
                      <span className='tab-title'>УСПЕВАЕМОСТЬ</span>
                  </button>
                </Link>
                  
                <Link to="/notifications">
                  <button onClick={() => handleTabClick('tab3')} className={`tab-btn ${activeTab === 'tab3' ? 'active' : ''}`}> 
                      <img className='tab-icon' src={activeTab === 'tab3' ? icon3_a : icon3} alt='nope'></img>
                      <span className='tab-title'>УВЕДОМЛЕНИЯ</span>
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
            <button className="exit-btn" onClick={() => handleExitClick()}>ВЫЙТИ</button>
          </div>
        </div>
      </div>
    </>
  );
}

function App() {
  return (
    <BrowserRouter> {/* Обертываем компонент StudentApp в BrowserRouter */}
      <StudentApp />
    </BrowserRouter>
  );
}

export default App;
