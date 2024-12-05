import React, { useState } from "react";
import PortFlowLogo from "../public/PortFlex.png";
import "./navigation.css";
import { useContext } from "react";
import { UserContext } from "../contexts/UserContext";
const Navigation = () => {
  const { user, loading, login, logout } = useContext(UserContext);
  const [dropdown, setDropdown] = useState(false);
  const dropdownToggle = () => {
    setDropdown(!dropdown);
  };
  if (loading) return <p>Ładowanie...</p>;

  return (
    <nav>
      <img
        src={PortFlowLogo}
        alt="PortFlow's logo"
        className="PortFlowLogo-nav"
      ></img>
      <div className="nav-options">
        <button>Opcja 1</button>
        <button>Opcja 2</button>
        <button>Opcja 3</button>
        {user ? (
          <div className="login-user-nav">
            <img
              onClick={dropdownToggle}
              src={user.avatar_url}
              alt={user.name}
              className="avatar-nav"
            />
            {dropdown && (
              <div className="dropdown-nav">
                <button>Profil</button>
                <button onClick={logout}>Wyloguj się</button>
              </div>
            )}
          </div>
        ) : (
          <button onClick={login}>Zaloguj się</button>
        )}
      </div>
    </nav>
  );
};

export default Navigation;
