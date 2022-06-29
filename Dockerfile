FROM mongo:latest

# install Python 3
RUN apt-get update && apt-get install -y python3.9 python3.9-pip
RUN apt-get -y install python3.9-dev
RUN pip3 install pymongo

EXPOSE 27017