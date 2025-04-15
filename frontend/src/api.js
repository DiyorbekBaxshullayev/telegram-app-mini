import axios from "axios";

const API_BASE = "http://localhost:8000/api"; // Django backend URL

export const getCars = () => axios.get(`${API_BASE}/cars/`);
export const getCarDetail = (id) => axios.get(`${API_BASE}/cars/${id}/`);
export const createOrder = (data) => axios.post(`${API_BASE}/orders/`, data);
