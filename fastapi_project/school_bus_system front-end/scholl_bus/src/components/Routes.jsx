import { useState } from "react";
import { createRoute } from "../api/api";

export default function Routes() {
  const [name, setName] = useState("");
  const [msg, setMsg] = useState("");

  const handleCreate = async () => {
    try {
      await createRoute({ name });
      setMsg("Route created");
    } catch {
      setMsg("Route already exists");
    }
  };

  return (
    <div>
      <h3>Create Route</h3>
      <input placeholder="Route Name" onChange={e => setName(e.target.value)} />
      <button onClick={handleCreate}>Add</button>
      <p>{msg}</p>
    </div>
  );
}
