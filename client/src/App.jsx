import React from 'react';
import './App.css';
import { Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Lawson from './pages/Lawson';
import Wiley from './pages/Wiley';
import Windsor from './pages/Windsor';

export default function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/lawson" element={<Lawson />} />
        <Route path="/wiley" element={<Wiley />} />
        <Route path="/windsor" element={<Windsor />} />
      </Routes>
    </div>
  );
}