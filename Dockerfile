#use python image as the base image
FROM python:3.9-slim-buster

#set the working directory in the container
WORKDIR /app

#copy the requirement file to the working directory
COPY  requirements.txt .

# install python required python packages
#This flag instructs pip not to use cached packages when installing, which can be
#useful to ensure that you always get the latest packages
RUN pip3 install --no-cache-dir -r requirements.txt

#copy application code to the working directory
COPY . . 

#set the environment variables for the flask app
ENV FLASK_RUN_HOST=0.0.0.0

#expose the app running port
EXPOSE 5000

# start the Flask app when the container is run
CMD ["flask", "run"]