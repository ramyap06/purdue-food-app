import { useParams } from "react-router-dom";
import Navbar from '../components/Navbar';

export default function DiningHallPage() {
    const { hallName } = useParams();
      return (
        <div>
        <Navbar />
        <div className="p-6">
            <h1 className="text-3xl font-bold capitalize">{hallName} Dining Hall</h1>
            <p className="text-gray-600 mt-2">
            This page was dynamically generated for <b>{hallName}</b> — no hardcoding needed.
            </p>
        </div>
        </div>
    );
}