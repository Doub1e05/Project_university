import React, { useState } from 'react';
import './tab3.css'
import Tip from '../../tips/tip';

export default function Tab3() {
  const handleClick = () => {
    const connect = true;

    return connect;
  };

  return (
    <div className='tab-wrapper'>
      <div className='tab-l'>
        <button className='tg-btn' onClick={handleClick}>Привязать к Telegram</button>

        <div className='tg-status'>Статус: <b>{handleClick() ? 'привязанно' : 'не привязанно'}</b></div>
      </div>
      <div className="tab-r">
      <Tip text="Для того, чтобы получать уведомления, нужно привязать свой аккаунт в Telegram или Вконтакте к специальному боту, который будет сообщать вам о проверенности лабораторных работ." />
      </div>
    </div>
  )
}
