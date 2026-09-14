// An object is a collection of key-value pairs.
//  In JavaScript, objects use curly braces and are equivalent to Python dictionaries.
//  Keys are strings. Values can be any type, including other objects or arrays.

// SMP member object
const member = {
  name: "Wanjiku Muthoni",
  city: "Nairobi",
  protocol: "SMP Phase 2",
  weeksCompleted: 4,
  skills: ["copywriting", "social media"],
  stats: {
    avgSleep: 7.2,
    avgSteps: 9800,
    goalHitRate: 0.71
  }
};

// Access with dot notation
console.log("Name:", member.name);
console.log("City:", member.city);
console.log("Weeks done:", member.weeksCompleted);

// Access nested object
console.log("Avg sleep:", member.stats.avgSleep);
console.log("Goal hit rate:", `${(member.stats.goalHitRate * 100).toFixed(0)}%`);

// Access array inside object
console.log("Skills:", member.skills.join(", "));

// Add a new key
member.lastActive = "2026-07-14";
console.log("\nLast active:", member.lastActive);

// Destructure to pull out named keys
const { name, city, weeksCompleted } = member;
console.log(`\n${name} | ${city} | Week ${weeksCompleted}`);

// Object.keys and Object.entries
console.log("\nTop-level keys:", Object.keys(member));
