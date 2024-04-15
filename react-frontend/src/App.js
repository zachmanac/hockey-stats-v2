import { useEffect, useState } from 'react';
import './App.scss';
import apiCalls from './apiCalls';
import DataTable from './components/DataTable';
import { createClient } from "@supabase/supabase-js";

const supabase = createClient("https://gwqnevtnmqmlqwgyvtqb.supabase.co", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imd3cW5ldnRubXFtbHF3Z3l2dHFiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTEzMzgxNzksImV4cCI6MjAyNjkxNDE3OX0.4rcu3MU6w258JYbjcX2PvtIcVd8xIAmOekJoDeyBYZQ");

function App() {
  const [message, setMessage] = useState('');
  const [players, setPlayers] = useState([]);

  useEffect(() => {
    async function fetchDataFromFastAPI() {
      try {
        const response = await apiCalls.getTest();
        setMessage(response.data.message);
      } catch (error) {
        console.error(error);
      }
    }
    fetchDataFromFastAPI();
  }, []);

  useEffect(() => {
    getPlayers();
  }, []);

  async function getPlayers() {
    // const { data, error } = await supabase.rpc('get_player_stats_for_season_20222023');
    const { data, error } = await supabase.rpc('get_predicted_stats_with_names');

    if(error) {
      console.error("Error fetching players:", error);
      return;
    }

    const flattenedData = data.map(player => {
      const { player_stats, ...rest } = player;
      return { ...rest, ...player_stats };
    });

    setPlayers(flattenedData);
  }

  return (
    <div className="App">
      <header className="App-header">
        <p>message here: {message}</p>
      </header>
      <DataTable players={players} />
    </div>
  );
}

export default App;
