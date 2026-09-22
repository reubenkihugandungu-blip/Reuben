## What this looks like with a real API: Facebook Graph
# The Facebook Graph API is one of the most widely used authenticated APIs in the world
# Every request requires an access token passed as a query parameter. 
# The endpoint structure is versioned, and the response is nested JSON with page data, 
# follower counts, and post content.

# Below is the endpoint URL to fetch public data from a Facebook page, and the JSON structure 
# the API returns. The page used here is facebook.com/amerix041.

# Facebook graph API V18.:ENDPOINT
Get https://graph.facebook.com/v18.0/amerix041
?fields=name,fan_count,followers_count,about
&access_token=YOUR_ACCESS-TOKEN

