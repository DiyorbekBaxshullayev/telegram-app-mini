import { useEffect, useState } from 'react';
import { getCars, createOrder } from '../api';
import CarCard from '../components/CarCard';
import CarModal from '../components/CarModal';
import OrderModal from '../components/OrderModal';

const Home = () => {
  const [cars, setCars] = useState([]);
  const [selectedCar, setSelectedCar] = useState(null);
  const [orderOpen, setOrderOpen] = useState(false);

  useEffect(() => {
    getCars().then(res => setCars(res.data));
  }, []);

  const handleOrder = (data) => {
    createOrder(data).then(() => {
      setOrderOpen(false);
      setSelectedCar(null);
      alert("Buyurtma yuborildi!");
    });
  };

  return (
    <div className="p-4">
      {cars.map(car => (
        <CarCard key={car.id} car={car} onClick={() => setSelectedCar(car)} />
      ))}
      {selectedCar && <CarModal car={selectedCar} onClose={() => setSelectedCar(null)} onOrder={() => setOrderOpen(true)} />}
      {orderOpen && <OrderModal carId={selectedCar.id} onClose={() => setOrderOpen(false)} onSubmit={handleOrder} />}
    </div>
  );
};

export default Home;
