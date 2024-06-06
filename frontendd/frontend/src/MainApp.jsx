// import axios from "axios"
// import { useEffect, useState } from "react"
// import "./App.css"
// import Cookies from 'js-cookie'

// import { useState } from 'react'
// import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";

// import './App.css'
// import AccountLabel from './account/Account'
// import Tab1 from './tabs/tab1/tab1';
// import Tab3 from './tabs/tab3/tab3'
// import Tab5 from './tabs/tab5/tab5'
// import Tab6 from './tabs/tab6/tab6'
// import InProc from './tabs/procc';

// import icon1 from './assets/Source/Icon/free-icon-gearwheel-3311767.png'
// import icon2 from './assets/Source/Icon/free-icon-note-3311727.png'
// import icon3 from './assets/Source/Icon/free-icon-notification-bell-3311730.png'
// import icon4 from './assets/Source/Icon/free-icon-profile-3311746.png'


// import icon1_a from './assets/Source/Icon/gear-a.png'
// import icon2_a from './assets/Source/Icon/note-a.png'
// import icon3_a from './assets/Source/Icon/bell-a.png'
// import icon4_a from './assets/Source/Icon/prof-a.png'

// export default function App(props) {
//   const role = props.user.role
//   const name = props.user.name.toUpperCase()


//   const [activeTab, setActiveTab] = useState('tab1');

//   const handleTabClick = (tabId) => {
//     setActiveTab(tabId);
//   };

//   const handleExitClick = () => {
    
//   };

//   if (role === 'студент') {
//     return (
//       <>
//         <div className="wrapper">
//           <div className="back"></div>
//           <div className="container">
//             <div className="left-w">
//               <div className="top-cont">
//                   {activeTab === 'tab1' && <h2 className='title'>ГЛАВНАЯ • ПОЛУЧЕНИЕ ID</h2>}
//                   {activeTab === 'tab2' && <h2 className='title'>ГЛАВНАЯ • УСПЕВАЕМОСТЬ</h2>}
//                   {activeTab === 'tab3' && <h2 className='title'>ГЛАВНАЯ • УВЕДОМЛЕНИЯ</h2>}
//                   {activeTab === 'tab4' && <h2 className='title'>ГЛАВНАЯ • О СЕБЕ</h2>}
//               </div>
//               <div className="mid-cont">
//                 <div className="tab-contents">
//                   <Routes>
//                     <Route path="/get-id" element={<Tab1 />} />
//                     <Route path="/academic-performance" element={<InProc />} />
//                     <Route path="/notifications" element={<Tab3 />} />
//                     <Route path="/about-me" element={<InProc />} />
//                   </Routes>
//                 </div>
//               </div>
//               <div className="end-cont">
//                 <span>© Copyright 2024 «VyatFlow» — Все права защищены.</span>
//               </div>
//             </div>

//             <div className="right-w">
//               <div className="top-cont">
//                 <AccountLabel name={name} role={role}/>
//               </div>
//               <div className="mid-cont">
//                 <div className="tabs">
//                   <Link to="/get-id">
//                     <button onClick={() => handleTabClick('tab1')} className={`tab-btn ${activeTab === 'tab1' ? 'active' : ''}`}>
//                         <img className='tab-icon' src={activeTab === 'tab1' ? icon1_a : icon1} alt='nope'></img>
//                         <span className='tab-title'>ПОЛУЧЕНИЕ ID</span>
//                     </button>
//                   </Link>

//                   <Link to="/academic-performance">
//                     <button onClick={() => handleTabClick('tab2')} className={`tab-btn ${activeTab === 'tab2' ? 'active' : ''}`}> 
//                         <img className='tab-icon' src={activeTab === 'tab2' ? icon2_a : icon2} alt='nope'></img>
//                         <span className='tab-title'>УСПЕВАЕМОСТЬ</span>
//                     </button>
//                   </Link>
                    
//                   <Link to="/notifications">
//                     <button onClick={() => handleTabClick('tab3')} className={`tab-btn ${activeTab === 'tab3' ? 'active' : ''}`}> 
//                         <img className='tab-icon' src={activeTab === 'tab3' ? icon3_a : icon3} alt='nope'></img>
//                         <span className='tab-title'>УВЕДОМЛЕНИЯ</span>
//                     </button>
//                   </Link>
                  
//                   <Link to="/about-me">
//                     <button onClick={() => handleTabClick('tab4')} className={`tab-btn ${activeTab === 'tab4' ? 'active' : ''}`}> 
//                         <img className='tab-icon' src={activeTab === 'tab4' ? icon4_a : icon4} alt='nope'></img>
//                         <span className='tab-title'>О СЕБЕ</span>
//                     </button>
//                   </Link>
//                 </div>
//               </div>
//               <button className="exit-btn" onClick={() => handleExitClick()}>ВЫЙТИ</button>
//             </div>
//           </div>
//         </div>
//       </>
//     )
//   } else {
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
                <AccountLabel name={name} role={role}/>
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
              <button className="exit-btn" onClick={() => handleExitClick()}>ВЫЙТИ</button>
            </div>
          </div>
        </div>
      </>
    )
  }
// }











// function App() {
  const [username, setUsername] = useState("")
  const [password, setPassword] = useState("")
  const [currentUser, setCurrentUser] = useState()
  const [profileData, setProfileData] = useState(null)
  const [subjectsData, setSubjectsData] = useState(null)

  useEffect(() => {
    const getProfile = async () => { 
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
    getProfile()
  }, [])

//   const submitLogin = async (e) => {
//     e.preventDefault();
//     try {
//       const res = await axios.post(
//         "http://localhost:8000/api/login/",
//         {
//           login: username,
//           password: password,
//         },
//         { withCredentials: true }
//       )
//       setCurrentUser(true)
//     } catch (error) {
//       console.log(error)
//     }
//   }

//   const submitLogout = async (e) => {
//     e.preventDefault();
//     try {
//       const csrftoken = Cookies.get('csrftoken')
//       const res = await axios.post(
//          "http://localhost:8000/api/logout/",
//          null, 
//          { 
//           withCredentials: true,  
//           headers: {
//               'X-CSRFToken': csrftoken  
//           }
//         }
//       )
//       setCurrentUser(false)
//       Cookies.remove('sessionid')
//     } catch (error) {
//       console.log(error)
//     }
//   }

//   if (currentUser) {
//     return (
//     <div className="App">
//       <form onSubmit={submitLogout}>
//         <div>
//           <label>{profileData.profile.last_name.toUpperCase()} {profileData.profile.first_name[0]}. {profileData.profile.surname[0]}.</label>
//           <p>{profileData.profile.role === 'Student' ? 'СТУДЕНТ' : 'ПРЕПОДАВАТЕЛЬ'} </p> 
//           <p>Telegram: <b>{profileData.profile.telegram === 'No' ? 'не привязан' : 'привязан'}</b> </p> 
//         </div>
//         <input type="submit" value="Выйти" />
//       </form>
//     </div>
//     )
//   }
//   return (
//     <div className="App">
//       <form onSubmit={submitLogin}>
//         <div>
//           <label>Логин</label>
//           <input
//             type="text"
//             placeholder="Логин"
//             value={username}
//             onChange={(e) => {
//               setUsername(e.target.value)
//             }}
//           />
//         </div>
//         <div>
//           <label>Пароль</label>
//           <input
//             type="password"
//             placeholder="Введите пароль"
//             value={password}
//             onChange={(e) => {
//               setPassword(e.target.value)
//             }}
//           />
//         </div>
//         <input type="submit" value="Войти" />
//       </form>
//     </div>
//   )
// }

// export default App







import axios from "axios";
import { useEffect, useState } from "react";
import Cookies from 'js-cookie';
import StudentApp from "./StudentApp";
import TeacherApp from "./TeacherApp";

function App() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [currentUser, setCurrentUser] = useState(false);
  const [role, setRole] = useState(null);
  const [profileData, setProfileData] = useState(null);

  useEffect(() => {
    const getProfile = async () => {
      try {
        const res = await axios.get(
          "http://localhost:8000/api/profile",
          { withCredentials: true }
        );

        if (res.status === 200) {
          setCurrentUser(true);
          setProfileData(res.data);
          setRole(res.data.role); // Предполагается, что в ответе есть поле role
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

  // Условный рендеринг: если пользователь авторизован и установлена роль, отображаем соответствующий компонент
  if (currentUser && role) {
    // return role === 'Student' ? <StudentApp /> : <TeacherApp />;
    return <TeacherApp />;
  }

  return (
    <div className="App">
      <form onSubmit={submitLogin}>
        <div>
          <label>Логин</label>
          <input
            type="text"
            placeholder="Логин"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
        </div>
        <div>
          <label>Пароль</label>
          <input
            type="password"
            placeholder="Введите пароль"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>
        <input type="submit" value="Войти" />
      </form>
    </div>
  );
}

export default App;
