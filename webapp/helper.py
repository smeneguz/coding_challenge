import bcrypt
from pymongo import MongoClient
import http
import requests
"""
HELPER FUNCTIONS
"""

client = MongoClient("mongodb://MongoDB:27017")
db = client.projectDB
images = db["Img"]

def userExist(username):
    exist = False
    if images.find_one({"Username": username}):
        exist = True
    return exist

def verifyUsers(username, password):
    if not userExist(username):
        return False

    user_hashed_pw = images.find({
        "Username" : username
    })[0]["Password"]

    if bcrypt.checkpw(password.encode('utf8'), user_hashed_pw):
        return True
    else:
        return False

def getUserimages(username):
    # get the images
    return images.find({
        "Username": username,
    })[0]["images"]

def getUserDescriptions(username):
    # get the Descriptions
    return images.find({
        "Username": username,
    })[0]["Descriptions"]

def is_url_image(image_url):
    image_formats = ("image/png", "image/jpeg", "image/jpg")
    r = requests.head(image_url)
    if r.headers["content-type"] in image_formats:
        return True
    return False