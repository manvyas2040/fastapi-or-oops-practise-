import { useState } from "react";
import { createStudent } from "../api/api";

export default function Students() {
  const [name, setName] = useState("");
  const [roll, setRoll] = useState("");
  const [busId, setBusId] = useState("");

  const handleCreate = async () => {
    await createStudent({
      name,
      roll,
      bus_id: busId ? Number(busId) : null
    });
    alert("Student added");
  };

  return (
    <div>
      <h3>Add Student</h3>
      <input placeholder="Name" onChange={e => setName(e.target.value)} />
      <input placeholder="Roll" onChange={e => setRoll(e.target.value)} />
      <input placeholder="Bus ID (optional)" onChange={e => setBusId(e.target.value)} />
      <button onClick={handleCreate}>Add Student</button>
    </div>
  );
}
