import { Outlet, Link } from "react-router-dom";
const Layout = () => {
  return (
    <>
      nav
      <main>
        <Outlet />
      </main>
    </>
  );
};

export default Layout;
