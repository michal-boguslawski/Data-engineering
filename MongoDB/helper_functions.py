from random import choice
from datetime import timedelta, datetime
from pymongo import MongoClient
from urllib.parse import quote_plus

from predefined_lists import it_roles, categories, seniorities


def generate_users(num_users: int):
    users = []
    for i in range(num_users):
        user = {
            "name": f"User{i}",
            "email": f"user{i}@example.com",
            "it_role": choice(it_roles),
            "seniority": choice(seniorities),
            "join_date": (datetime.now() - timedelta(days=choice(range(365))))
        }
        users.append(user)
    return users

def generate_posts(num_posts: int, users: list[str]):
    posts = []
    for i in range(num_posts):
        post = {
            "title": f"Post {i}",
            "author_id": choice(users),
            "content": f"This is the content of post {i}",
            "category": choice(categories),
            "date": (datetime.now() - timedelta(days=choice(range(365)))),
            "likes": choice(range(100))
        }
        posts.append(post)
    return posts

def generate_comments(num_comments: int, users: list[str], posts: list[str]):
    comments = []
    for i in range(num_comments):
        comment = {
            "post_id": choice(posts),
            "user_id": choice(users),
            "content": f"This is the content of comment {i}",
            "date": (datetime.now() - timedelta(days=choice(range(365)))),
            "likes": choice(range(100))
        }
        comments.append(comment)
    return comments

def get_client():
    user = "admin"
    password = "password123"
    host = "localhost:27017/"

    uri = f"mongodb://{user}:{password}@{host}"

    # print(uri)

    # Create connection
    client = MongoClient(uri)
    return client
