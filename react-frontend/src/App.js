import { useEffect, useState } from 'react';
import './App.scss';
import apiCalls from './apiCalls';
import data from './mockData';

function App() {
  const [message, setMessage] = useState('');

  useEffect(() => {
    async function fetchData() {
      try {
        const response = await apiCalls.getTest();
        setMessage(response.data.message);
        console.log(response);
      } catch (error) {
        console.error(error);
      }
    }
    fetchData();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <p>message here: {message}</p>
        <table className="table">
          <thead>
            <tr>
              <th>Name</th>
              <th>Games Played</th>
              <th>Goals</th>
              <th>Assists</th>
              <th>Points</th>
              <th>+/-</th>
              <th>PIM</th>
              <th>Shots</th>
              <th>Shooting %</th>
              <th>PP Goals</th>
              <th>PP Points</th>
              <th>SH Goals</th>
              <th>GWG</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>{data.data[0].skaterFullName}</td>
              <td>{data.data[0].gamesPlayed}</td>
              <td>{data.data[0].goals}</td>
              <td>{data.data[0].assists}</td>
              <td>{data.data[0].points}</td>
              <td>{data.data[0].plusMinus}</td>
              <td>{data.data[0].penaltyMinutes}</td>
              <td>{data.data[0].shots}</td>
              <td>{data.data[0].shootingPct}</td>
              <td>{data.data[0].ppGoals}</td>
              <td>{data.data[0].ppPoints}</td>
              <td>{data.data[0].shGoals}</td>
              <td>{data.data[0].gameWinningGoals}</td>
            </tr>
          </tbody>
        </table>
      </header>
    </div>
  );
}

export default App;
