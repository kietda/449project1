# 449project1
Install python:
sudo apt-get install python3
Install flask:
pip install flask

Go to the project folder, open terminal
Run: python pr1j.py
Database:(id, title, text, community, url, username, date)
Create new post:
curl -i -H "Content-Type:application/json" -X POST -d '{"title":"firefox","text":"Firefox is showing the way back to a world that’s private by default","community":"Technology", "url":"https://www.theverge.com/tech/2020/2/26/21153525/firefox-dns-encryption-amazon-go-browsing-shopping-privacy","username":"test1","date":"2020/03/01"}' http://localhost:5000/todo/api/v1.0/posts
Delete an existing post:
curl -X DELETE http://localhost:5000/todo/api/v1.0/posts/1
Retrieve an existing post
curl -i http://localhost:5000/todo/api/v1.0/posts/1

Not finished:
List the n most recent posts to a particular community
List the n most recent posts to any community

