# coding_challenge

### SETTINGS

execute the following command in the same directory where the docker-compose file is located:

`docker-compose build` and then `docker-compose up`

Use `docker ps` to get the ID of the running container and then use the `docker inspect {CONTAINER_ID}` command to obtain the IP address the container is using

### CHECK code correction

The Python community has formalized some recommended programming styles to help everyone write code in a common, agreed-upon style that makes the most sense for shared code. This style is captured in [PEP 8](https://peps.python.org/pep-0008/), the "Style Guide for Python Code". Pylint can be a quick and easy way of seeing if your code has captured the essence of [PEP 8](https://peps.python.org/pep-0008/) and is therefore friendly to other potential users.

Example check: `pylint app.py`

##  API Structure

**1** - The picture uploading tool: each user can upload one picture, provide a description. To register, each user must insert his/her username and password. For retriving the picture uploaded by the user, him/her must enter the username and password.
After the successful response, the page or API will show a thank you
message. Additional functionality for testing retrive img correspond to uploaded one: [base64-to-image-converter](https://codebeautify.org/base64-to-image-converter).
- [X] **Resource**: /test	**Parameters**: None **Method**: GET	**Status Codes**: 200  **Success Return**: Show successful response with img base64 code.
- [X] **Resource**: /register	**Parameters**: username - password **Method**: POST	**Status Codes**: 200 – OK _OR_ 301 – Invalid Username  **Success Return**: Successful response with code.
- [X] **Resource**: /load	**Parameters**: username - password - image - description	**Method**: POST	**Status Codes**: 200 – OK _OR_ 301 – Invalid Username _OR_ 302 - Invalid Password _OR_ 303 - Invalide path to Img **Success Return**: Successful response with 200 code.
- [X] **Resource**: /retrieve	**Parameters**: username - password **Method**: POST	**Status Codes**: 200 – OK _OR_ 301 – Invalid Username _OR_ 302 - Invalid Password  **Success Return**: successful response for retriving image, with status code and img base64 code.


P.S.
There are some controls that are missing, such as the fact that the description field exists once the load is called etc..., or to improve the control of the existence of the image you want to load, currently to load an image, you have to enter the image in the application's **webapp folder**. Use the test calls passed with the postman collection.


[Test.postman_collection.zip](https://github.com/smeneguz/coding_challenge/files/9052509/Test.postman_collection.zip)
