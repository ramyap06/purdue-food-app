import { Link } from 'react-router-dom';

export default function FoodItem({ name, carbCount, fatCount, proteinCount }) {
  return (
    <button className="w-full text-left rounded-2xl border border-gray-200 bg-white p-4 shadow-sm hover:shadow-md">
      <h2 className="text-lg font-semibold">{name}</h2>
      <p>Carbs: {carbCount}g</p>
      <p>Fat: {fatCount}g</p>
      <p>Protein: {proteinCount}g</p>
    </button>
  );
}