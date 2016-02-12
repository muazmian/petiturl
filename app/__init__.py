from flask import Flask
from .redisConnection import RedisConnection

app = Flask(__name__)
redisConnection = RedisConnection('localhost', 6379)
from app import views
