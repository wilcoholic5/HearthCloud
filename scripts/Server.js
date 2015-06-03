//lets require/import the mongodb native drivers.
var mongodb = require('mongodb');
var fs = require('fs');
//We need to work with "MongoClient" interface in order to connect to a mongodb server.
var MongoClient = mongodb.MongoClient;

// Connection URL. This is where your mongodb server is running.
var url = 'mongodb://localhost:27017/comments';

var MongoClient = require('mongodb').MongoClient;
 
var myCollection;
var db = MongoClient.connect('mongodb://127.0.0.1:27017/comments', function(err, db) {
	if(err)
		throw err;
	console.log("connected to the mongoDB !");
	myCollection = db.collection('cardData');
	cards = myCollection.find()
	totalComments = 0;
	cardCount = 0;
	averageComments = 0;
	cards.forEach(function (card) {
		if (card.commentCount != undefined) {
			cardCount++;
			totalComments += card.commentCount
			averageComments = totalComments/cardCount;
		}
	})
});

var WebSocketServer = require('websocket').server;
var http = require('http');

var server = http.createServer(function(request, response) {
	// process HTTP request. Since we're writing just WebSockets server
	// we don't have to implement anything.
});
server.listen(1337, function() { });
stuff = '';
function cardSearch(name, connection) {
	try {
		return myCollection.findOne({cardName : name},
		function(err, result) {   // callback
			stuff = result
			console.log(stuff)
			var html = fs.readFile("../cards/Polarity/"+result.cardName+".txt", "utf8", function(error, data) {
				result.html = data;
				var html = fs.readFile("../cards/Subjectivity/"+result.cardName+".txt", "utf8", function(error, data) {
					result.html2 = data;
					result.popularity = Number((result.commentCount/averageComments).toFixed(1));
					connection.sendUTF(JSON.stringify(result));
				});
			})
		
			return result
		});
	} catch (err) {
		connection.sendUTF("card does not exist in our records");
	}
}

// create the server
wsServer = new WebSocketServer({
	httpServer: server
});

// WebSocket server
wsServer.on('request', function(request) {
	var connection = request.accept(null, request.origin);
	// This is the most important callback for us, we'll handle
	// all messages from users here.
	connection.on('message', function(message) {
		if (message.type === 'utf8') {
			console.log('finding the card')
			cardData = cardSearch(message.utf8Data, connection)
		}
	});

	connection.on('close', function(connection) {
		// close user connection
	});
});