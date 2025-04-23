use("tech_blog_db");

//Liczbę postów według roli IT.
db.posts.aggregate([
    { $lookup: {
      from: "users",
      localField: "author_id",
      foreignField: "_id",
      as: "posts_users"
    }},
    { $unwind: "$posts_users" },
    { $group: {
        _id: "$posts_users.it_role",
        posts_count : { $sum: 1} 
    }}
]);

//Kategorie z największą liczbą polubień.

db.posts.aggregate([
    { $group: {
        _id: "$category",
        category_likes: { $sum: 1 }
    }},
    { $sort: {category_likes: -1 } },
    { $limit: 2 }
])
//Posty z największą liczbą komentarzy.

db.comments.aggregate([
    { $group: {
        _id: "$post_id",
        comments_count: { $sum: 1 }
    }},
    {$lookup: {
      from: "posts",
      localField: "_id",
      foreignField: "_id",
      as: "post_comments"
    }},
    { $unwind: "$post_comments" },
    { $sort: {comments_count: -1} },
    { $limit: 10 },
    { $project: {
        "post_comments.title": 1,
        "post_comments.author_id": 1,
        "post_comments.content": 1,
        "post_comments.category": 1,
        comments_count: 1,
    }}
])