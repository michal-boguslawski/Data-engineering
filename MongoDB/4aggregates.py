from helper_functions import get_client
import pandas as pd

# Connect to database
client = get_client()
db = client.get_database("tech_blog_db")

# Posts count by IT role
posts_count = db.posts.aggregate([
    {
        "$lookup": {
            "from": "users",
            "localField": "author_id",
            "foreignField": "_id",
            "as": "author"
        }
    },
    {
        "$unwind": "$author"
    },
    {
        "$group": {
            "_id": "$author.it_role",
            "count": {"$sum": 1}
        }
    }
])

print("Count by role: ")
print(pd.DataFrame(posts_count.to_list()))

# Categories with most posts likes
categories = db.posts.aggregate([
    {
        "$group": {
            "_id": "$category",
            "likes": {"$sum": "$likes"}
        }
    },
    {
        "$sort": {"likes": -1}
    }
])

print("Mosts likes: ")
print(pd.DataFrame(categories.to_list()))

# Posts with most comments
posts = db.comments.aggregate([
    {
        "$group": {
            "_id": "$post_id",
            "comments_count": {"$sum": 1}
        }
    },
    {
        "$sort": {"comments_count": -1}
    },
    {
        "$lookup": {
            "from": "posts",
            "localField": "_id",
            "foreignField": "_id",
            "as": "post_comments"
        }
    },
    {
        "$unwind": "$post_comments"
    },
    {
        "$limit": 10
    },
    {
        "$project": {
            "title": "$post_comments.title",
            "author_id": "$post_comments.author_id",
            "category": "$post_comments.category",
            "content": "$post_comments.content",
            "comments_count": 1
        }
    }
])

print("Most comments: ")
print(pd.DataFrame(posts.to_list()))
