# coding_challenge

### SETTINGS

execute the following command in the same directory where the docker-compose file is located:

`docker-compose up --build`

Use `docker ps` to get the ID of the running container and then use the `docker inspect {CONTAINER_ID}` command to obtain the IP address the container is using

##  API Structure

**1** - The Polling tool: users can open the page or get a list via API, see the
question and list of answers, choose one. After the successful response, the
page or the API will show a thank you message.
- [X] **Resource**: /retrieve	**Parameters**: None	**Method**: GET	**Status Codes**: 200 – OK  **Success Return**: List of all question and aswer
- [X] **Resource**: /answer	**Parameters**: None	**Method**: POST	**Status Codes**: 200 – OK _OR_ 303 – Invalid Message  **Success Return**: After the successful response, the page or the API will show a thank you message.


**2** - The Feedback form: the user can open the page or send an API request,
provide his feedback title, and summary. After the successful response, the
page or API will show a thank you message. Additional page or API exists to
get a list of submitted feedbacks.

**3** - The picture uploading tool: users can upload pictures, provide descriptions.
After the successful response, the page or API will show a thank you
message. Additional functionality for listing all uploaded pictures and
downloading selected picture also present.
