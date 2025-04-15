import { useState } from 'react';

const OrderModal = ({ carId, onClose, onSubmit }) => {
  const [form, setForm] = useState({
    name: '',
    phone: '',
    passport: '',
    car: carId
  });

  const handleChange = (e) => setForm({ ...form, [e.target.name]: e.target.value });

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center">
      <div className="bg-white p-4 rounded-xl w-11/12 max-w-md">
        <h2 className="text-xl font-bold mb-4">Buyurtma qilish</h2>
        <input name="name" value={form.name} onChange={handleChange} placeholder="Ism" className="w-full mb-2 p-2 border rounded" />
        <input name="phone" value={form.phone} onChange={handleChange} placeholder="Telefon" className="w-full mb-2 p-2 border rounded" />
        <input name="passport" value={form.passport} onChange={handleChange} placeholder="Pasport ma'lumotlari" className="w-full mb-4 p-2 border rounded" />
        <div className="flex justify-between">
          <button onClick={onClose} className="bg-gray-300 px-4 py-2 rounded">Bekor</button>
          <button onClick={() => onSubmit(form)} className="bg-green-600 text-white px-4 py-2 rounded">Yuborish</button>
        </div>
      </div>
    </div>
  );
};

export default OrderModal;
