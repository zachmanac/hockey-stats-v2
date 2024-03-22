import axios from 'axios';

async function getTest() {
  try {
    const response = await axios.get('http://localhost:8000');
    console.log(response);
    return response;
  } catch (error) {
    console.error(error);
  }
}

const apiCalls = {
  getTest
}

export default apiCalls;