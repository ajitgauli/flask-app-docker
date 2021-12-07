## **My Flask App**
This app provides `/` endpoint for request methods `GET` and `POST`.
For `GET /` it returns an html message unless a header `Accept: appliction/json` is provided in which case it formats the response to JSON.<br/><br/>


### **Installation**
 - [Download Docker](https://docs.docker.com/get-docker/)
 - Unzip the source code for this project and navigate into the directory.<br/><br/>

### **Running Service**

From within the project directory run service either in dev or prod mode as described below.
 - For Dev mode, log level is set to DEBUG.
  
      `docker-compose up app_dev`

 - For Prod mode, log level is set to INFO.
  
      `docker-compose up app_prod`

- Once any of the above command runs successfully, the API is accessible on  `localhost:8080/` and the app logs are written to stdout and to a log file at /var/log/app.log inside the docker container.<br/><br/>

### **Testing API**
Once the service is up and running, we can test the response using the following curl commands.

    curl localhost:8080/

should return 

    <p>Hello, World</p>
---
    curl localhost:8080/ --header "Accept: application/json"

should return 

    {"message":"Hello, World"}
---
    curl -X POST localhost:8080/ -H "content-type: application/json" -d "{ \"foo\": \"bar\"}"

should return 

    {"foo":"bar"}
<br/>

### **Running Unit Tests**
I'm using pytest for testing. Use the following command to run tests.

`docker-compose up pytest`

<br/>

### **Running Pylint**
I'm using pylint for linting. Use the following command to run linting.

`docker-compose up pylint`
