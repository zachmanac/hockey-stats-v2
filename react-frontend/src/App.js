import { useEffect, useState } from 'react';
import './App.scss';
import apiCalls from './apiCalls';
import data from './mockData';
import DataTable from './components/DataTable';
import { createClient } from "@supabase/supabase-js";

const supabase = createClient("https://gwqnevtnmqmlqwgyvtqb.supabase.co", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imd3cW5ldnRubXFtbHF3Z3l2dHFiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTEzMzgxNzksImV4cCI6MjAyNjkxNDE3OX0.4rcu3MU6w258JYbjcX2PvtIcVd8xIAmOekJoDeyBYZQ");

function App() {
  const [message, setMessage] = useState('');
  const [players, setPlayers] = useState([]);

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

  useEffect(() => {
    getPlayers();
  }, []);

  async function getPlayers() {
    const { data } = await supabase.from("players").select();
    setPlayers(data);
  }

  return (
    <div className="App">
      <header className="App-header">
        <p>message here: {message}</p>
        <ul>
          {players.map((player) => (
            <li key={player.name}>{player.name}</li>
          ))}
        </ul>
      </header>
      <DataTable />
    </div>
  );
}

export default App;
