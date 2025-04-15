const CarCard = ({ car, onClick }) => {
    return (
      <div className="bg-white shadow-md rounded-xl p-4 mb-4">
        <img src={car.image} alt={car.name} className="w-full h-48 object-cover rounded-xl" />
        <h2 className="text-xl font-bold">{car.name}</h2>
        <p>{car.brand} - {car.year}</p>
        <p className="text-green-600 font-semibold">Kunlik: ${car.daily_price}</p>
        <button
          className="mt-2 bg-blue-600 text-white px-4 py-2 rounded-xl"
          onClick={onClick}
        >
          Batafsil
        </button>
      </div>
    );
  };
  
  export default CarCard;
  