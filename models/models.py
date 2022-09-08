from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Tweet(Base):
    __tablename__ = 'tweet'

    id = Column(Integer, primary_key=True)
    tweetId = Column(String)
    tweetBody = Column(String)
    createdBy = Column(String)
    createdAt = Column(DateTime)
    hashtags = relationship('Hashtag', secondary='tweet_hashtag', back_populates='tweets')

    
    def as_json(self):
        return {
            "tweetId": self.tweetId, 
            "tweetBody": self.tweetBody, 
            "createdBy": self.createdBy, 
            "createdAt": self.createdAt, 
            "hashtags": list(map(lambda x: x.text, self.hashtags))
        }
    


class Hashtag(Base):
    __tablename__ = 'hashtag'

    id = Column(Integer, primary_key=True)
    text = Column(String)
    tweets = relationship('Tweet', secondary='tweet_hashtag', back_populates='hashtags')


class TweetHashtag(Base):
    __tablename__ = 'tweet_hashtag'

    id = Column(Integer, primary_key=True)
    tweetId = Column(Integer, ForeignKey('tweet.id'))
    hashtagId = Column(Integer, ForeignKey('hashtag.id'))


