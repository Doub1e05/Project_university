import axios from "axios"
import { useEffect, useState } from "react"
import "./App.css"
import Cookies from 'js-cookie'

function App() {
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
      )
      setCurrentUser(true)
    } catch (error) {
      console.log(error)
    }
  }

  const submitLogout = async (e) => {
    e.preventDefault();
    try {
      const csrftoken = Cookies.get('csrftoken')
      const res = await axios.post(
         "http://localhost:8000/api/logout/",
         null, 
         { 
          withCredentials: true,  
          headers: {
              'X-CSRFToken': csrftoken  
          }
        }
      )
      setCurrentUser(false)
      Cookies.remove('sessionid')
    } catch (error) {
      console.log(error)
    }
  }

  if (currentUser) {
    return (
    <div className="App">
      <form onSubmit={submitLogout}>
        <div>
          <label>{profileData.profile.last_name.toUpperCase()} {profileData.profile.first_name[0]}. {profileData.profile.surname[0]}.</label>
          <p>{profileData.profile.role === 'Student' ? 'СТУДЕНТ' : 'ПРЕПОДАВАТЕЛЬ'} </p> 
          <p>Telegram: <b>{profileData.profile.telegram === 'No' ? 'не привязан' : 'привязан'}</b> </p> 
        </div>
        <input type="submit" value="Выйти" />
      </form>
    </div>
    )
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
            onChange={(e) => {
              setUsername(e.target.value)
            }}
          />
        </div>
        <div>
          <label>Пароль</label>
          <input
            type="password"
            placeholder="Введите пароль"
            value={password}
            onChange={(e) => {
              setPassword(e.target.value)
            }}
          />
        </div>
        <input type="submit" value="Войти" />
      </form>
    </div>
  )
}

export default App
