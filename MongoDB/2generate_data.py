# from predefined_lists import it_roles, categories, seniorities
from helper_functions import generate_users, generate_posts, generate_comments, get_client

# Connect to database
client = get_client()
db = client.get_database("tech_blog_db")

# Generate users
users = generate_users(1000)
db.users.insert_many(users)

# Generate posts
unique_users = db.users.distinct("_id")
posts = generate_posts(10000, unique_users)
db.posts.insert_many(posts)

# Generate comments
unique_posts = db.posts.distinct("_id")
comments = generate_comments(100000, unique_users, unique_posts)
db.comments.insert_many(comments)
