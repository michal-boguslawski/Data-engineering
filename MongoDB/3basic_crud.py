from helper_functions import get_client
from datetime import datetime

# Connect to database
client = get_client()
db = client.get_database("tech_blog_db")

# add new post
user = db.users.find_one({"name": "User100"})["_id"]
print(user)

new_post = {
    "title": "Post 100",
    "author_id": user,
    "content": "This new post created manually",
    "category": "Cloud",
    "date": datetime(2024, 5, 1),
    "likes": 1001
}

db.posts.insert_one(new_post)

# find posts by category
posts = db.posts.find({"category": "Cloud"})
print(posts.to_list()[:5])

# find posts by likes
posts = db.posts.find({"likes": {"$gt": 1000}})
print("By likes: ", posts.to_list())

# delete post
posts = db.posts.find_one({"content": "This new post created manually"})
print("Before delete:", posts)
print("---------------------------------")
popped = db.posts.find_one_and_delete({"content": "This new post created manually"})
print("Deleted element:", popped)
posts = db.posts.find_one({"content": "This new post created manually"})
print("After delete:", posts)
