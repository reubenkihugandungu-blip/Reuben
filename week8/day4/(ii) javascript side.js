// The browser sends fetch requests to the Python API. It does not know or care that Python is processing the request.
//  It only knows the URL, the HTTP method, and the JSON structure of the response.

const API_BASE = "http://localhost:8000";

// GET all check-ins from Python API
const loadCheckIns = async () => {
  const response = await fetch(`${API_BASE}/api/checkins`);
  if (!response.ok) throw new Error(`HTTP ${response.status}`);
  return await response.json();
};

// POST a new check-in to Python API
const submitCheckIn = async (payload) => {
  const response = await fetch(`${API_BASE}/api/checkins`, {
    method:  "POST",
    headers: { "Content-Type": "application/json" },
    body:    JSON.stringify(payload)
  });
  if (!response.ok) throw new Error(`HTTP ${response.status}`);
  return await response.json();
};