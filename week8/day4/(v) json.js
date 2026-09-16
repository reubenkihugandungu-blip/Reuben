// json.stringify and json.parse

// JavaScript object (lives in memory)
const checkIn = {
  name:     "Aisha Waweru",
  sleep:    7.8,
  water:    10,
  steps:    11400,
  hit_goal: true
};

// Convert to JSON string (what the browser sends over the wire)
const jsonString = JSON.stringify(checkIn);
console.log("Type after stringify:", typeof jsonString);
console.log("JSON string:", jsonString);

// Pretty-print (2-space indent)
console.log("\nPretty JSON:");
console.log(JSON.stringify(checkIn, null, 2));

// Convert back to object (what the browser receives and parses)
const parsed = JSON.parse(jsonString);
console.log("\nType after parse:", typeof parsed);
console.log("Name:", parsed.name);
console.log("Hit goal:", parsed.hit_goal);

// What happens with invalid JSON
try {
  JSON.parse("{bad json}");
} catch (err) {
  console.log("\nParse error caught:", err.message.slice(0, 50));
}

// Arrays serialize and parse correctly too
const log = [{ day: 1, steps: 9800 }, { day: 2, steps: 11200 }];
const logJson = JSON.stringify(log);
const logBack = JSON.parse(logJson);
console.log("\nArray round-trip:", logBack[1].steps);
