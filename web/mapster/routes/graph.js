var express = require('express');
var router = express.Router();
const assert = require('assert');

/* GET users listing. */
router.get('/', function(req, res, next) {
	//var d3 = require("d3");
	fs = require('fs');
	var path = __base+'public/miserables.json';
	//var graph = JSON.parse(fs.readFileSync(path, 'utf8'));
  var graph = fs.readFileSync(path, 'utf8');

	res.render('graph', { title: 'Mapster -- graph', graph:graph} );
});

/* GET users listing. */
router.get('/bubble', function(req, res, next) {

  // var d3 = require("d3");
  // fs = require('fs');
  // var path = __base+'public/flare.csv';
  // var bubblestr = fs.readFileSync(path, 'utf8');

  fs = require('fs');
  var path = __base+'public/brand.json';
  var bubble = fs.readFileSync(path, 'utf8');
  
  res.render('bubble', { title: 'Mapster -- bubbleview', bubble:bubble} );
});

/* GET users listing. */
router.get('/tweets', function(req, res, next) {
  fs = require('fs');
  var path = __base+'public/brand.json';
  var bubble = fs.readFileSync(path, 'utf8');

  var url = 'mongodb://localhost:27017/Mapster';
  var MongoClient = require('mongodb').MongoClient;
  var assert = require('assert');

  MongoClient.connect(url, function(err, db) {
    assert.equal(null, err);
    getTweets(db, function(tweets) {
      console.log("tweets");
      console.info(tweets);
      db.close();
      res.render('tweets', { title: 'Mapster -- tweets', tweets:tweets});
    });
  });
});

var getTweets = function(db, callback) {
  var cursor = db.collection("tweets").find().sort({_id:1}).limit(10);
  cursor.toArray(function(err, items){
    if (!err) {
      callback(items)
    }
  });
};

module.exports = router;
