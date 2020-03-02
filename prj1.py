#designing a web application with python and flask

from flask import Flask, jsonify, request
from flask import abort, make_response

app = Flask(__name__)

posts = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'text': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'community': u'Sales',
        'url':u'http://walmart.com',
        'username':u'tester1',
        'date':u'03/01/2020'
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'text': u'Need to find a good Python tutorial on the web', 
        'community': u'Technology',
        'url':u'https://miro.medium.com/max/768/1*CrK1VuTTMSg-zL9-z3ohQQ.png',
        'username':u'tester2',
        'date':u'03/02/2020'
    }
]

@app.route('/')
def index():
    return "Hello everyone accessing our project 1!"

#delete later
@app.route('/todo/api/v1.0/posts', methods = ['GET'])
def get_posts():
    return jsonify({'posts': posts})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error:':'Not found'}), 404)

#create a new post
@app.route('/todo/api/v1.0/posts',methods=['POST'])
def create_post():
    if not request.json or not 'title' in request.json \
        or not 'text' in request.json \
        or not 'community' in request.json \
        or not 'username' in request.json \
        or not 'date' in request.json:        
        abort(400)
    post = {
        'id': posts[-1]['id'] + 1,
        'title':request.json['title'],
        'text':request.json['text'],
        'community':request.json['community'],
        'url':request.json.get('url',""),
        'username':request.json['username'],
        'date':request.json['date']
    }
    posts.append(post)
    return jsonify({'post':post}),201

#delete an existing post
@app.route('/todo/api/v1.0/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = [post for post in posts if post['id'] == post_id]
    if len(post)==0:
        abort(404)
    posts.remove(post[0])
    return jsonify({'result':True})

#Retrieve an existing post
@app.route('/todo/api/v1.0/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post =[post for post in posts if post['id'] == post_id]
    if len(post)==0:
        abort(404)
    return jsonify({'post': post[0]})



if __name__ == '__main__':
    app.run(debug=True)