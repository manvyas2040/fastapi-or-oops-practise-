import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

API.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export const loginDriver = (data) =>
  API.post("/driver/login", data);

export const createRoute = (data) =>
  API.post("/routes", data);

export const createBus = (data) =>
  API.post("/buses", data);

export const createStudent = (data) =>
  API.post("/students", data);

export const getGPS = (busId) =>
  API.get(`/gps/${busId}`);
