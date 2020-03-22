Steps:

1) Install Postman application to inspect url postman requests (aka "collections")
    https://www.postman.com

2) Install Docker
    https://docs.docker.com

3) Install Docker Compose
    https://docs.docker.com/compose/install

4) Create the database; docker will access the directory of project1.db
    $ python3 createdb.py

5) Open docker-compose.yml and change "volume" directory to where source files are located; additional information in the docker-compose.yml file.

Note: I configured docker to build the container image with ubuntu16.04, python3, and flask installed. Everything should automate on its own.

6) Execution and test with no load:
    $ docker-compose up

6.1) Test with load:
    $ docker-compose up --scale excess_test=<number of containers or "users">

7) Check docker compose logs
    $ docker-compose logs basic_test
    $ docker-compose logs bogus_test
    $ docker-compose logs neg_test

7.1) Save logs to file
    $ docker-compose logs --no-color basic_test > basic_test_log.txt
    $ docker-compose logs --no-color bogus_test > bogus_test_log.txt
    $ docker-compose logs --no-color neg_test > neg_test_log.txt

8) Restart and remove running containers
    $ docker-compose down


Note: To remove dangling docker image (name with "<none>")
    $ docker rmi $(docker images -q -f dangling=true)
