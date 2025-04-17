// // import { useEffect, useState } from 'react';
// // import { getCars, createOrder } from '../api';
// // import CarCard from '../components/CarCard';
// // import CarModal from '../components/CarModal';
// // import OrderModal from '../components/OrderModal';

// // const Home = () => {
// //   const [cars, setCars] = useState([]);
// //   const [selectedCar, setSelectedCar] = useState(null);
// //   const [orderOpen, setOrderOpen] = useState(false);

// //   useEffect(() => {
// //     getCars().then(res => setCars(res.data));
// //   }, []);

// //   const handleOrder = (data) => {
// //     createOrder(data).then(() => {
// //       setOrderOpen(false);
// //       setSelectedCar(null);
// //       alert("Buyurtma yuborildi!");
// //     });
// //   };

// //   return (
// //     <div className="p-4">
// //       {cars.map(car => (
// //         <CarCard key={car.id} car={car} onClick={() => setSelectedCar(car)} />
// //       ))}
// //       {selectedCar && <CarModal car={selectedCar} onClose={() => setSelectedCar(null)} onOrder={() => setOrderOpen(true)} />}
// //       {orderOpen && <OrderModal carId={selectedCar.id} onClose={() => setOrderOpen(false)} onSubmit={handleOrder} />}
// //     </div>
// //   );
// // };

// // export default Home;

// // components/CarCard.jsx yoki Home.jsx
// import { useEffect, useState } from "react";

// function Home() {
//   const [cars, setCars] = useState([]);

//   useEffect(() => {
//     fetch("http://127.0.0.1:8000/api/cars/")
//       .then(res => res.json())
//       .then(data => setCars(data));
//   }, []);

//   return (
//     <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
//       {cars.map(car => (
//         <div key={car.id} className="border p-4 rounded shadow">
//           <h2 className="text-xl font-bold">{car.name}</h2>
//           <p>{car.description}</p>
//           <p><strong>Narx:</strong> {car.price} so'm/kun</p>
//         </div>
//       ))}
//     </div>
//   );
// }

// export default Home;


// Home.jsx
import { useEffect, useState } from "react";
import axios from "axios";
import CarCard from "../components/CarCard";

const Home = () => {
  const [cars, setCars] = useState([]);

  useEffect(() => {
    const fetchCars = async () => {
      try {
        const response = await axios.get(`${import.meta.env.VITE_API_URL}/cars/`);
        setCars(response.data);
      } catch (error) {
        console.error("Xatolik yuz berdi:", error);
      }
    };

    fetchCars();
  }, []);

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Mavjud mashinalar</h1>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {cars.map((car) => (
          <CarCard key={car.id} car={car} onClick={() => console.log("Batafsil: ", car.name)} />
        ))}
      </div>
    </div>
  );
};

export default Home;

