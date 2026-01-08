import { useState } from "react";
import { loginDriver } from "../api/api";

export default function Login({ onLogin }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleLogin = async () => {
    try {
      const res = await loginDriver({ username, password });
      localStorage.setItem("token", res.data.access_token);
      onLogin();
    } catch {
      setError("Invalid credentials");
    }
  };

  return (
    <div>
      <h2>Driver Login</h2>
      <input placeholder="Username" onChange={e => setUsername(e.target.value)} />
      <input type="password" placeholder="Password" onChange={e => setPassword(e.target.value)} />
      <button onClick={handleLogin}>Login</button>
      {error && <p style={{color:"red"}}>{error}</p>}
    </div>
  );
}
