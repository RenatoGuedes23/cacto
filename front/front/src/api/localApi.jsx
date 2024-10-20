import axios from 'axios';

const isServer = typeof window === 'undefined';

const axiosInstance = axios.create({
  ...(isServer && {
    httpsAgent: new (require('https')).Agent({  
      rejectUnauthorized: true
    }),
  }),
  headers: { 
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'POST,GET,OPTIONS,DELETE',
    'Access-Control-Allow-Credentials': false,
  }
});

export default axiosInstance;
