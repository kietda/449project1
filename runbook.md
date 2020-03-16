# Support Contacts

|        | Team           | Contact Info          	  | Runbook Review        |
|--------|----------------|---------------------------|-----------------------|
|   1	 | Developer      | kdang53@csu.fullerton.edu | Kiet Dang - 3/15/2020 |
|   2	 | Tester         | 		..		     	  | Chris.. - -/-/2020    |
|   3	 | Operator       | 		..	              | Arthur..  - -/-/2020  |


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
		>> to run microservice 1

# How to test (basic) the services:

Following these steps to install neccessary packages:
1. Install Requests:
pip3 install --user requests

Following these steps to test the services:
1. Open terminal in the project folder
2. Executing a linux command:
	python3 basictest_micro1.py
3. Executing a linux command:
	python3 basictest_micro2.py	

# How to open the database to test changes
1. Open terminal and execute a linux command to install package "sqlitebrowser"
	sudo apt-get install sqlitebrowser
2. In Tuffix windows, search and open the package named "DB  Browser for SQLite"
3. In the project folder, drag the file named "project1.db" to the window "DB  Browser for SQLite"
4. Check tables in database if neccessary


# System testing
...

# ...
