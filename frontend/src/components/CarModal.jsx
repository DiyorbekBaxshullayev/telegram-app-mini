const CarModal = ({ car, onClose, onOrder }) => {
    return (
      <div className="fixed top-0 left-0 w-full h-full bg-black bg-opacity-40 flex justify-center items-center">
        <div className="bg-white p-4 rounded-xl w-11/12 max-w-md">
          <img src={car.image} alt={car.name} className="w-full h-40 object-cover rounded" />
          <h2 className="text-xl font-bold mt-2">{car.name}</h2>
          <p>{car.brand} - {car.year}</p>
          <p className="mt-2">{car.description}</p>
          <p className="text-green-600 font-bold mt-2">Kunlik narx: ${car.daily_price}</p>
          <div className="flex justify-between mt-4">
            <button className="bg-gray-300 px-4 py-2 rounded" onClick={onClose}>Yopish</button>
            <button className="bg-blue-600 text-white px-4 py-2 rounded" onClick={onOrder}>Buyurtma</button>
          </div>
        </div>
      </div>
    );
  };
  
  export default CarModal;
  