# QA-SFIA2

[//]: # (Implicit Links Within Project)

[1]: https://docs.google.com/spreadsheets/d/1dMUbgEsOmRcXkmD-zshyu050ahH6E2spgOlQVY6_hMM/edit?usp=sharing   "Risk Assessment"
[3]: https://team-1579095236068.atlassian.net/jira/software/projects/QDA2/boards/5   "JIRA Project"



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

### Project Planning - Improving JIRA




### Source Code Management

The best way for me to correctly implement JIRA integration with my source code management software will be to declare the following assertions: 
- One task or subtask within JIRA requires creating a new feature branch.
- When that task has reached its definition of ‘done’, then we close the branch, merge with master, and then close that branch.


#### Project Management Tools & Project Management Assistance

When thinking about the CI pipeline, the thing that irritates me most about JIRA , is the integration with VCS. The fact that you need to know your issue’s tracking number is a subjective pain!

Tracking numbers in JIRA are non descriptive, and therefore for a developer to FIND that number, they have to load up the website, browse for the issue they are currently working on, and then take note of that number, tab back into the CLI, add this tracking number to your git commit message.

### Project Management Integrations

JIRA server is integrated into our IDE using Tools -> Tasks and Contexts.

Time Tracking system integrated into my IDE using the Jetbrains Time Tracker Plugin -> Integrates with PyCharm tasks. Will manually push to the corresponding JIRA issue. (Currently no way of automating this feature.)

Git is integrated into our IDE using Jetbrains VCS. It is also integrated into JIRA, allowing us to update our JIRA project status with the use of GitHub smart commits.
I have automated the process of creating smart commit messages. We take variables from our PyCharm task metadata, which subsequently drawn from our JIRA server.
 
 Each commit is structured as so: {id} - {summary} : #comment

I integrated Jenkins within PyCharm, because I am too 'DevOps' to have to keep tabbing out of my IDE in order check the build status of my current job.
With this, I faced a minor issue with compatibility between Jenkins2 and Jenkins JetBrains plugin. The fix was simple - Log in with an API token, and make sure to include our 'crumb token', in order to protect against CSRF exploitation.
  

Jenkins is configured to build the master branch of our repo with gitSCM web hook polling.

### Workflow

PyCharm will automatically search our JIRA server for ‘tasks’. The moment we assign ourself to one of these new tasks, pulled from our Project backlog, a number of things happen:

- When we open a new issue, we automatically create a new feature branch with Git. This branch is automatically named by JIRA.

When we open a new issue, our time tracker automatically starts ticking.

When we hit ‘commit’, PyCharm will automatically create a commit message based on the active project which was assigned to us by JIRA. This commit message will already be in the required format for smart commits, all we need to do is add our comment on the end.

The only things we I haven’t currently automated is the ‘in progress and done’ states for each task. 


## Project Brief



### Resources

- View my full risk assessment document [here.][1]
- View my JIRA Project [here.][3]

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
Pull from a .csv
Pull from a database
API call to an external API

Service #4
This service will also create an “Object” however this “Object” must be based upon the results of service #2 + #3 using some pre-defined rules.
Please see below for an example of how this logic can look.

The complexity of your logic here is up to you, again a simple implementation is allowed, however, may not showcase your full understanding of the technology.

## Project Approach
I choose to create a magic 8 ball using my service 1 as the data record page, service 2 creating a random question, service 3 creating a random answer, my service 4 takes the answers from service 1 and 2 and generates a random trueability depending on what has generated by the service 2 and 3.
I started the project by creating the home page first to generate some data on wehat i want it to do, from there i was able to build on the application.

## Project Management


## Project Architecture



### Database Structure
![alt text](https://github.com/knightscode94/QA-SFIA2/blob/master/docs/DB.png)


### CI Pipeline


#### My Jenkins Workflow

For my CI server in this project, I chose to use Jenkins.

Jenkins has official plugin support for docker swarm, and proved as a positive in my last QA-SFIA project. I am expecting to run into a few issues implementing jenkins as instead of it running one flask app its going to have 4 micro apps.


### Front End Development



## Testing




### Unit Testing

Unit testing of our services took longer to write than the actual MVP code...
...But that's okay, I was reading information, and this challenged me to think about TDD with a professional understanding.

#### Unit Testing Service #1

#### Unit Testing Service #2


#### Unit Testing Service #3


#### Unit Testing Service #4

### Functional Testing




## Project Review



### Known Issues and Future Optimisations



