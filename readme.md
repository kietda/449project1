# Overview

This is the project we’re going to build services for a web application
similar to reddit.

For this project you will build two microservices for specific functionality of this site and two automation test suites for these services.

# SERVICES
# POSTING MICROSERVICE
Each post should have a title, text, a community (subreddit), an optional URL linking to a resource (e.g. a news article or picture), a username, and a date the post was made.
The following operations should be exposed:
•	Create a new post
•	Delete an existing post
•	Retrieve an existing post
•	List the n most recent posts to a particular community
•	List the n most recent posts to any community
When retrieving lists of posts, do not include the text or resource URL for the post.
# USER ACCOUNT MICROSERVICE
Each user who registers should have the following data associated with them:
•	Username
•	Email
•	Karma
The following operations will be exposed:
•	Create user
•	Update email
•	Increment Karma
•	Decrement Karma
•	Deactivate account
The data for the user can be in the same database or different database as the other services.
