import './tip.css'
import { useState } from 'react';
import icon_info from '../assets/Source/Icon/free-icon-information-157933.png'
import icon_arrow from '../assets/Source/Icon/down-arrow.png'

export default function Tip(props) {
  const tip_content = props.text || '';
  const [show_tip, setShow] = useState(false);

  const handleTipClick = () => {
    setShow(!show_tip);
    console.log(show_tip);
  };

  return (
    <>
      <div onClick={() => handleTipClick(setShow)} className={`title-tip-info ${show_tip ? 'show-tip-title' : ''}`}>
        Информация
        <img className={`tip-icon tip-icon-arrow ${show_tip ? 'tip-icon-arrow-show' : ''}`} src={icon_arrow} alt='nope'></img>
        <img className='tip-icon tip-icon-info' src={icon_info} alt='nope'></img>
      </div>

      <div className={`tip-info ${show_tip ? 'show-tip' : ''}`}>{tip_content}</div>
    </>
  )
}