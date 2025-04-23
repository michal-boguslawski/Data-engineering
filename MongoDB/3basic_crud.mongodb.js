use("tech_blog_db")

// Dodawanie nowego posta
let user_id = db.users.findOne({"name": "Customer100"}, { _id: 1});

db.posts.insertOne({
    title: "Nowy tytuł",
    author_id: user_id._id,
    content: "To jest nowy post, który dodałem ręcznie",
    category: "Python",
    date: new Date(2025, 4, 13),
    likes: 1000000 
})


// wyszukowanie postów
// wg kategorii
db.posts.find({ category: "Python" })
// wg liczby polubień
db.posts.findOne({ likes: { $gt: 100000} })

//aktualizacja postów
//jeden dokument

let nowy_tag = ["Jakis", "nowy", "tag"];
db.posts.updateOne(
    { title: "Nowy tytuł" },
    { $set: {tags: nowy_tag} }
)
db.posts.findOne({ likes: { $gt: 100000} })

//wiele dokumentów

db.posts.updateMany(
    { category: "Python" },
    { $inc: {likes: 1000} }
)
db.posts.find({ category: "Python" })

//usuwanie postów
db.posts.deleteOne({title: "Q5z2ctFxhvshNgbMp0ORTU6gBOwTNcZZQGkpQytd7FbrGXQ2sQhmXudSY6s0TQeBWMSqXKhfrr1YiXS6pvTDWgqMqbU"})
db.posts.find({title: "Q5z2ctFxhvshNgbMp0ORTU6gBOwTNcZZQGkpQytd7FbrGXQ2sQhmXudSY6s0TQeBWMSqXKhfrr1YiXS6pvTDWgqMqbU"})