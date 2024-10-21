import './otel-config'  // Atualize o caminho conforme necessário
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'

console.log('Inicializando aplicação...')

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)

console.log('Aplicação inicializada com sucesso.')
