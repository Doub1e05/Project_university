import icon from '../assets/Source/Icon/free-icon-user-profile-2696783.png'
import './Account.css'

export default function AccountLabel(props) {
  const role = props.role
  const name = props.name

  return (
    <>
      <div className="acc-wrapper">
        <p className='acc-role'><b className='acc-name'>{name}</b><br />{role}</p>
        <img src={icon} alt="nope" className="acc-icon" />
      </div>
    </>
  )
}