#👉  When a developer calls the X API to fetch a post, the response is a nested JSON object. 
# The post text is buried inside a data key. The engagement numbers are inside public_metrics inside data.
#  The author details are in a separate includes section. 
# No different from what you have been parsing all lesson.
# Below is a post from x.com/amerix, structured exactly as the X API v2 would return it. 
# No keys, no connection, just the structure.

# Parse a real x API response
# This is what the X API v2 returns when you fetch a post
# structure: data (the post) + includes (the author details)
x_response = {
    "data": {
        "id": "2076589716036608320",
        "text": "Live by a code:\n\n* Loyalty.\n* Strength.\n* Honour.\n*Discipline.\n\nIf you stand for nothing, you fall for anything.",
        "created_at": "2026-07-14T05:30:00Z",
        "author_id": "748352990",
        "public_metrics": {
            "retweet_count": 2104,
            "reply_count": 487,
            "like_count": 11380,
            "quote_count": 319,
            "bookmark_count": 4251
        }
    },
    "includes": {
        "users": [
            {
                "id": "748352990",
                "name": "Amerix",
                "username": "amerix",
                "public_metrics": {
                    "followers_count": 1200000,
                    "following_count": 487
                }
            }
        ]
    }
}

# Parse it exactly as you have been parsing all lesson
post = x_response["data"]
author = x_response["includes"]["users"][0]
metrics = post["public_metrics"]

print("POST")
print(f" Author: @{author['username']} ({author['name']})")
print(f" Text: {post['text'][:60]}...")
print(f" Posted: {post['created_at']}")
print()
print("ENGAGEMENT")
print(f" Likes: {metrics['like_count']:,}")
print(f" Retweets: {metrics['retweet_count']:,}")
print(f" Replies: {metrics['reply_count']:,}")
print(f" Bookmarks: {metrics['bookmark_count']:,}")
print()
print(f"AUTHOR: @{author['username']} has {author['public_metrics']['followers_count']:,} followers")
print(f"Read more at: https://x.com/{author['username']}")
print(f"Engagement rate: {(metrics['like_count'] + metrics['retweet_count'] + metrics['reply_count']) / author['public_metrics']['followers_count'] * 100:.2f}%")

# Calculate the engagement rate as a percentage. 
# Formula: (likes + retweets + replies) / followers * 100. Add one line that prints it rounded to two decimal places

# Whether you are parsing an SMP member record, a weather API, or an X post, the pattern does not change:
#  navigate layer by layer, use .get() for optional fields, pull only what you need. The API changes. The technique does not.