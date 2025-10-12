import React from 'react';
import './App.css';
import Header from './components/Header';
import DiningHall from './components/DiningHall';

function App() {
  return (
    <div className="bg-gradient-to-br from-gray-900 via-black to-gray-800 min-h-screen p-10">
      <Header />
      <ul className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 p-6">
        <DiningHall dist={.05} hMeter={5}>Lawson</DiningHall>
        <DiningHall dist={.05} hMeter={5}>Wiley</DiningHall>
        <DiningHall dist={.05} hMeter={5}>Windsor</DiningHall>
      </ul>
    </div>
  );
}

export default App
