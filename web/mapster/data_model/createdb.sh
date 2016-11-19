mongo
use Mapster

db.tweets.insertMany(
   [
     { text: "ssssssss", name: "Ann", created_at: "A", },
     { text: "aaaaaaaaa", name: "Bob", created_at: "A", },
     { text: "cccccccc", name: "Alex", created_at: "D", } 
   ]
)