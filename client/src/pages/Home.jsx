import React from 'react';
import Navbar from '../components/Navbar';
import Header from '../components/Header';
import DiningHall from '../components/DiningHall';

export default function Home() {
    return (
        <div>
            <Navbar />
            <div className="bg-gradient-to-br from-gray-900 via-black to-gray-800 p-10">
            <Header />
            <ul className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 p-6">
                <DiningHall path="/lawson" dist={.05} hMeter={5}>Lawson</DiningHall>
                <DiningHall path="/wiley" dist={.05} hMeter={5}>Wiley</DiningHall>
                <DiningHall path="/windsor" dist={.05} hMeter={5}>Windsor</DiningHall>
            </ul>
            </div>
        </div>
    );
}