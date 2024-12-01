import { useState, useEffect } from "react";
import "./App.css";
import axios from "axios";

function App() {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/user", { withCredentials: true })

      .then((response) => {
        console.log("Dane użytkownika:", response.data);
        setUser(response.data.user);
      })
      .catch((error) => {
        console.error("Błąd podczas pobierania użytkownika:", error);
        setUser(null);
      })
      .finally(() => {
        setLoading(false);
      });
  }, []);

  const handleLogin = () => {
    console.log("Przekierowanie do logowania");
    window.location.href = "http://127.0.0.1:8000/login";
  };

  const handleLogout = () => {
    axios
      .get("http://127.0.0.1:8000/logout", { withCredentials: true })
      .then(() => {
        setUser(null);
      })
      .catch((error) => {
        console.error("Logout failed", error);
      });
  };

  if (loading) return <p>Loading...</p>;

  return (
    <div>
      <p className="read-the-docs">pf</p>
      {!user ? (
        <>
          <button onClick={handleLogin}>Zaloguj się</button>
          <button onClick={handleLogout}>Wyloguj się</button>
        </>
      ) : (
        <div>
          <img
            src={user.avatar_url}
            alt={`${user.name}'s avatar`}
            style={{ borderRadius: "50%", width: "100px", height: "100px" }}
          />
          <h2>Witaj, {user.name}!</h2>
          <p>Email: {user.email}</p>
          <button onClick={handleLogout}>Wyloguj się</button>
        </div>
      )}
    </div>
  );
}

export default App;
