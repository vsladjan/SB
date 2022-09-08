import uuid
from sqlalchemy.orm import Session
from .models import Hashtag, Tweet, TweetHashtag
import datetime

class TweetDmodel:

    def __init__(self, db):
        self.db = db

    def getTweets(self, requestDict):
        session = Session(self.db.eng, future=True)
        if requestDict['usernames'] or requestDict['hashTag']:
            usernameFilter = Tweet.createdBy.in_(requestDict['usernames']) if requestDict['usernames'] else True
            hashClause = Hashtag.text.in_(requestDict['hashTag']) if requestDict['hashTag'] else True

            result = session.query(Tweet).join(TweetHashtag).join(Hashtag)\
                            .where(hashClause).filter(usernameFilter)\
                            .group_by(Tweet.id).order_by(Tweet.createdAt.desc())\
                            .limit(requestDict['limit']).offset(requestDict['offset']).all()
        else:
            result = session.query(Tweet).order_by(Tweet.createdAt.desc())\
                            .limit(requestDict['limit']).offset(requestDict['offset']).all()

        return_list = list(map(lambda x: x.as_json(), result))
        session.close()
        print(len(result))

        return return_list

    def postTweet(self, data):
        session = Session(self.db.eng, future=True)
        newTweet = Tweet(tweetBody=data['tweetBody'], 
                            createdBy=data['username'], 
                            createdAt=datetime.datetime.now(), 
                            tweetId=uuid.uuid4())
        session.add(newTweet)

        for hash in data['hashTags']:
            hashTag = session.query(Hashtag).where(Hashtag.text == hash).first()
            if hashTag is None:
                hashTag = Hashtag(text=hash)
            session.add(hashTag)
            newTweet.hashtags.append(hashTag)

        value = newTweet.as_json()

        session.commit()
        session.close()
        
        return value


    def deleteTweet(self, data):
        session = Session(self.db.eng, future=True)
        tweet = session.query(Tweet).where(Tweet.tweetId == data['tweetId']).first()
        returnData = None
        if (tweet is not None):
            if tweet.createdBy == data['username']:
                returnData = tweet.as_json()
                session.delete(tweet)
                returnCode = 'deleted'
            else:
                returnCode = 'username'
        else:
            returnCode = 'id'

        value = {
            'returnCode': returnCode,
            'returnData': returnData
        }

        session.commit()
        session.close()

        return value