# AVIV technical test solution

You can use this file to write down your assumptions and list the missing features or technical revamp that should
be achieved with your implementation.

## Notes

Write here notes about your implementation choices and assumptions.

## Setup Project - Task Done
1. Github
   1. Create a new github repo AVIV.
   2. Intialize the project with "git init".
   3. Add project to github repo with commands:
      1. git remote add origin https://github.com/hatimali/aviv.git
      2. git remote -v
      3. git push --set-upstream origin master
   4. Add credentials to config: " git config --global credential.helper store"
   5. Checkout a dev branch from maser for all the dev work and master is all the base project
2. Virtual Environment
   1. Create a virtual environment (env) : "python3 -m venv env"
   2. Activate virtual environment: "source env/bin/activate"
3. Add requirments.txt with "pip freeze > requirements.txt"
4. Install requirments: pip3 install -r requirements.txt
5. Docker Steps:
   1. Run docker-compose up
      1. If docker-compose not installed then run "sudo apt install docker-compose"
   2. docker-compose build
   3. docker-compose-up (if error for db Cannot start service db):
      1. sudo service postgresql stop
      2. Run "docker-compose up" again (This time project runs)
   4. Run project on http://127.0.0.1:8080/listings
6. Install all the required packages in a virtual environment through pip for successfully running TestUpdateListing
7. 


## Questions

This section contains additional questions your expected to answer before the debrief interview.

- **What is missing with your implementation to go to production?**

- **How would you deploy your implementation?**
  - We can deploy our code with quite a few platform,but I would prefer to use Heroku here.
  - 

- **If you had to implement the same application from scratch, what would you do differently?**
  - 

- **The application aims at storing hundreds of thousands listings and millions of prices, and be accessed by millions
  of users every month. What should be anticipated and done to handle it?**

  NB : You can update the [given architecture schema](./schemas/Aviv_Technical_Test_Architecture.drawio) by importing it
  on [diagrams.net](https://app.diagrams.net/) 
