/*************************** instructions

need to install express.js and below packages

npm install geolib
npm install csv-to-array

to run the program

nodejs server.js

keep the csv file and server.js in same directory level.


to test using command line

curl "http://localhost:8080/nearestPharmacy?lat=39.11578800&lon=-94.75981000" | python -m json.tool

{
    "address": "2860 SW MISSION WOODS DR",
    "distance": 12.97172012,
    "name": "JAYHAWK PHARMACY AND PATIENT SUPPLY"
}

**************************************/





var express = require('express');
var app = express();
var port = process.env.PORT || 8080;
geolib = require('geolib')
var pharmacies=[]

/*
After getting the user location, get the zip code of the location.

Then read database records of the pharmacies with matching zip code 

Then find the closest one from the filtered locations to the user location.

send back the response to the user.

The solution provided below is kind of using static data from csv. Reading all the csv data into json in this scenario. Some databases offer location based distance function so that we can filter records at database level and display final result to user.

*/

//reading into json array starts here
var columns = ["name","address","city","state","zip","latitude","longitude"];
require("csv-to-array")({
   file: "pharmacies.csv",
   columns: columns
}, function (err, array) {
  //console.log(err || array);
  pharmacies=array;  
});

//reading data ends here

app.get('/nearestPharmacy', function(req, res) {
  var latt = req.param('lat');
  var long = req.param('lon');
  var dist=[];
  var indexOfShortest;
  var shortestDist;
  for (var i =1; i < pharmacies.length; i++) {
       var dat = pharmacies[i];
      // shortest distance identification using geolib function
      dist[i-1]=geolib.getDistance({latitude: latt, longitude: long}, {latitude: dat.latitude, longitude: dat.longitude});    
      if (!shortestDist || dist[i-1] < shortestDist) {
      		shortestDist = dist[i-1];
     	        indexOfShortest=i-1;
      }
   }  
  //console.log(dist);
  //console.log(dist[indexOfShortest]);
  var miles=dist[indexOfShortest]*0.00062137;
  //console.log(indexOfShortest);
  //console.log(pharmacies[indexOfShortest+1]); 	
  //preparing response json.
  res.setHeader('Content-Type', 'application/json');
  res.send(JSON.stringify({ distance: miles,address: pharmacies[indexOfShortest].address,name: pharmacies[indexOfShortest].name }));
});

app.listen(port);
console.log('Server started! At http://localhost:' + port);
