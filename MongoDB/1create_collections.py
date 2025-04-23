from helper_functions import get_client
from predefined_lists import it_roles, categories, seniorities


client = get_client()
print([x for x in client.list_databases()])

db = client.get_database("tech_blog_db")

# Define schema
user_schema = {
    "validator": {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["name", "email", "it_role", "seniority"],
            "properties": {
                "name": {
                    "bsonType": "string",
                    "minLength": 2,
                    "maxLength": 50,
                    "description": "Name of user, required"
                },
                "email": {
                    "bsonType": "string",
                    "pattern": "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$",
                    "description": "Customer email address, required"
                },
                "it_role": {
                    "enum": it_roles,
                    "description": "Role in IT department"
                },
                "seniority": {
                    "enum": seniorities,
                    "description": "Seniority of a role"
                },
                "join_date": {
                    "bsonType": "date",
                    "description": "Join date of the user"
                },
                "bio": {
                    "bsonType": "string",
                    "maxLength": 500,
                    "description": "Short description of the user"
                }
            }
        }
    }
}


db.create_collection("users", validator=user_schema["validator"])
print("Collection 'users' created with schema.")

# Define the JSON Schema
post_schema = {
    "validator": {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["title", "author_id", "content", "category", "date"],
            "properties": {
                "title": {
                    "bsonType": "string",
                    "minLength": 5,
                    "maxLength": 200,
                    "description": "Title of the post"
                },
                "author_id": {
                    "bsonType": "objectId",
                    "description": "User Id"
                },
                "content": {
                    "bsonType": "string",
                    "minLength": 20,
                    "description": "Post body"
                },
                "category": {
                    "enum": categories,
                    "description": "Category of post"
                },
                "date": {
                    "bsonType": "date",
                    "description": "Creation date of the post"
                },
                "likes": {
                    "bsonType": "int",
                    "minimum": 0,
                    "description": "Count of likes"
                },
                "tags": {
                    "bsonType": "array",
                    "items": {
                        "bsonType": "string",
                        "minLength": 0,
                        "maxLength": 10
                    }
                }
            }
        }
    }
}

# Create the collection
db.create_collection("posts", validator=post_schema["validator"])
print("Collection 'posts' created with schema.")

# Define the JSON Schema
comment_schema = {
    "validator": {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["post_id", "user_id", "content", "date"],
            "properties": {
                "post_id": {
                    "bsonType": "objectId",
                    "description": "Post id"
                },
                "user_id": {
                    "bsonType": "objectId",
                    "description": "User Id"
                },
                "content": {
                    "bsonType": "string",
                    "minLength": 20,
                    "description": "Comment body"
                },
                "date": {
                    "bsonType": "date",
                    "description": "Creation date of the post"
                },
                "likes": {
                    "bsonType": "int",
                    "minimum": 0,
                    "description": "Count of likes"
                }
            }
        }
    }
}

# Create the collection
db.create_collection("comments", validator=comment_schema["validator"])
print("Collection 'comments' created with schema.")