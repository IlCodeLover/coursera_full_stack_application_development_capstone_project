# Full Stack Application Development Capstone Project

[Full Stack Application Development Capstone Project
](https://www.coursera.org/learn/ibm-cloud-native-full-stack-development-capstone/home/info)

## Tech stack
![Tech stack](./images/Full_stack_tech_stack.png)

## Course objective
1. Module 1: 
   - Project scenario, forking, cloning, 
   - static web page
2. Module 2
   - Add user management (FE: React, JS, html), BE (Django); 
   - Add session management
3. Module 3: 
    - Create backend services in JavaScript, e.g: database/app.js
    - Build the Docker app 
    - Containerize MongoDB and Express server using docker-compose.yml
    - Deploy sentiment analyzer microservice using IBM Cloud Code Engine
4. Module 4
    - Create dynamic pages for details and reviews
    - Create user-friendly and aesthic front-end pages to provide it to users
5. Module 5
    - Implement CI/CD with Github workflow for linting
    - Make Epress-Mongo server running on Docket
    - Sentiment analyzer microservice
    - Make app available to run on a container
    - Add deploy artifacts to app so that it can be managed by Kubernetes (K8)
6. Module 6
   - Submission
   - peer grade review
   
## Project requirement
A national car dealership with local branches spread across the United States recently conducted a market survey. One of the suggestions that emerged from the survey was that customers would find it beneficial if they could access a central database of dealership reviews across the country.

You are a new hire at the company. You are assigned the task of building a website that allows new and existing customers to look up different branches by state and look at customer reviews of the various branches. Customers should be able to create an account and add their review for any of the branches. The management hopes this will bring transparency to the system and also increase the trust customers have in the dealership.

After thorough research and brainstorming, the team developed use cases for anonymous, authorized, and admin users.

### Use cases for anonymous users:
- View the Contact Us page.
- View the About Us page.
- View the list of dealerships.
- Filter the list of dealerships by state:
    - Select Show all or a specific state from the State dropdown on the dealership page.
    - View all states if nothing is selected in the dropdown.
    - View a table of dealerships for the selected state when the form is submitted.
- Click on a dealership to view the reviews for that dealership on the details page with each review displayed on a bootstrap card.
- Log in using their credentials.

### Use cases for authorized users:
In addition to the above, authorized users should be able to write a review for any dealership on the dealership's page. In order to enable authorized users to write their reviews:

- A Review button should be provided against each dealer listed in the dealership table.
- Clicking on the Review button should take the user to the review page.
- Filling the form on the review page and submitting it should add the review.
```python  
{
  "user_id": 1, => from Django
  "name": "Berkly Shepley", => from Django
  "dealership": 15, => from the form
  "review": "Total grid-enabled service-desk", => form textbox
  "time": "", => current time
  "purchase": true, => form checkbox
  "purchase_date": "07/11/2020", => form calendar (bootstrap)
  "car_make": "Audi", => from django dropdown
  "car_model": "A6", => from django dropdown
  "car_year": 2010 => form django dropdown
  }
```
On submission, the user should be taken back to the dealership detail page with the submitted review featured at the top of the reviews list, sorted on time.


### Use cases for admin users:
-  Log in to the admin site with a predefined username and password.
- Add new make, model, and other attributes.
  Your organization has assigned you as the Lead Full-Stack Software Developer on this project. Your job is to develop this portal as part of your Capstone project by following best practices for Full-Stack software development.


# Module 1: Create static page About us, Contact us
The Django app will be mainly used for user management and authentication, managing car models and makes, and routing other MongoDB services for dealership and customer reviews. You will build this Django app and related services in a phased manner along the capstone course.

In this module, you are asked to perform the following tasks:

- Fork the GitHub repo containing the project template.
- Clone your forked repository.
- Run the Django app on the development server.
- Add a navigation to the website using Bootstrap.
- Add an "About Us" static page.
- Add a "Contact Us" static page.
  Follow the instructional Skill Network lab to complete the above tasks step by step.

## Step 1: Clone and ckeck the main app running
As part of the project, your first task is to run and test its main Django application. You are given a skeleton of the Django application as a starting point.

### Fork and Clone the repository
- Navigate to this [repo](https://github.com/ibm-developer-skills-network/xrwvm-fullstack_developer_capstone): link and create a fork of the repository that includes essential starter code required for this project.

- Go to your forked repository.

- Copy the git clone URL of the skeleton repository that you forked into your account.
- Follow [instructions "Add static page"](./lectures/Module1_add_static_pages.pdf)
### Working with light-weight, serverless db: sqlite3

```sql
sqlite3 db.sqlite3 # connect to db
.table # list all tables
.exit # quit 
```
### Run the Django app on development server
![App running](./images/django_server.jpg)

# Module 2: User Management Overview
Now, you have the initial Django application built and deployed. In the next step, the admins of the dealership will review the app to identify users and manage their accesses based on roles (such as anonymous users or registered users). To accomplish this, you need to add authentication and authorization, that is, user management, to the app. In this lesson, you need to perform the following tasks to add the user management feature:

- Create a superuser for your app [Admin login](http://127.0.0.1:8000/admin/)
- Build the Client side and configure it.
- Check the Client configuration.
- Add a Login view to handle login requests.
- Add a Logout view to handle logout requests.
- Add a Registration view to handle Sign-up requests.

- Follow the [instructional lab](./lectures/) to complete the above tasks step by step.

## Set up Django env
Run the following to set up the django environment.
```
cd /home/project/xrwvm-fullstack_developer_capstone/server pip install virtualenv
virtualenv djangoenv
source djangoenv/bin/activate

python3 manage.py check
python3 manage.py makemigrations 
python3 manage.py migrate 

# stop the server if running
python3 manage.py createsuperuser # give name, password and any email (even not real one)

python3 manage.py runserver
```

3. Install the required packages by running the following command.
   python3 -m pip install -U -r requirements.txt

## Requirement to run npm command
### Install Node16 using nvm:
- Install [nvm](https://github.com/nvm-sh/nvm)
- Install node 16 that is compatible with Mac 11.3.1
- Create a simple [node web server](https://nodejs.org/docs/latest/api/synopsis.html#example)
```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
zsh: source ~/.zshrc # refress zsh file
nvm --version # check if nvm is installed
nvm ls-remote # fetch the list all node versions
nvm install <version-of-node-in-the-list>
node --version # check installed version
npm --version
nvm ls # give info of installed version on local
nvm use <version-want-to-use> # switch between different node versions

# create any folder to store your .js server
mkdir nodeDemo
cd nodeDemo
touch hello.js
ls
code hello.js # open .js in VS code 
# insert code 

const http = require('node:http');

const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
res.statusCode = 200;
res.setHeader('Content-Type', 'text/plain');
res.end('Hello, World!\n');
});

server.listen(port, hostname, () => {
console.log(`Server running at http://${hostname}:${port}/`);
});

###########################
node hello.js # to run server
```
#### Install Node: this way does not work for Mac 11.3.1.
```
brew install node
which npm # Example output: /usr/local/bin/npm
export PATH=$PATH:<node's bin path>
# e.g: export PATH=$PATH:/usr/local/bin
source ~/.bashrc
npm -v # check if the setting path is working
```

### Users
Some users are available. You can use some [free temporary email](https://10minutemail.com/)
- admin/admin

### How to build and run Node and Django
1. If there is change in FE --> build it again using npm
2. If there is change in model, Db --> migrate them
2. Then run Django app
```
cd <frontend folder where there is package.json>
npm run build
cd <project Djang folder where there is manage.py>
python3 manage.py check

python3 manage.py makemigrations
python3 manage.py migrate

python3 manage.py runserver
```
# Module 3
## Make Django app talk to MongoDB (NoSQL) using backend service developed in JavaScript
- Working with Mongoose to provide API endpoints
> Node app use *mongoose* to interact iwth the MongoDB
- We write backend services in an Express app and deploy it on IBM Code Engine.
- Students are provided 2 schema files: dealerships.js and reviews.js and their data in json files.
``` 
# review.js
const mongoose = require('mongoose');

const Schema = mongoose.Schema;

const reviews = new Schema({
	id: {
    type: Number,
    required: true,
	},
	name: {
    type: String,
    required: true
  },
  dealership: {
    type: Number,
    required: true,
  },
  review: {
    type: String,
    required: true
  },
  purchase: {
    type: Boolean,
    required: true
  },
  purchase_date: {
    type: String,
    required: true
  },
  car_make: {
    type: String,
    required: true
  },
  car_model: {
    type: String,
    required: true
  },
  car_year: {
    type: Number,
    required: true
  },
});

module.exports = mongoose.model('reviews', reviews);

``` 

And data records "reviews.json"
```
{
  "reviews": [
    {
      "id": 1,
      "name": "Berkly Shepley",
      "dealership": 15,
      "review": "Total grid-enabled service-desk",
      "purchase": true,
      "purchase_date": "07/11/2020",
      "car_make": "Audi",
      "car_model": "A6",
      "car_year": 2010
    },
    {
      "id": 2,
      "name": "Gwenora Zettoi",
      "dealership": 23,
      "review": "Future-proofed foreground capability",
      "purchase": true,
      "purchase_date": "09/17/2020",
      "car_make": "Pontiac",
      "car_model": "Firebird",
      "car_year": 1995
    },
  ...
  ]
}
```

- Build a docker app
```
docker ps -a / check all status containers
docker images // list images

docker volume ls // list volume
docker inspect <volumn-id> # check mounting 
 
docker build . -t nodeapp # create images for Node app
docker-compose up # create 2 containers for Mongo (download image from Docker hub) and Node app (from local images)

# after finishing your test, you should stop them
docker ps

# only stop the service (not delete)
docker stop <three-first-digit container id>

# remove all services
docker-compose down

# remove services and their volumes (persistent storage) of these service
docker-compose down --volumes
docker volume prune # delete anonymous volume auto created by Docker



# remove image
docker rmi <image_name> # remove image


```

Test all endpoints by replacing URLs in address bar
```
docker-compose up // to run Node app and MongoDB in containers
# alternative, to start server locally
node app.js

http://localhost:3030/ --> Welcome to the Mongoose API
http://localhost:27017/ --> It looks like you are trying to access MongoDB over HTTP on the native driver port.
http://localhost:3030/fetchReviews
http://localhost:3030/fetchReviews/dealer/15

curl http://localhost:3030/fetchReviews/dealer/15
curl http://localhost:3030/fetchDealers
curl http://localhost:3030/fetchDealer/3

```

### Re-Build and Restart services after changing code
```
# option 1 --> issue: existing container is not updated with new changes in app.js
docker-compose up --build # build and restart

# option 2: work ok, but not a good practice to fix image name
docker-compose down --volumes
docker rmi nodeapp
docker build . -t nodeapp
docker-compose up
docker-compose down --volumes

```

#### option 3 (RECOMMEND): modify docker-compose to build Node app
```
# modify docker-compose file
  api:
    #image: nodeapp # remove the prebuild image
    build: . # tell Docker to build the image for Node app before running the api service, ./ is the current dir where Dockerfile is
    ports:
      - 3030:3030
    depends_on: # depends_on ensures mongo_db container running first and then starts the api container.
      - mongo_db
      
Ctr + C: to stop all services running (if yes)

# rebuild nodeapp image (even thought it exists nodeapp:latest) because the code in app.js has changed
# output --> naming to docker.io/library/database-api
docker-compose build 
 

docker-compose up # it will use the new image it build "database-api" to start a service for Node app.
```

### Check data in MongoDb 
```
# start container for MongoDB
docker exec -it db_container mongosh # mongo_db
use dealershipsDB # connect to DB name <>
show collections
db.<table-name>.find().pretty()
```


## Module 3.2: Buid CarModel and CarMake models
```
python3 manage.py makemigrations
python3 manage.py migrate  # execute this when new/update models are created 
python manage.py runserver
# add CarMake, CarModel in model.py
# register carMake, CarModel in admin.py
python3 manage.py makemigrations
python3 manage.py migrate --run-syncdb # option --run-syncdb allow creating tables for apps WITHOUT migrations

# build client frontend
cd ../frontend
npm install # to install packages in package.json
npm run build 

# create djangoap/views, urls to fetch CarMake, CarModel
# create sample data in populate.py, function initialize()

# generating data by executing initialize() on the terminal via python shell
python3 manage.py shell
>>>from djangoapp.populate import initiate
>>>initiate()

# go to http://127.0.0.1:8000/admin --> login --> see sample data
 
```
## Module 3.3: Create Django Proxy Services of Backend APIs
- Finished tasks
  - create container/service for MongDB to store external data: reviews, and dealers
  - create container/service to host express API end points (from Django app)
  - create CarModel, CarMake
- TO DO:
  - ingerate those models and services to manage all entities: dealers and reviews
  - user sends a request to fetch reviews/dealers --> Express API endpoints (Django app) --> result returns in Dj views (can be seen as proxy services because it plays a role "middle man" btw a browser and a server.


```
###########################################################
# Environment setup 
###########################################################
cd <folder with docker-compose file>
docker-compose build
docker-compose up # at this point, there are 2 serives running: mongo and nodeapp

# backend url: http://localhost:3030
# add that "backend url" in djangoap/.env
# backend_url = http://localhost:3030 (without the slash / at the end

# Open another terminal
cd <folder containg manage.py>
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver

###########################################################
# Task: Create function to interact with backend in djangoapp/restapi.py
###########################################################
def get_request(endpoint, **kwargs):
    ...
###########################################################  
# Task: Deploy sentiment analysis on Code Engine as a mircroservice
# I create images of sentimen analysis in Docker-compose so that i can run it locally withou IBM App Engine
###########################################################
  # Sentiment analyzer
    # Sentiment Analyzer service
  sentiment_service:
    build:
      context: ../djangoapp/microservices # Path to the folder containing the sentiment Dockerfile
      dockerfile: Dockerfile # Name of the Dockerfile for the sentiment analyzer
    ports:
      - 3031:3031
###########################################################
# Task: create Django views to get entities dealder, reviews
###########################################################
# see restapis.py, views.py, urls.py


```


## Build image for sentiment analyzer
```
docker build . -t senti_analyzer

# docker run image and mapping <browser's port><container's port>
docker run -p 3031:3031 <image-name>
curl http://localhost:3031 # on your host machine
curl http://localhost:3031/analyze/The%20product%20is%20amazing%20and%20highly%20recommended
#--> {"sentiment": "positive"}%  
```

### Update all images into one Docker-compose
```
cd <folder with docker-compose>
docker-compose up --build
```
## Deploy sentiment analysis on Code Engine as a mircroservice
```
### create a code engine project. After a project is created, click on Code Engine CLI
name:       Code Engine - sn-labs-ilcodelover  
ID:         ccde0e11-6dbe-4683-a9e1-c8c87962b727  
Subdomain:  1q2yzhoqdo1j  
Domain:     us-south.codeengine.appdomain.cloud  
Region:     us-south

Kubernetes Config:    
Context:               1q2yzhoqdo1j  
Environment Variable:  export KUBECONFIG="/home/theia/.bluemix/plugins/code-engine/Code En

SN_ICR_NAMESPACE = sn-labs-ilcodelover

### build image for sentiment analyzer ; push it on IBM cloud container registry and deploy it on app engine IBM (using code engine CLI)
ibmcloud ce project current
cd <folder contain Docker image of sentiment analyzer
docker build . -t us.icr.io/${SN_ICR_NAMESPACE}/senti_analyzer
docker push us.icr.io/${SN_ICR_NAMESPACE}/senti_analyzer
ibmcloud ce application create --name sentianalyzer --image us.icr.io/${SN_ICR_NAMESPACE}/senti_analyzer --registry-secret icr-secret --port 5000
ibmcloud ce application delete --name sentianalyzer


### check if the image is public or not
ibmcloud cr image-inspect us.icr.io/${SN_ICR_NAMESPACE}/senti_analyzer

Run 'ibmcloud ce application get -n sentianalyzer' to check the application status.
OK

```
1. sentiment: https://sentianalyzer.1q7comj3m8s7.us-south.codeengine.appdomain.cloud
2. frontend djangoapp: https://ilcodelover-8000.theiadockernext-1-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai/dealer/2
3. backend nodeapp Express: https://ilcodelover-3030.theiadockernext-1-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai"
4. MongoDB: 

### Run your lab
```
# Start microservices: MongoDB, Node app, Sentiment analyzer
cd <folder with docker-compose>
docker-compose build
docker-compose up

# Step 2: populate data in MongoDB (if there is no existing data/ you deleted the volumn of db)
python3 manage.py shell
>>>from djangoapp.populate import initiate
>>>initiate()

# Step 3: Start your Djangoapp
cd <folder containg manage.py>
python3 manage.py check # check if there is any error 
python3 manage.py makemigrations # create migration files
python3 manage.py migrate # apply migration files to create tables in DB
python3 manage.py runserver # start Django app

# Step 4: Test some of endpoints:
#curl http://localhost:3030/fetchReviews/dealer/28 # test only backend Node app 
# curl http://127.0.0.1:8000/djangoapp/reviews/dealer/28 # test the Django app
```

# Module 4: Create dynamic pages for details and reviews
* Prerequisites: 
  - Django app running
  - Node app running
  - Sentiment analyzer running
  - MongoDB running
  - CarMake, CarModel, Dealer, Review data in DB
  - Backend service with Express-MongoDB should be running on one of the terminals.

```
###########################################################
# Task1: Add and set up React components fro Dealers page
###########################################################
# modify frontend/src/App.js to add Dealers component
# modify djangoproj/urls.py and add the routes for Dealers in it
# rebuild frontend app via npm (whenever any changes in frontend)
cd <frontend folder>
npm install
npm run build

# start the backend Django app (can do it after/before starting FE, the BK will restarted if FB is changed

###########################################################
# Task2: Add REACT components Dealer showing reviews (by clicking on hyperlink under Dealer Name
###########################################################
<Route path="/dealer/:id" element={<Dealer />} />
path('dealer/<int:dealer_id>/', TemplateView.as_view(template_name="index.html"))

###########################################################
# Task 3: Create a dealer details or review page
###########################################################
# components/Dealers/PostReview.jsx

# Task 4: add postreview 
```
Sample http://127.0.0.1:8000/dealers/ ( index.html is loaded as entry point, then is routed to React components http://127.0.0.1:8000/djangoapp/get_dealers)
![get_dealers](./images/djangoapp_get_dealers.png)
Sample http://127.0.0.1:8000/djangoapp/dealer/9
![dealer/id](./images/djangoapp_dealer_id.png)

# Module 5: CI/CD overview

## Install Flake8 to check Python coding convention
```python
pip install flake8
```

- Open Setting --> search Flake8 --> enable it, and enable Notification
- On VS Code/IntelliJ: You will see the hightlights (red, yellow) on the top right small window. 
- On IntelliJ, select Problem panel. On Project Errors, select Inspect Code. This code analysis show different errors than running flake8 command. I don't know the reason!

```
# Check the standard for a specific file
cd <folder-contain-file.py>
flake8 file.py

# Check the standard flake for a folder
cd <folder-need-to-validate>
flake8

```

We can also create a .flake8 config file at the project root folder and explicitly define our rules. I stored this file at this path: project\server\
```
[flake8]
ignore = E203, E266, W503
# max-line-length = 88
exclude = .git, __pycache__, build, dist, migrations, venv
max-complexity = 10
select = B,C,E,F,W,T4,B9
format = default
```

## Install jshint to check javascript coding convention
```
# open terminal and install jshint globally
npm install -g jshint
export PATH=$PATH:$(npm bin -g)
source ~/.zshrc

# check standard 
jshint <name of folder or .>
```


## Github action workflow
Set up CI/CD pipeline for the Django app using GitHub Actions.
- go to github --> select Action
- creete a new workflow 
- add code file in .github/workflows/main.yml

Whenever there is commit or PR, the workflow will run.
## Containerize & Deploy to Kubernetes
In line with the latest trends in technology and to avoid vendor lock-in, your management team is looking to deploy the dealership application to multiple clouds. The application is currently running on Code Engine, but you have been told not all cloud providers have a hosted Code Engine service. You are put in charge to look at containers as a possible way to mitigate this problem as all the big cloud providers have a way to host and manage containers. When containerizing an application, the process includes packaging an application with its relevant environment variables, configuration files, libraries, and software dependencies. The result is a container image that can then be run on a container platform.  You are also asked to use Kubernetes to manage the containerized deployment. Kubernetes is an open-source container orchestration platform that automates the deployment, management, and scaling of applications.


In this module you will:
- Add the ability to your application to run in a container
- Add deployment artifacts for your application so it can be managed by Kubernetes
- The management is interested in using the hybrid cloud strategy, where some applications and services reside on a private cloud and others on a public cloud. So, Kubernestes is a solution. 

# Module 6: 
# Reference
1. [CSS syntax explained](https://www.wa4e.com/code/css/)
2. 