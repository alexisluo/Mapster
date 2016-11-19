

function connectDB(url) {
	var url = 'mongodb://localhost:27017/test';
	MongoClient.connect(url, function(err, db) {
  		assert.equal(null, err);
  		console.log("Connected correctly to server.");
  		db.close();
	});

	/*
	var databaseUrl = "mydb"; // "username:password@example.com/mydb"
	var collections = ["users", "reports"]
	var db = require("mongojs").connect(databaseUrl, collections);
	*/
}




//module.exports = db;
