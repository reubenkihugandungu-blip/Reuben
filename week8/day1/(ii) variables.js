// Definition

// const declares a variable that will not be reassigned. 
// let declares a variable that may be reassigned later. 
// Use const by default. Switch to let only when you know the value will change.

// Keyword	 Reassignable?     Use case
// const	     No	          Configuration, names, fixed data
// let	         Yes	      Counters, running totals, loop variables
// var	         Yes	      Old code only. Avoid in new code.

// Tip: 
// In Python, variable type is determined at runtime and can change freely. 
// In JavaScript, const and let do not restrict the type. 
// They only restrict whether the variable name can be pointed at a new value.
// A const array can still have items added to it.\

// const for fixed values
const athleteName = "Wanjiku";
const protocol = "SMP Phase 1";
const targetSteps = 10000;

// let for values that change
let dayNumber = 1;
let stepCount = 0;

console.log("Athlete:", athleteName);
console.log("Protocol:", protocol);
console.log("Target steps:", targetSteps);

// Reassign let variable
dayNumber = 7;
stepCount = 11240;

console.log("\nDay:", dayNumber);
console.log("Steps logged:", stepCount);
console.log("Hit goal:", stepCount >= targetSteps);

// typeof checks the data type
console.log("\nTypes:");
console.log("athleteName:", typeof athleteName);   // string
console.log("targetSteps:", typeof targetSteps);   // number
console.log("hit goal:",    typeof true);           // boolean

// Try this:
// Add a line that tries to reassign athleteName to a new value, for example athleteName = "Wanjiku". 
// Run it and read the error. This is what const enforces.