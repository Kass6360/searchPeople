from weibo import APIClient
import ConfigParser

def connect():
    config = ConfigParser.ConfigParser()
    key_value = config.read('./key.ignore')

    APP_KEY = config.get('keys', 'key')
    APP_SECRET = config.get('keys', 'secrit')
    CALLBACK_URL = 'http://www.example.com/callback' # callback url
    print APP_KEY, APP_SECRET


connect()
