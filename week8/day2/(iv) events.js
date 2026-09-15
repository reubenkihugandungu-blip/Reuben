// An event is a signal the browser sends when something happens: a click, a keystroke, a form submission, a page load.
// addEventListener(eventName, callbackFunction) registers a function to run when that event fires on a specific element.

// Wire up the buttons in the live demo below
const addBtn    = document.querySelector('#d3addBtn');
const clearBtn  = document.querySelector('#d3clearBtn');
const logInput  = document.querySelector('#d3input');
const logList   = document.querySelector('#d3list');
const countEl   = document.querySelector('#d3count');

let count = 0;

addBtn.addEventListener('click', () => {
  const value = logInput.value.trim();
  if (!value) {
    console.log("No input to add.");
    return;
  }

  // Create new list item
  const li = document.createElement('li');
  li.textContent = value;
  li.style.padding = "4px 0";
  li.style.borderBottom = "1px solid #30363d";
  logList.appendChild(li);

  count++;
  countEl.textContent = `Entries: ${count}`;
  logInput.value = "";
  logInput.focus();
  console.log(`Added: "${value}"`);
});

clearBtn.addEventListener('click', () => {
  logList.innerHTML = "";
  count = 0;
  countEl.textContent = "Entries: 0";
  console.log("Log cleared.");
});

// Keyboard shortcut: Enter key submits
logInput.addEventListener('keydown', (event) => {
  if (event.key === 'Enter') {
    addBtn.click();
  }
});

console.log("Event listeners attached. Use the panel below.");

// Try This:
// Run the code above, then type "11,240 steps - Day 37" in the input and press Enter.
//  Add three more entries.
//  Click Clear. Now modify the click listener to prepend the current date (use new Date().toLocaleDateString()) to each entry before adding it.