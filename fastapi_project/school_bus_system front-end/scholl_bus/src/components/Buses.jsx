import { useState } from "react";
import { createBus } from "../api/api";

export default function Buses() {
  const [number, setNumber] = useState("");
  const [routeId, setRouteId] = useState("");

  const handleCreate = async () => {
    await createBus({ number: Number(number), route_id: Number(routeId) });
    alert("Bus created");
  };

  return (
    <div>
      <h3>Create Bus</h3>
      <input placeholder="Bus Number" onChange={e => setNumber(e.target.value)} />
      <input placeholder="Route ID" onChange={e => setRouteId(e.target.value)} />
      <button onClick={handleCreate}>Add Bus</button>
    </div>
  );
}
