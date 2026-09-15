// A POST request sends data to a server. Unlike GET (which only reads), POST creates or updates a resource. 
// In JavaScript, you pass a second argument to fetch() with method: 
// "POST", a body containing the JSON string, and headers declaring the content type.

// Simulated POST: mirrors fetch with method + body + headers
const simulatedPost = async (endpoint, payload) => {
  console.log(`POST ${endpoint}`);
  console.log("Payload sent:", JSON.stringify(payload, null, 2));
  // Server processes and responds
  const response = {
    success: true,
    memberId: Math.floor(Math.random() * 9000) + 1000,
    receivedAt: new Date().toISOString(),
    message: `Check-in for ${payload.name} recorded.`
  };
  return { ok: true, status: 201, json: async () => response };
};

// POST a daily check-in
const submitCheckIn = async (checkIn) => {
  try {
    const response = await simulatedPost("/api/checkin", checkIn);

    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const result = await response.json();

    console.log("\nServer response:");
    console.log(`  Success:   ${result.success}`);
    console.log(`  Member ID: ${result.memberId}`);
    console.log(`  Message:   ${result.message}`);
    console.log(`  Timestamp: ${result.receivedAt}`);
  } catch (err) {
    console.log("Error:", err.message);
  }
};

// What the fetch call looks like (VS Code)
/*
const response = await fetch("https://api.smp.com/checkin", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify(checkIn)
});
*/

// Submit a check-in
const todayCheckIn = {
  name:  "Brian Otieno",
  date:  "2026-07-15",
  sleep: 7.5,
  water: 9,
  steps: 11240
};

await submitCheckIn(todayCheckIn);
