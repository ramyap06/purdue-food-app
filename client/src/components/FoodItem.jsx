export default function FoodItem({name, carbCount, fatCount, proteinCount}) {
    return (
        <h2>{name}</h2>
        <p>{carbCount}</p>
        <p>{fatCount}</p>
        <p>{proteinCount}</p>
    );
}