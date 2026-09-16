// Definition: CORS
// CORS (Cross-Origin Resource Sharing) is a browser security policy that blocks JavaScript from making requests 
// to a different domain than the page it is on.
// If your HTML file is on localhost:5500 and your Python API is on localhost:8000, 
// the browser blocks the request by default. The Python server must include the right response headers to allow it.

// Problem	                              What happens	                      Fix
// No CORS headers	                 Browser blocks request, console error	 Add CORSMiddleware in FastAPI
// Wrong origin in allow_origins	Request blocked for specific origin  	Use ["*"] in dev, specific domains in production
// Preflight OPTIONS fails	         POST/PUT requests blocked	             Add allow_methods=["*"]

// Tip:
//  allow_origins=["*"] is fine for development.
//  In production, replace "*" with the specific domain of your front end, for example ["https://amerix.co.ke"]. 
// This ensures only your site can call your API.