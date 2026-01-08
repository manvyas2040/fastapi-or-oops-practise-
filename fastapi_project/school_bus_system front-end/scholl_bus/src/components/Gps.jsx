import { useState } from "react";
import { getGPS } from "../api/api";

export default function GPS() {
  const [busId, setBusId] = useState("");
  const [gps, setGps] = useState(null);

  const fetchGPS = async () => {
    const res = await getGPS(busId);
    setGps(res.data);
  };

  return (
    <div>
      <h3>GPS Info</h3>
      <input placeholder="Bus ID" onChange={e => setBusId(e.target.value)} />
      <button onClick={fetchGPS}>Get GPS</button>

      {gps && (
        <p>
          Lat: {gps.latitude}, Lng: {gps.longitude}
        </p>
      )}
    </div>
  );
}
