import { useEffect, useState } from 'react';
import './App.scss';
import apiCalls from './apiCalls';
import data from './mockData';
import DataTable from './components/DataTable';

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
      </header>
      <DataTable />
    </div>
  );
}

export default App;
