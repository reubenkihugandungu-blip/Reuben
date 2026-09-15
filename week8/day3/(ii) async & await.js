// async marks a function as one that performs asynchronous work. 
// Inside an async function, await pauses that function until the Promise it is waiting for resolves.
// The rest of the page keeps running while the wait happens.

// BASIC FETCH PATTERN

// // The full pattern every fetch request follows
const fetchData = async () => {
  try {
    const response = await fetch("https://api.example.com/data");

    if (!response.ok) {
      throw new Error(`HTTP error: ${response.status}`);
    }

    const data = await response.json(); // parse JSON body
    console.log(data);

  } catch (err) {
    console.error("Fetch failed:", err.message);
  }
};

fetchData();

// 
// Step	                    What happens	                      Python equivalent
// fetch(url)	           Sends the HTTP request	              requests.get(url)
// await response	       Waits for HTTP headers to arrive       synchronous by default
// response.ok	           True if status is 200-299	          response.status_code == 200
// response.json()	       Parses the JSON body (async)	          response.json()
// try/catch	           Handles network errors	               try/except