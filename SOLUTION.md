# AVIV technical test solution

You can use this file to write down your assumptions and list the missing features or technical revamp that should
be achieved with your implementation.

## Notes

### Setup Project Steps
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
7. Add Price table and excute the .sql file through this command:
   1. cat ./db/02_add_listing_fixtures.sql | docker exec -i <container_id> psql -U listing -d listing


## Questions

This section contains additional questions your expected to answer before the debrief interview.

- **What is missing with your implementation to go to production?**
    With current implementation I can think of a few things that can be added before going live.
    1. A DELETE listing API is important for removing all the expired or unwanted listing. I have added that API as well.
    2. A boolean field for marking on expired listing can be added on listing creation and updates.
    3. Email field can be added when creating a listing and later used for promotional use like recommending listing via email
       to individual user.
  
- **How would you deploy your implementation?**  
  - Deployment of an implementation can vary depending on the technology stack and infrastructure. 
  Generally, for a Dockerized Flask REST API application, you can deploy it using a container 
  orchestration platform such as Kubernetes or Docker Swarm. You can also use a platform-as-a-service (PaaS) 
  provider like Heroku or AWS Elastic Beanstalk. Additionally, you can deploy the application to a virtual machine 
  or physical server using a continuous integration and continuous deployment (CI/CD) pipeline.

- **If you had to implement the same application from scratch, what would you do differently?**
  - If I had to implement the same application from scratch, I would focus on the following:
  1. Requirements gathering and analysis: I would make sure to gather and analyze the requirements of the application thoroughly before starting the implementation. 
  2. Design and architecture: I would spend more time on designing the architecture of the application and selecting the appropriate technology stack for the project. 
  3. Testing: I would implement automated testing for the application, including unit tests, integration tests, and end-to-end tests. 
  4. Documentation: I would document the implementation thoroughly to make it easier for other developers to understand the code and maintain the application.

- **The application aims at storing hundreds of thousands listings and millions of prices, and be accessed by millions
  of users every month. What should be anticipated and done to handle it?**
  - To handle the storage of hundreds of thousands of listings and millions of prices and the traffic from millions of users every month, several things should be anticipated and done:
  Scaling: The application should be designed with scalability in mind, and the infrastructure should be able to handle a significant increase in traffic and data storage. 
  Caching: Implementing a caching layer can help improve the performance of the application and reduce the load on the database. 
  Load testing: The application should be load tested to identify bottlenecks and optimize the performance of the application. 
  Database optimization: The database should be optimized to handle large volumes of data, including indexing and partitioning. 
  Monitoring and logging: The application should be monitored to identify issues and logged to track activity and troubleshoot issues. 
  Security: The application should be secured to protect against attacks, including implementing measures such as rate limiting and API key authentication.

    NB : You can update the [given architecture schema](./schemas/Aviv_Technical_Test_Architecture.drawio) by importing it
    on [diagrams.net](https://app.diagrams.net/) 
