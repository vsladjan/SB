from flask import current_app, request
from flask import Response
from flask import jsonify

from .base_controller import BaseController
from models.tweet_dmodel import TweetDmodel
from util.error import Error
from util.helper import Helper

class TweetsController(BaseController):

    QUERY_HASHTAG = 'hashTag'
    QUERY_USERNAME = 'username'
    QUERY_LIMIT = 'limit'
    QUERY_OFFSET = 'offset'

    def __init__(self, db):
        super().__init__(db)
        self.tweetDmodel = TweetDmodel(db)
        self.helper = Helper()

    def tweetsGet(self):
        #get data from request
        hashTag = request.args.getlist(self.QUERY_HASHTAG)
        usernames = request.args.getlist(self.QUERY_USERNAME)
        limit = request.args.get(self.QUERY_LIMIT)
        offset = request.args.get(self.QUERY_OFFSET)

        # return integer from string if number is > 0, otherwise -1
        limit_number = self.helper.getInt(limit)
        offset_number = self.helper.getInt(offset)

        # return 400 error if validation does not pass
        if limit_number == -1 or offset_number == -1:
            error = Error(400, 103, "Bad request, integers are required in limit and offset")
            response = Response(response=error.toJSON(), status=error.httpCode, mimetype="application/json")
            response.headers["Content-Type"] = "application/json"
            return response

        #Get data from database since everything is ok
        limit_number = limit_number if limit_number > 0 and limit_number <= 100 else 50
        requestDict = {
            "hashTag" : hashTag,
            "usernames" : usernames,
            "limit": limit_number,
            "offset": offset_number
        }
        values = self.tweetDmodel.getTweets(requestDict)
        new_offset = offset_number + limit_number
        newUrl = self.helper.changeUrl(request.url, new_offset)

        response = None
        #if new_offset >= len(values):
        #    response = { "tweets": values }
        #else:
        response = {
            "tweets": values,
            "nextPage": newUrl
        }
        return jsonify(response)


    def tweetsPost(self):
        username = request.environ['X-username']
        data = request.json
        tweetBody = data['tweetBody'] if 'tweetBody' in data else ''
        hashTags = data["hashTags"] if 'hashTags' in data else []

        #return 400 (bad request) if validation does not pass
        if len(hashTags) > 5 or len(tweetBody) > 320:
            error = Error()
            if len(hashTags) > 5:
                error.errorCode = 101 #or whatever else code number
                error.message = "Bad request, number of hashtags must be between 0 and 5"
            if (len(tweetBody) > 320):
                error.errorCode = 100 #or whatever else code number
                error.message = "Bad request, tweetBody message must have less than 320 characters"
            response = Response(response=error.toJSON(), status=error.httpCode, mimetype="application/json")
            response.headers["Content-Type"] = "application/json"
            return response

        data = {
            "username": username,
            "tweetBody": tweetBody,
            "hashTags": hashTags
        }

        result = self.tweetDmodel.postTweet(data)
        return jsonify(result)


    def tweetsDelete(self, id):
        username = request.environ['X-username']
        tweetId = id

        data = {
            "username": username,
            "tweetId": tweetId
        }

        result = self.tweetDmodel.deleteTweet(data)

        # return value jsonifyed if result got deleted
        if result['returnCode'] == 'deleted':
            return jsonify(result['returnData'])
        else:
            # return error depending did id or username check failed
            error = None
            if result['returnCode'] == 'id':
                error = Error(404, 90, "Tweet not found")
            elif result['returnCode'] == 'username':
                error = Error(403, 90, 'Forbidden response, user tried to delete somebody elses tweet')
            response = Response(response=error.toJSON(), status=error.httpCode, mimetype="application/json")
            response.headers["Content-Type"] = "application/json"
            return response