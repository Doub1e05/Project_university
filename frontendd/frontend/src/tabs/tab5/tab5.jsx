import React, { useState } from 'react';
import axios from 'axios';
import './tab5.css';
import Tip from '../../tips/tip';
import ModalCamera from './ModalCamera'; 

import copy_icon from '../../../src/assets/Source/Icon/qr.png';
import s_icon from '../../../src/assets/Source/Icon/search.png';

export default function Tab6() {
  const [searchQuery, setSearchQuery] = useState('');
  const [IdWork, id_work] = useState(7);
  const [response, setResponse] = useState(['', '', '']);
  const [error, setError] = useState('');
  const [showModal, setShowModal] = useState(false);

  const handleSearch = async () => {
    try {
      const query = parseInt(searchQuery.trim());

      const responseWorkStatuses = await axios.get(`http://127.0.0.1:8000/api/work-statuses/`);
      const responseWorks = await axios.get('http://127.0.0.1:8000/api/works');
      const responseThread = await axios.get('http://127.0.0.1:8000/api/threads');

      const filteredStudent = responseWorkStatuses.data.find(item => item.identifier === query);

      const idWork = filteredStudent.work.id;
      id_work(idWork);
      const filteredWorks = responseWorks.data.find(item => item.id === idWork);
      const nameWork = filteredWorks.work_name;
      const idThread = filteredWorks.thread;
      const filteredThread = responseThread.data.find(item => item.id === idThread);

      const Course = filteredThread.course;
      const fullname = filteredStudent.student.last_name + ' ' +  filteredStudent.student.first_name + ' ' + filteredStudent.student.surname;
  

      setResponse([fullname, Course, nameWork]);
    } catch (error) {
      console.error('Ошибка поиска:', error.message);
      setError(error.message || 'Ошибка поиска');
    }
  };

  const handleAccept = async () => {
    try {
      await axios.patch(`http://127.0.0.1:8000/api/work-statuses/${IdWork}`, {
        status: 'Accepted',
      });

      console.log('Принято');
    } catch (error) {
      console.error('Ошибка при принятии:', error.message);
    }
  };

  const handleReject = async () => {
    try {
      await axios.patch(`http://127.0.0.1:8000/api/work-statuses/${IdWork}`, {
        status: 'Rejected',
      });

      console.log('Отклонено');
    } catch (error) {
      console.error('Ошибка при отклонении:', error.message);
    }
  };

  return (
    <div className='tab-wrapper'>
      <div className='tab-l'>
        <form>
          <div className="input">
            <img src={s_icon} alt="" className="input-s-icon" />
            <input
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className='code-input'
            />
            <img src={copy_icon} alt="" className="input-c-icon" onClick={() => setShowModal(true)}/>
          </div>

          <button type="button" onClick={handleSearch} className='search-btn'>
            Поиск
          </button>
        </form>
        <div className='search-out'>
          ФИО: {response[0]} <br/> Курс: {response[1]} <br/> Работа: {response[2]} <br/>
        </div>
        <div className="btns">
          <button className='accept-btn' onClick={handleAccept}>
            ПРИНЯТЬ
          </button>
          <button className='reject-btn' onClick={handleReject}>
            ОТКЛОНИТЬ
          </button>
        </div>
      </div>
      <div className="tab-r">
        <Tip text="Предподавателям не нужны подсказки, они и так все знают )" />
      </div>
      <ModalCamera show={showModal} onClose={() => setShowModal(false)} />
    </div>
  );
}
