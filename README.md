# QA-SFIA2

[//]: # (Implicit Links Within Project)

## Contents
- [Pre-Project Reflection](#pre-project-reflection)
- [Project Brief](#project-brief)
  - [Resources](#resources)
  - [Requirements](#requirements)
- [Project Approach](#project-approach)
- [Project Architecture](#project-architecture)
  - [Database Structure](#database-structure)
  - [CI Pipeline](#ci-pipeline)
  - [Front End Development](#front-end-development)
- [Testing](#testing)
 - [Unit Testing](#unit-testing)
 - [Functional Testing](#functional-testing)
- [Project Management](#project-management)
- [Project Review](#project-review)
  - [Known Issues and Future Optimisation](#known-issues-and-future-optimisations)


## Pre-Project Reflection

after the disapointment of not doing well in my frist project as it wasnt origional I am a bit concerned how well I will get on with this new task, I know my project was like the flask blog but there were differences even though it used similar code.

#### Issue Estimation

Im expecting to have issues turning my project into a flask application and turning it into a docker container, I have struggled to understand the implemtation of docker and swarm and need to do more research and have better practice.

#### A Smarter Approach
I wanted to make a project that was fairly simple that included some data analysis but die to lack of experience and having issues running working code I wrote my code in a way I knew would work and looked to develop on that. I will continue to keep things basic to produce something that works until I am confident enough to make something complex.

### Requirements
Using a flask, MYQSL, Docker compose the plan is to create a flask app with 4 services. 
Service #1
The core service – this will render the Jinja2 templates you need to interact with your application, it will also be responsible for communicating with the other 3 services, and finally for persisting some data in an SQL database.

Service #2 + #3
These will both generate a random “Object”, this object can be whatever you like as we encourage creativity in this project.

You can create the “Object” however you like, some methods will be more complex but therefore show a greater technical understanding and flexibility, examples of how you can generate your “Object” are:

Random number
Random letter
Pull an item from an Array
Pull from a database
API call to an external API

Service #4
This service will also create an “Object” however this “Object” must be based upon the results of service #2 + #3 using some pre-defined rules.
Please see below for an example of how this logic can look.

The complexity of your logic here is up to you, again a simple implementation is allowed, however, may not showcase your full understanding of the technology.

## Project Approach
I choose to create a magic 8 ball using my service 1 as the data record page, service 2 creating a random question, service 3 creating a random answer, my service 4 takes the answers from service 1 and 2 and generates a random trueability depending on what has generated by the service 2 and 3.
I started the project by creating the home page first to generate some data on wehat i want it to do, from there i was able to build on the application.

### Database Structure
![alt text](https://github.com/knightscode94/QA-SFIA2/blob/master/docs/DB.png)


#### My Jenkins Workflow

For my CI server in this project, I chose to use Jenkins.

Jenkins has official plugin support for docker swarm, and proved as a positive in my last QA-SFIA project. I am expecting to run into a few issues implementing jenkins as instead of it running one flask app its going to have 4 micro apps.


## Testing
service 1

![alt text](https://github.com/knightscode94/QA-SFIA2/blob/master/docs/S1.png)

service 2

![alt text](https://github.com/knightscode94/QA-SFIA2/blob/master/docs/S2.png)

Service 3

![alt text](https://github.com/knightscode94/QA-SFIA2/blob/master/docs/S3.png)

Service 4

![alt text](https://github.com/knightscode94/QA-SFIA2/blob/master/docs/S4.png)


## Project Review
although I have created a project with multiple services that interact with each other I have unfortunatley only managed to get my project to work using docker-compose, my tests dont run properly, I dont even know if my ansible is properly working, jenkins isnt set up properly, I have tried to do everything needed for this project but know I didnt manage to hit all the targets. My biggest struggle was the 4 services and getting them to run. I had to rewrite my project into something more basic and still struggled. I honestly thought choosing the 8ball application would be easy to set up but realised how difficult this challenge was when making into micro apps.


### Known Issues and Future Optimisations

1)tests run but doesnt properly work due to something with the database export.

2)jenkins doesnt run a sucessful build running docker 
+ docker build -t accountownerapp:B2 -f Dockerfile .
unable to prepare context: unable to evaluate symlinks in Dockerfile path: lstat /var/lib/jenkins/workspace/docker/Dockerfile: no such file or directory
[Pipeline] }
[Pipeline] // node
[Pipeline] End of Pipeline
ERROR: script returned exit code 1
Finished: FAILURE

3)ansible i added the code didnt even get a chance to run it so unsure if it works.

4) does not deploy replicas


