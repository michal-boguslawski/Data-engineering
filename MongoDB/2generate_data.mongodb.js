use("tech_blog_db")

const it_roles = ["Frontend Developer", "Backend Developer", "DevOps Engineer", "Software Engineer", "Data Engineer", "QA Engineer", "Full Stack Developer"]
const categories = ["JavaScript", "Python", "Java", "DevOps", "Cloud", "Architecture", "Best Practices", "Testing", "Security", "Machine Learning", "Database"]
const seniorities = ["Junior", "Mid", "Senior", "Lead", "Principal"]


// Funkcje pomocnicze generujące dane losowe
function randomInt(min, max) {
    return NumberInt(Math.floor(Math.random() * (max - min + 1)) + min);
}

function generateRandomText(length) {
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    let result = '';
    const charactersLength = characters.length;
    
    for (let i = 0; i < length; i++) {
      result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
  
    return result;
  }

function randomDate(start, end) {
    return new Date(start.getTime() + Math.random() * (end.getTime() - start.getTime()));
}

function randomElement(array) {
    return array[Math.floor(Math.random() * array.length)];
}

// Funkcja generowania klientów
function generateUsers(count) {
    let users = [];
    for (let i = 0; i < count; i++) {
        users.push({
            name: `Customer${i}`,
            email: `customer${i}@example.com`,
            it_role: randomElement(it_roles),
            seniority: randomElement(seniorities),
            join_date: randomDate(new Date(2020, 0, 1), new Date()),
            bio: generateRandomText(randomInt(100, 500))
        });
    }
    return users;
}

function generateTags(count) {
    let tags = [];
    for (let i = 0; i < count; i ++){
        tags.push(generateRandomText(randomInt(1, 10)))
    }
    return tags
}

function generatePosts(userIds, count) {
    let posts = [];
    for (let i = 0; i < count; i++) {
        posts.push({
            title: generateRandomText(randomInt(5, 200)),
            author_id: randomElement(userIds),
            content: generateRandomText(randomInt(20, 5000)),
            category: randomElement(categories),
            date: randomDate(new Date(2020, 0, 1), new Date()),
            likes: randomInt(0, 10000),
            tags: generateTags(randomInt(1, 10))
        })
    }
    return posts
}

function generateComments(postIds, userIds, count) {
    let posts = [];
    for (let i = 0; i < count; i++) {
        posts.push({
            post_id: randomElement(postIds),
            user_id: randomElement(userIds),
            content: generateRandomText(randomInt(20, 200)),
            date: randomDate(new Date(2020, 0, 1), new Date()),
            likes: randomInt(0, 10000)
        })
    }
    return posts
}

let users = generateUsers(1000);
db.users.insertMany(users);

let user_ids = db.users.distinct("_id");
let posts = generatePosts(user_ids, 5000);
db.posts.insertMany(posts);

let post_ids = db.posts.distinct("_id");
let comments = generateComments(post_ids, user_ids, 10000);
db.comments.insertMany(comments);
