import { createContext, useState, useEffect } from "react";
import axios from "axios";

export const UserContext = createContext();

export const UserProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  // Funkcja do logowania
  const login = () => {
    window.location.href = "http://127.0.0.1:8000/login";
  };

  // Funkcja do wylogowania
  const logout = async () => {
    try {
      await axios.get("http://127.0.0.1:8000/logout", {
        withCredentials: true,
      });
      setUser(null); // Resetuje stan użytkownika
    } catch (error) {
      console.error("Błąd podczas wylogowywania:", error);
    }
  };

  // Pobieranie danych użytkownika podczas inicjalizacji
  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/user", { withCredentials: true })
      .then((response) => {
        setUser(response.data.user);
      })
      .catch(() => {
        setUser(null);
      })
      .finally(() => {
        setLoading(false);
      });
  }, []);

  return (
    <UserContext.Provider value={{ user, setUser, loading, login, logout }}>
      {children}
    </UserContext.Provider>
  );
};
