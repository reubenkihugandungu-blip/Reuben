// A function is a reusable block of code. 
// JavaScript has two common ways to write functions: function declarations and arrow functions.
// Arrow functions are shorter and are standard in modern JavaScript.

// Arrow function with default parameter
const assessDay = (steps, goal = 10000) => {
  if (steps >= goal) return "HIT";
  return "MISS";
};

// Function returning an object
const analyzeDay = (sleep, water, steps) => {
  const hitGoal = steps >= 10000;
  let rating;
  if (sleep >= 7.5 && water >= 8 && hitGoal) 
    {rating = "Excellent";}
  else if (hitGoal)
    {rating = "Good";}
  else if (sleep >= 7.0) 
    {rating = "Average";}
  else 
    {rating = "Below target";}
  return { sleep, water, steps, hitGoal, rating };
};

// Test with SMP data
const days = [
  [8.0, 10, 12100],
  [5.5,  4,  7800],
  [7.2,  8, 10050],
  [6.0,  5,  9200],
];

days.forEach(([sleep, water, steps]) => {
  const result = analyzeDay(sleep, water, steps);
  console.log(`Sleep:${result.sleep}h  Water:${result.water}gl  
    Steps:${result.steps.toLocaleString()}  --> ${result.rating}`);
});

// for...of loop
console.log("\nGoal assessments:");
const stepLog = [9800, 11400, 6300, 10050];
for (const steps of stepLog) {
  console.log(`  ${steps.toLocaleString()} --> ${assessDay(steps)}`);
}

// Add a function called weekSummary that takes an array of step counts and returns an object with total, average, and hitCount. 
// Call it on the stepLog array and log the result.