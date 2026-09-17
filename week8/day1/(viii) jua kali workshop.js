// Arrays, objects, loops, and template literals are not tied to fitness data. 
// The same code structure works for a Jua Kali metalwork shop tracking completed jobs. The syntax is identical.

// 👇creates a constant array called jobs. It will contain completed jobs
const workshop = {
  name: "Kamau Metalworks",
  town: "Gikomba, Nairobi",
  craftsman: "Joseph Kamau"
};

const jobs = [
  { type: "Sliding gate",  materials_kes: 18000, labour_kes: 8000, paid: true  },
  { type: "Window grills", materials_kes:  6500, labour_kes: 4500, paid: true  },
  { type: "Door frame",    materials_kes:  4200, labour_kes: 2800, paid: false },
  { type: "Roof sheet",    materials_kes:  9800, labour_kes: 3200, paid: true  },
  { type: "Security door", materials_kes: 12000, labour_kes: 7000, paid: false },
];

const totalRevenue = jobs
  .filter(j => j.paid) // is an arrow function that keeps only jobs where paid is true
  .reduce((sum, j) => sum + j.materials_kes + j.labour_kes, 0);
  // ☝️adds together the material and labour costs for every paid job
  // 0 is the starting value

// 👇 !j.paid means "the job is not paid"
// .length counts how many matching jobs exists
const unpaidCount = jobs.filter(j => !j.paid).length;

//👇 prints the workshop name and town
// ${...} inserts JS values into a template string

console.log(`Workshop: ${workshop.name} | ${workshop.town}`);
console.log(`Craftsman: ${workshop.craftsman}`);
console.log(`Jobs completed: ${jobs.length}`);
console.log(`Revenue collected: KES ${totalRevenue.toLocaleString()}`); // tolocalestring, put commas
console.log(`Unpaid jobs: ${unpaidCount}`);
console.log("\nJob breakdown:");

// 👇 Uses a ternary operator
// job.paid is true, status becomes PAID , otherwise becomes UNPAID

for (const job of jobs) {
  const total = job.materials_kes + job.labour_kes;
  const status = job.paid ? "PAID" : "UNPAID";
  console.log(`  ${job.type} | KES ${total.toLocaleString()} | ${status}`);
}
