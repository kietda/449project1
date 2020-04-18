# Support Contacts

|        | Team           | Contact Info          	  			| Runbook Review        		|
|--------|----------------|-------------------------------------|-------------------------------|
|   1	 | Development      | kdang53@csu.fullerton.edu 			| Kiet Dang - 3/15/2020 		|
|   2	 | Testing          | christian.angeles@csu.fullerton.edu | Christian Angeles - 3/28/2020 |
|   3	 | Operations       | art2015@csu.fullerton.edu 	  | Arthur Salazar - 3/29/2020  		|


# Overview

This is the project we’re going to build services for a web application
similar to reddit.

# How to run the services:

The test environment for this project in this course is a Tuffix VM with
Python 3.6.7

Following these steps to install neccessary packages:
1. Install python:
sudo apt-get install python3
2. Install pip3:
sudo apt install python3-pip
3. Install flask:
pip3 install flask

Following these steps to start the services:
1. Open terminal in the project folder
2. Executing a linux command:
	python3 createdb.py
		>> to create new database named "project1.db"
3. Executing a linux command:
	python3 micro1.py
		>> to run microservice 1
4. Open another terminal
4. Executing a linux command:
	python3 micro2.py
		>> to run microservice 2

# How to open the database to test changes
1. Open terminal and execute the linux command to install package "sqlitebrowser"
	sudo apt-get install sqlitebrowser
2. In Tuffix windows, search and open the package named "DB  Browser for SQLite"
3. In the project folder, drag the file named "project1.db" to the window "DB  Browser for SQLite"
4. Check tables in database if neccessary


# Test micro services (Tuffix 2019 Edition r2)
1. Open a terminal to install docker and docker compose
2. Install Docker (steps from https://medium.com/@Grigorkh/how-to-install-docker-on-ubuntu-19-04-7ccfeda5935)
	- $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
	- $ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable edge test"
	- $ sudo apt-get install docker-ce
3. Install Docker Compose (steps from https://www.osradar.com/how-to-install-latest-docker-compose-on-ubuntu-19-04-centos-8-debian-10-fedora-30/)
	- $ sudo curl -s https://api.github.com/repos/docker/compose/releases/latest | grep browser_download_url | grep docker-compose-Linux-x86_64 | cut -d '"' -f 4 | wget -qi -
	- $ sudo chmod +x docker-compose-Linux-x86_64
	- $ sudo mv docker-compose-Linux-x86_64 /usr/local/bin/docker-compose
4. Locate docker-compose.yml in the project folder and open with a text editor. Under "volumes" for excess_test, basic_test, and bogus_neg_test enter the full path directory to where project files are located
	- If the project folder was extracted on the TuffixVM's desktop, then by default the volumes are set to "/home/student/Desktop/cpsc449project1"
5. Open a terminal and run the micro services
6. Open another terminal and change directory to the project folder
	- $ cd /home/student/Desktop/cpsc449project1
7. Test with no load
	- $ sudo docker-compose up
8. Test with load (TuffixVM might not be able to handle 100 containers at once; start with 10)
	- An example: --scale excess_test=<number of containers or "simulated users">
	- $ sudo docker-compose up --scale excess_test=10
9. Check docker compose logs
	- $ sudo docker-compose logs basic_test
	- $ sudo docker-compose logs bogus_neg_test
10. Stop and remove running containers
	- $ sudo docker-compose down

# Deployment and Operations
This was tested on Tuffix environment
# Installation for foreman, Gunicorn3 and Caddy1

1. install Gunicorn3
$ sudo apt install --yes gunicorn3

2. install foreman
sudo apt install ruby-foreman

3.installing Caddy1
$ curl https://getcaddy.com | bash -s personal
# Running the Procfile
Before make sure that both the Procfile and Caddyfile are in the same directory as the project folder

1. Always use this command for foreman to confirm the micro services are recognized
$ foreman check

2. to run the three instances for ever microservices (including caddy)
$ sudo foreman start -m posting=3,user=3,caddy=1

3.2 microservices will be access by:
http://localhost:2015/posts	(== http://localhost:5000)
http://localhost:2015/users	(== http://localhost:5000)
