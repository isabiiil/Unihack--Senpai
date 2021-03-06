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


def loginuser(userid, pw):

    utoken = str(uuid.uuid4())
    atoken = gimmetoken()

    userid = "115db214-8862-45bd-ad71-3b3ccf0156d7"

    url = "https://aca4e01c-1465-4012-8e84-f282757e54f9-us-east1.apps.astra.datastax.com/api/rest/v1/keyspaces/data/tables/users/rows/" + userid

    headers = {
        'accept': "application/json",
        'x-cassandra-request-id': utoken,
        'x-cassandra-token': atoken,
        'cache-control': "no-cache"
        }

    response = requests.request("GET", url, headers=headers)

    rjs = json.loads(response.text)

    if rjs['count'] >0: 
          if rjs['rows'][0]['password'] == pw:
                    return True
              
    return False



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


        userid= request_json['userid']
        pw =  request_json['password']

        resp =  loginuser(userid, pw)

        retjson = {}

        ##change required header

        retjson['status'] = str(resp)
    
        return json.dumps(retjson)


    retstr = "action not done"

    if request.args and 'message' in request.args:
        return request.args.get('message')
    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        return retstr
