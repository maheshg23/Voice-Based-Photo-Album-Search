## Voice Based Photo Album Search

##### [Link To Web Application Photo Album](http://smartphotoalbum.s3-website-us-east-1.amazonaws.com)


## FRONTEND (HTML, JavaScript, CSS)
The frontend is hosted in AWS S3 and provides a web-app user interface to interact with the chat bot. Many open source libraries and frameworks were used to design the UI/UX of the bot. 

## DESCRIPTION

"Voice Based Photo Album Search" is a serverless, microservice driven web-based application, that can be searched using natural language
through both text and voice. We can upload photos and search then similar to a image search engine. It is designed using multiple AWS components :-
##### AWS Transcribe, API-Gateway, Swagger, S3-Buckets, Lambda Functions, VPC, ElasticSearch, AWS Lex, AWS Rekognition, Cloud watch.

The Search query from the user is sent to AWS Lex which identifies the keywords from the query and searched the Elastic Search for the indices. If there is a match then it will return all the images that matched the search query. The search query can be text that the user enters or it can be a voice note where we would use AWS Transcribe to convert speech to text and then use the text for the search query.

The Upload workflow takes an image from the user local system and uplads it directly to S3 and then uses AWS rekognition to index the image which is later stored in Elastic search.

## ARCHITECHTURE :- 
![alt text](https://github.com/maheshg23/Voice-Based-Photo-Album-Search/blob/master/images/ArchitectureDiagram.png)


## SAMPLE UI OF THE WEB APPLICATION
![alt text](https://github.com/maheshg23/Voice-Based-Photo-Album-Search/blob/master/images/ApplicationUI.png)


## SAMPLE OUTPUT 
### Search a Photo
The user searches for a particular photo and it is displayed after the search is sccessful :-  
![alt text](https://github.com/maheshg23/Voice-Based-Photo-Album-Search/blob/master/images/SeachOutput.png)


### References `
- https://medium.com/@dhruvarora2/access-aws-services-like-rekognition-from-a-vpc-enabled-lambda-b1d6907bae93
- https://medium.com/@dhruvarora2/setup-an-ec2-instance-as-a-nat-gateway-217d9bce82a0
- https://medium.com/@dhruvarora2/uploading-images-to-s3-via-api-gateway-put-request-435a774bcdb8
- https://github.com/aws-samples/amazon-transcribe-websocket-static
