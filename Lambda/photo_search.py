import json
import boto3
import requests

def clearIndices():
    host = 'https://vpc-photos-ckzmaanotkmt2wvajojjlqunvm.us-east-1.es.amazonaws.com/photos/'
    res = requests.delete(host)
    res = json.loads(res.content.decode('utf-8'))
    return res   

def searchIndices():
    host = 'https://vpc-photos-ckzmaanotkmt2wvajojjlqunvm.us-east-1.es.amazonaws.com/photos/_search?q=dog'
    res = requests.get(host)
    res = json.loads(res.content.decode('utf-8'))
    return res

def searchElasticIndex(search):
    photos = []
    for s in search:
        host = 'https://vpc-photos-ckzmaanotkmt2wvajojjlqunvm.us-east-1.es.amazonaws.com/photos/_search?q='+s
        res = requests.get(host)
        res = json.loads(res.content.decode('utf-8'))
        for item in res["hits"]["hits"]:
            bucket = item["_source"]["bucket"]
            key = item["_source"]["objectKey"]
            photoURL = "https://{0}.s3.amazonaws.com/{1}".format(bucket,key)
            photos.append(photoURL)
    return photos

def prepareForSearch(res):
    photos = []
    if res["slots"]["query"] != None:
        photos.append(res["slots"]["query"])
    if res["slots"]["search"] != None:
        photos.append(res["slots"]["search"])
    return photos

def sendToLex(message):
    lex = boto3.client('lex-runtime')
    response = lex.post_text(
        botName='photosforsearch',
        botAlias='photos',
        userId='lf1',
        inputText=message)
    return response
    
def lambda_handler(event, context):
    # TODO implement
    photos = []
    #res = clearIndices() used to clear indexes in ES
    #res = searchIndices() #used to check index
    message = event["params"]["querystring"]["q"]
    resFromLex = sendToLex(message)
    search = prepareForSearch(resFromLex)
    photos = searchElasticIndex(search)
    return {
        'statusCode': 200,
        'body': json.dumps(photos)
    }
