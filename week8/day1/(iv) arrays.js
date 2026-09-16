// An array is an ordered list of values. In JavaScript, arrays use square brackets and are equivalent to Python lists. 
// Items are accessed by index starting at zero.

// SMP skills list
const skills = ["welding", "tiling", "copywriting", "phone repair", "beekeeping"];

console.log("Skills:", skills);
console.log("First:", skills[0]);
console.log("Last:", skills[skills.length - 1]);
console.log("Count:", skills.length);

// Add and remove items
skills.push("plumbing");          // add to end
const removed = skills.shift();  // remove from front
console.log("\nAfter push + shift:", skills);
console.log("Removed:", removed);

// Array methods that return new arrays
const stepLog = [8200, 11400, 6300, 10050, 9800, 12100, 7500];

const hitDays = stepLog.filter(s => s >= 10000); // creates a new array containing only step counts that are atleast 10,000
const doubled = stepLog.map(s => s * 2);
const total   = stepLog.reduce((sum, s) => sum + s, 0); // adds all values in steplog, 0 is the starting total
const average = total / stepLog.length;
const sorted = [...stepLog].sort((a, b) => b - a);
// ☝️ copies steplog using the spread operator, them sorts the copy from largest to smallest. 
// the original array is unchanged.

console.log("\nStep log:", stepLog);
console.log("Hit days (>=10k):", hitDays);
console.log("Total steps:", total.toLocaleString());
console.log("Average:", Math.round(average).toLocaleString()); // rounds the average to the nearest whole number and formats it with commas
console.log("Sorted descending:", sorted); // prints the sorted step counts from highest to lowest

// Check membership
console.log("\nIncludes 6300:", stepLog.includes(6300)); // checks whether 6300 exists in steplog
console.log("Index of 9800:", stepLog.indexOf(9800));

// Try This:
// Add const sorted = [...stepLog].sort((a, b) => b - a); to the code and log it.
//  The spread operator ... creates a copy so the original stays unchanged. 
// Sort in JavaScript requires a compare function for numbers because the default sort is alphabetical.

