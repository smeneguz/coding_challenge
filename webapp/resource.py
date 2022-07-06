"""
RESOURCES
"""
import base64
from flask_restful import Api, Resource
import os
import helper
import bcrypt
from flask import jsonify, request
import json


class Test(Resource):
    def get(self):
        with open("test.jpeg", "rb") as image2string:
            converted_string = base64.b64encode(image2string.read())
        print(converted_string)
  
        with open('encode.bin', "wb") as file:
            file.write(converted_string)

            retJson = {
                "status": 200,
                "description": "Test",
                "image": str(converted_string)
            }

        return jsonify(retJson)

class Register(Resource):
    def post(self):
        # Get data from request
        data = request.get_json()

        # Get data
        username = data["username"]
        password = data["password"]

        # check existence user
        if helper.userExist(username):
            retJson = {
                "status": 301,  
                "description": "Invalid Username",
            }
            return jsonify(retJson)

        # encrypt password
        hashed_pw = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

        # Insert
        helper.images.insert_one({
            "Username": username,
            "Password": hashed_pw,
            "images": [],
            "Descriptions": []
        })

        retJson = {
            "status": 200,
            "msg": "Registration successful"
        }
        return jsonify(retJson)

class RetrieveImg(Resource):
    def post(self):
        data = request.get_json()

        # Get data
        username = data["username"]
        password = data["password"]

        # check user existance
        if not helper.userExist(username):
            retJson = {
                "status": 301,
                "description": "Invalid Username",
            }
            return jsonify(retJson)
        
        # check psw
        correct_pw = helper.verifyUsers(username, password)
        if not correct_pw:
            retJson = {
                "status": 302,
                "description": "Invalid Password",
            }
            return jsonify(retJson)
        
        # get the images
        images = helper.getUserimages(username)

        # Successful response 
        retJson = {
            "status": 200,
            "obj": str(images),
            "description": helper.getUserDescriptions(username)
        }
        return jsonify(retJson)


class Load(Resource):
    def post(self):
        # Get data from request
        data = request.get_json()

        # Get data
        username = data["username"]
        password = data["password"]
        image = data["image"]
        description = data["description"]

        # check user existance
        if not helper.userExist(username):
            retJson = {
                "status": 301,
                "description": "Invalid Username",
            }
            return jsonify(retJson)
        
        # check psw
        correct_pw = helper.verifyUsers(username, password)
        if not correct_pw:
            retJson = {
                "status": 302,
                "description": "Invalid Password",
            }
            return jsonify(retJson)

        if not image or not os.path.exists(image):
            retJson = {
                "status": 303,
                "description": "Invalide path to Img",
            }
            return jsonify(retJson)

        # get the images && Descriptions
        imgs = helper.getUserimages(username)

        descr = helper.getUserDescriptions(username)

        # take image string from path
        with open(image, "rb") as image2string:
            converted_string = base64.b64encode(image2string.read())
        print(converted_string)
  
        with open('encode.bin', "wb") as file:
            file.write(converted_string)

        # add new image and description
        imgs.append(converted_string)
        descr.append(description)

        helper.images.update_many({
            "Username": username
        }, {
            "$set": {
                "images": imgs,
                "Descriptions": description
            }
        })

        retJson = {
            "status": 200,
            "msg": "image has been loaded successfully"
        }
        
        return jsonify(retJson)





