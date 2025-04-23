use("tech_blog_db")

const it_roles = ["Frontend Developer", "Backend Developer", "DevOps Engineer", "Software Engineer", "Data Engineer", "QA Engineer", "Full Stack Developer"]
const categories = ["JavaScript", "Python", "Java", "DevOps", "Cloud", "Architecture", "Best Practices", "Testing", "Security", "Machine Learning", "Database"]
const seniorities = ["Junior", "Mid", "Senior", "Lead", "Principal"]


db.createCollection("users", {
    validator: {
        $jsonSchema: {
            bsonType: "object",
            required: ["name", "email", "it_role", "seniority"],
            properties: {
                name: {
                    bsonType: "string",
                    minLength: 2,
                    maxLength: 50,
                    description: "Name of user, requires"
                },
                email: {
                    bsonType: "string",
                    pattern: "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$",
                    description: "Customer email address, required"
                },
                it_role: {
                    enum: it_roles,
                    description: "Role in IT department"
                },
                seniority: {
                    enum: seniorities,
                    description: "Seniority of a role"
                },
                join_date: {
                    bsonType: "date",
                    description: "Join date of the user"
                },
                bio: {
                    bsonType: "string",
                    maxLength: 500,
                    description: "Short description of the user"
                }
            }
        }
    }
})

db.createCollection("posts", {
    validator: {
        $jsonSchema: {
            bsonType: "object",
            required: ["title", "author_id", "content", "category", "date"],
            properties: {
                title: {
                    bsonType: "string",
                    minLength: 5,
                    maxLength: 200,
                    description: "Title of the post"
                },
                author_id: {
                    bsonType: "objectId",
                    description: "User Id"
                },
                content: {
                    bsonType: "string",
                    minLength: 20,
                    description: "Post body"
                },
                category: {
                    enum: categories,
                    description: "Category of post"
                },
                date: {
                    bsonType: "date",
                    description: "Creation date of the post"
                },
                likes: {
                    bsonType: "int",
                    minimum: 0,
                    description: "Count of likes"
                },
                tags: {
                    bsonType: "array",
                    items: {
                        bsonType: "string",
                        minLength: 0,
                        maxLength: 10
                    }
                }
            }
        }
    }
})

db.createCollection("comments", {
    validator: {
        $jsonSchema: {
            bsonType: "object",
            required: ["post_id", "user_id", "content", "date"],
            properties: {
                post_id: {
                    bsonType: "objectId",
                    description: "Post id"
                },
                user_id: {
                    bsonType: "objectId",
                    description: "User Id"
                },
                content: {
                    bsonType: "string",
                    minLength: 20,
                    description: "Comment body"
                },
                date: {
                    bsonType: "date",
                    description: "Creation date of the post"
                },
                likes: {
                    bsonType: "int",
                    minimum: 0,
                    description: "Count of likes"
                }
            }
        }
    }
})
