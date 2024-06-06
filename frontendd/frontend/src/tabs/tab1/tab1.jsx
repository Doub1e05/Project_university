import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './tab1.css';
import Tip from '../../tips/tip';

import lab_icon from '../../../src/assets/Source/Icon/free-icon-to-do-3311779.png';
import sub_icon from '../../../src/assets/Source/Icon/free-icon-clipboard-3311692.png';
import copy_icon from '../../../src/assets/Source/Icon/free-icon-multitask-3311722.png';

export default function Tab1() {
  const [selectedSubject, setSelectedSubject] = useState('');
  const [selectedLabWork, setSelectedLabWork] = useState('');
  const [code, setIdentifierValue] = useState('');
  const [subjectOptions, setSubjectOptions] = useState([]);
  const [selectedWorks, setSelectedWorks] = useState([]);
  const [selectedSubjectId, setSelectedSubjectId] = useState(null);

  useEffect(() => {
    const fetchSubjects = async () => {
      try {
        const worksResponse = await axios.get('http://127.0.0.1:8000/api/works');
        const subjectsResponse = await axios.get('http://127.0.0.1:8000/api/subjects');
        
        const filteredWorks = worksResponse.data.filter(work => work.thread === 1);
        const subjectIds = filteredWorks.map(work => work.subject);
        const filteredSubjects = subjectsResponse.data.filter(subject => subjectIds.includes(subject.id));
        setSubjectOptions(filteredSubjects);

        const defaultSubjectId = filteredSubjects[0]?.id;
        setSelectedSubjectId(defaultSubjectId);
      } catch (error) {
        console.error('Error fetching subjects:', error);
      }
    };

    fetchSubjects();
  }, []);

  useEffect(() => {
    const fetchWorks = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/works');
        const works = response.data.filter(work => work.thread === 1 && work.subject === selectedSubjectId);
        setSelectedWorks(works);
      } catch (error) {
        console.error('Error fetching works:', error);
      }
    };

    fetchWorks();
  }, [selectedSubjectId]);

  const handleCodeRequest = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/api/work-statuses/');
      const filteredItem = response.data.find(item => item.student.id === 1 && item.work.id === parseInt(selectedLabWork));
      const identifier = filteredItem ? filteredItem.identifier : 'Не найдено';
      setIdentifierValue(identifier);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  const idСopy = () => {
    navigator.clipboard.writeText(code)
      .then(() => {
        console.log('скопировано!');
      })
      .catch(err => {
        console.log('Something went wrong', err);
      });
  };

  return (
    <div className='tab-wrapper'>
      <div className='tab-l'>
        <div className="choice-title">
          Предмет
          <img src={sub_icon} alt="nope" className="choice-icon" />
        </div>
        <select className='choice-input' value={selectedSubject} onChange={(e) => {
          setSelectedSubject(e.target.value);
          setSelectedLabWork('');
        }}>
          <option value="">Выберите предмет</option>
          {subjectOptions.map((subject, index) => (
            <option key={index} value={subject.id}>
              {subject.subject_name}
            </option>
          ))}
        </select>

        <div className="choice-title">
          Лабораторная работа 
          <img src={lab_icon} alt="nope" className="choice-icon" />
        </div>
        <select className='choice-input' value={selectedLabWork} onChange={(e) => setSelectedLabWork(e.target.value)}>
          <option value="">Выберите лабораторную работу</option>
          {selectedWorks.map((work, index) => (
            <option key={index} value={work.id}>
              {work.work_name}
            </option>
          ))}
        </select>

        <button className='select-btn' onClick={handleCodeRequest}>Получить код</button>

        <div onClick={idСopy} className="code">
          <div className="id-splsh">ID</div>
          <div className="id-code">{code}</div>
          <img src={copy_icon} alt="nope" className="icon-copy" />
        </div>
        
      </div>
      <div className="tab-r">
        <Tip text="   Укажите учебный предмет и номер работы для получения ID. Идентификатор создан с целью упрощения проверки отчётов и экономии времени, а также для быстрого уведомления о том, что работа успешно проверена.  " />
      </div>
    </div>
  );
}
