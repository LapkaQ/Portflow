import { Outlet, Link } from "react-router-dom";
import Navigation from "../components/Navigation";
const Layout = () => {
  return (
    <>
      <Navigation />
      <main>
        <Outlet />
      </main>
      footer
    </>
  );
};

export default Layout;
