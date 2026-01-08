import { useState } from "react";
import Login from "./components/Login";
import Routes from "./components/Routes";
import Buses from "./components/Buses";
import Students from "./components/Students";
import Gps from "./components/Gps";

function App() {
  const [loggedIn, setLoggedIn] = useState(!!localStorage.getItem("token"));

  if (!loggedIn) {
    return <Login onLogin={() => setLoggedIn(true)} />;
  }

  return (
    <div>
      <h1>School Bus Management</h1>
      <Routes />
      <Buses />
      <Students />
      <Gps />
    </div>
  );
}

export default App;
