import os
import pymongo
import json
import uuid
import time
import requests


def gimmetoken():
    url = "https://aca4e01c-1465-4012-8e84-f282757e54f9-us-east1.apps.astra.datastax.com/api/rest/v1/auth"

    payload = "{\"username\":\"moody\",\"password\":\"Moody921\"}"
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "fd91ccce-5703-4cde-ab48-9bee17b2daba"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    # print(response.text)

    rj = json.loads(response.text)

    # print (rj['authToken'])

    return rj['authToken']



def registeruser(username, pw, imgurl, utoken, utoken2):

    url = "https://aca4e01c-1465-4012-8e84-f282757e54f9-us-east1.apps.astra.datastax.com/api/rest/v1/keyspaces/data/tables/users/rows"

    atoken = gimmetoken()

    payload = {}
    pc = []
    pc.append({"name":"id","value":utoken})
    pc.append({"name":"name","value":username})
    pc.append({"name":"password","value":pw})
    pc.append({"name":"avatar","value":imgurl})

    payload ['columns'] = pc

    jpayload = json.dumps(payload)

    # payload = "{\"columns\":[,,,]}"
    headers = {
        'accept': "application/json",
        'content-type': "application/json",
        'x-cassandra-request-id': utoken2,
        'x-cassandra-token': atoken,
        'cache-control': "no-cache"
        }

    response = requests.request("POST", url, data=jpayload, headers=headers)

    return response.text





def dummy(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    if request.method == 'OPTIONS':
        # Allows GET requests from origin https://mydomain.com with
        # Authorization header
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Max-Age': '3600',
            'Access-Control-Allow-Credentials': 'true'
        }
        return ('', 204, headers)

    # Set CORS headers for main requests
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': 'true'
    }

    request_json = request.get_json()
    # mongostr = os.environ.get('MONGOSTR')
    # client = pymongo.MongoClient(mongostr)
    # db = client["hackthis"]
    # col = db.tasks 
    # results = []
    # payload = {}
    # maxid = 0
    
    if request_json:

        utoken = str(uuid.uuid4())
        time.sleep(1)
        utoken2 = str(uuid.uuid4())
        # time.sleep(1)
        # utoken3 = str(uuid.uuid4())


        username = request_json['user']
        pw =  request_json['password']
        imgurl = request_json['avatar']

        resp =  registeruser(username, pw, imgurl, utoken, utoken2)
        retjson = {}

        ##change required header

        retjson['status'] = resp
        retjson['userid'] = utoken
    
        return json.dumps(retjson)


    retstr = "action not done"

    if request.args and 'message' in request.args:
        return request.args.get('message')
    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        return retstr
