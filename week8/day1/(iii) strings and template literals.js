// Definition
// A template literal is a string that uses backticks instead of quotes and can embed variables directly using ${variable}. 
// This is JavaScript's equivalent of Python's f-strings.

const name = "Kamau";
const sleep = 7.5;
const steps = 12340;
const goal = 10000;

// Template literal: backticks + ${}
const report = `Athlete: ${name}
Sleep:   ${sleep} hours
Steps:   ${steps.toLocaleString()} 
Goal:    ${goal.toLocaleString()}
Result:  ${steps >= goal ? "HIT" : "MISS"}`;
// toLocaleString() adds commas to large numbers
// if steps >= goal is true print, print "Hit" otherwise print "Miss"

console.log(report);

// String methods
const city = "  nairobi  ";
console.log("\nRaw city:", `"${city}"`);
console.log("Trimmed:", `"${city.trim()}"`);
console.log("Upper:", city.trim().toUpperCase());
console.log("Length:", city.trim().length);

// String includes and startsWith
const skill = "phone repair";
console.log("\nIncludes 'repair':", skill.includes("repair"));
console.log("Starts with 'phone':", skill.startsWith("phone"));
console.log("Replace:", skill.replace("phone", "laptop"));

