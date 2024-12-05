import { useState, useEffect } from "react";
import "./App.css";
import { useContext } from "react";
import { UserContext } from "../contexts/UserContext";

function App() {
  const { user, loading, login, logout } = useContext(UserContext);

  if (loading) return <p>Ładowanie...</p>;

  return (
    <div>
      <p className="read-the-docs">PortFlow💗</p>
      {!user ? (
        <button onClick={login}>Zaloguj się</button>
      ) : (
        <div className="flex flex-col items-center card">
          <img
            src={user.avatar_url}
            alt={`${user.name}'s avatar`}
            style={{ borderRadius: "50%", width: "100px", height: "100px" }}
          />
          <h2>Witaj, {user.name}!</h2>
          <button onClick={logout}>Wyloguj się</button>
        </div>
      )}
    </div>
  );
}

export default App;
