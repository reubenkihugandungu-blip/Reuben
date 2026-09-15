// Once you have a reference to an element, 
// you can change what it displays and how it looks using three main properties: textContent, innerHTML, and style.

// Property	                               What it does	                     When to use
// el.textContent = "x"	             Sets the visible text only      	When inserting plain text (safe)
// el.innerHTML = "<b>x</b>"	     Sets text including HTML tags	    When you need HTML formatting
// el.style.color = "red"	         Sets inline CSS on the element	    Dynamic style changes
// el.classList.add("active")	     Adds a CSS class	                Toggle states via pre-written CSS
// el.classList.remove("active")	 Removes a CSS class	            Toggle states via pre-written CSS

// Get the live display panel for this exercise
const panel = document.querySelector('#d2panel');

// Change text content
panel.textContent = "SMP Daily Report";
console.log("Set text:", panel.textContent);

// Change style properties
panel.style.color = "#4ecca3";
panel.style.fontWeight = "bold";
panel.style.padding = "8px";
panel.style.background = "#0a1628";
panel.style.borderRadius = "4px";
console.log("Styles applied");

// innerHTML adds HTML structure
panel.innerHTML = `
  <strong style="color:#f5a623;">Day 37</strong>
  | Steps: <span style="color:#4ecca3;">11,240</span>
  | Sleep: <span style="color:#a5d6ff;">7.5h</span>
  | Rating: <span style="color:#e94560;">Excellent</span>
`;
console.log("HTML injected into panel");

// Create a brand new element and append it
const newItem = document.createElement('p');
newItem.textContent = "Created by JavaScript at runtime";
newItem.style.color = "#8b949e";
newItem.style.fontSize = "0.85rem";
newItem.style.marginTop = "4px";
panel.appendChild(newItem);
console.log("New element appended");

// Tip:
//  Use textContent when inserting user-provided text.
//  It escapes HTML automatically, so a user who types <script>alert('x')</script> into a form cannot inject code. 
// Use innerHTML only for HTML you write yourself and fully control.
