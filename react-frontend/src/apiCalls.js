import axios from 'axios';

const baseURL = 'http://localhost:8000/';

async function getTest() {
  try {
    const response = await axios.get(`${baseURL}`);
    return response;
  } catch (error) {
    console.error(error);
  }
}

const apiCalls = {
  getTest
}

export default apiCalls;