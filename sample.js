// Load the SDK for JavaScript
var AWS = require('aws-sdk');
// Load credentials and set region from JSON file
AWS.config.loadFromPath('./config.json');

// Create S3 service object
s3 = new AWS.S3({apiVersion: '2006-03-01'});
                    
// Call S3 to list current buckets
// s3.listBuckets(function(err, data) {
//    if (err) {
//       console.log("Error", err);
//    } else {
//       console.log("Bucket List", data.Buckets);
//    }
// });

// Create the parameters for calling createBucket
// var bucketParams = {
//    Bucket : process.argv[2]
// };                    
                                   
//  // Call S3 to create the bucket
// s3.createBucket(bucketParams, function(err, data) {
//    if (err) {
//       console.log("Error", err);
//    } else {
//       console.log("Success", data.Location);
//    }
// });

//Upload data
var uploadParams = {Bucket: process.argv[2], Key: '', Body: ''};
var file = process.argv[3];

// call S3 to retrieve upload file to specified bucket
var fs = require('fs');

var fileStream = fs.createReadStream(file);
fileStream.on('error', function(err) {
  console.log('File Error', err);
});
uploadParams.Body = fileStream;
var path = require('path');
uploadParams.Key = path.basename(file);
// call S3 to retrieve upload file to specified bucket
s3.upload (uploadParams, function (err, data) {
  if (err) {
    console.log("Error", err);
  } if (data) {
    console.log("Upload Success", data.Location);
  }
});

//list all bucket data
//  var bucketParams = {
//     Bucket : process.argv[2]
//  };  
//  s3.listObjects(bucketParams, function(err, data) {
//    if (err) console.log(err, err.stack); // an error occurred
//    else     console.log(data.Contents);           // successful response
//  });
