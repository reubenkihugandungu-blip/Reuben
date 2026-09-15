// Tip: fetch() only rejects the Promise on network failure (no connection, DNS error).
//  A 404 or 500 response does NOT throw an error. That is why you must always check response.ok manually.
//  If you skip this check, a 500 error from the server will silently pass through your success code.

// Wrong: no response.ok check
const response = await fetch(url);
const data = await response.json(); // works even on 500 error

// Correct: always check response.ok first
const response = await fetch(url);
if (!response.ok) {
  throw new Error(`Server error: ${response.status}`);
}
const data = await response.json();