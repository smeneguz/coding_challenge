import bcrypt
from app import users
"""
HELPER FUNCTIONS
"""

def userExist(username):
    exist = True
    if users.find({"Username": username}).count() == 0:
        notExist = False
    return notExist

def verifyUsers(username, password):
    if not userExist(username):
        return False

    user_hashed_pw = users.find({
        "Username" : username
    })[0]["Password"]

    if bcrypt.checkpw(password.encode('utf8', user_hashed_pw)):
        return True
    else:
        return False

def getUserMessages(username):
    # get the messages
    return user.find({
        "Username": username,
    })[0]["Messages"]