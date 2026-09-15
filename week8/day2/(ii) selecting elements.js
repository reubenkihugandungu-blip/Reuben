// document.querySelector(selector) returns the first element that matches a CSS selector. 
// document.querySelectorAll(selector) returns all matches as a NodeList. 
// These are the two methods you will use for almost everything.

// Selector	            Selects           	               Python equivalent
// #myId	     Element with id="myId"	                  dict lookup by unique key
// .myClass	     All elements with class="myClass"	      list filter by attribute
// p	         All paragraph elements	                  list filter by type
// div > span	 span elements directly inside a div	  nested dict access

// This page has a hidden element with id "d1target"
//let's select it, read it, then change it

const el = document.querySelector('#d1target');

console.log("Tag name:", el.tagName);
console.log("Text content:", el.textContent);
console.log("Class list:", [...el.classList].join(','));

// Change its content
el.textContent = "Updated by Javascript";
console.log("New content:", el.textContent);

// Select all elements with class "d1item"
const items = document.querySelectorAll('.d1item');
console.log("\nNumber of .d1item elements:", items.length);

// Loop and read each one
items.forEach((item, index) => {
  console.log(`Item ${index}: ${item.textContent}`);
});
