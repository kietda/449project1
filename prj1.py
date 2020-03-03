#designing a web application with python and flask

from flask import Flask, jsonify, request
from flask import abort, make_response
import sqlite3
    
app = Flask(__name__)
app.config["DEBUG"] = True

#let the connection object know to use the dict_factory function, which
#return items from the database as dictionaries rather than lists
#=> these work better when we output them to JSON
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/')
def index():
    return "Hello everyone accessing our project 1!"

#delete later
@app.route('/todo/api/v1.0/posts', methods = ['GET'])
def get_posts():
    conn = sqlite3.connect('project1.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_posts = cur.execute('SELECT * FROM posts;').fetchall()
    return jsonify(all_posts)    
    #return jsonify({'posts': posts})

#since a web service client applications will expect that we always
#respond with JSON, so we need to improve our 404 error handler
# @app.errorhandler(404)
# def not_found(error):
#     return make_response(jsonify({'error:':'Not found'}), 404)

#create a new post
@app.route('/todo/api/v1.0/posts',methods=['POST'])
def create_post():
    if not request.json or not 'title' in request.json \
        or not 'text' in request.json \
        or not 'community' in request.json \
        or not 'username' in request.json \
        or not 'date' in request.json:        
        abort(400)
    
    #get the lastet id
    conn = sqlite3.connect('project1.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    results = cur.execute('SELECT * FROM posts WHERE id=(SELECT MAX(id) FROM posts);').fetchall()
    if len(results)==0:
        nextid = "1"
    else:
        nextid = str(int(results[0]['id']) + 1)
    # return jsonify({'result':post_id}),200
    pid = request.json.get('id',"")
    if pid == "":
        pid = nextid
    else:
        to_filter = []
        to_filter.append(pid)
        results = cur.execute("SELECT * FROM posts WHERE id=?;",to_filter).fetchall()
        if len(results)!=0:
            abort(409)        
    ptitle = request.json['title']
    ptext = request.json['text']
    pcommunity =request.json['community']
    purl = request.json.get('url',"")
    pusername = request.json['username']
    pdate = request.json['date']
    query = "INSERT INTO posts (id, title, text, community, url, username, date) VALUES (?,?,?,?,?,?,?);"
    to_filter2 = []
    to_filter2.append(pid)
    to_filter2.append(ptitle)
    to_filter2.append(ptext)
    to_filter2.append(pcommunity)
    to_filter2.append(purl)
    to_filter2.append(pusername)
    to_filter2.append(pdate)    
    # results = cur.execute(query, (pid, ptitle, ptext, pcommunity, purl, pusername, pdate))
    results = cur.execute(query, to_filter2)
    conn.commit()
    # if len(results)==0:
    #     abort(404)
    return jsonify({'post':True}),201
    
    
    # post = {
    #     'id': posts[-1]['id'] + 1,
    #     'title':request.json['title'],
    #     'text':request.json['text'],
    #     'community':request.json['community'],
    #     'url':request.json.get('url',""),
    #     'username':request.json['username'],
    #     'date':request.json['date']
    # }
    # posts.append(post)
    # return jsonify({'post':post}),201

#delete an existing post
@app.route('/todo/api/v1.0/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    conn = sqlite3.connect('project1.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()    
    to_filter = []
    to_filter.append(post_id)
    query = "SELECT * FROM posts WHERE id=?;"
    results = cur.execute(query, to_filter).fetchall()
    if len(results)==0:
        abort(404)     
    query = "DELETE FROM posts WHERE id=?;"
    cur.execute(query,to_filter).fetchall()
    conn.commit()
    return jsonify({'result':True}),200

#Retrieve an existing post
@app.route('/todo/api/v1.0/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    conn = sqlite3.connect('project1.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    query = "SELECT * FROM posts WHERE id=?;"
    to_filter = []
    to_filter.append(post_id)
    results = cur.execute(query, to_filter).fetchall()
    if len(results)==0:
        abort(404)
    return jsonify(results),200

#List the n most recent posts to a particular community
@app.route('/todo/api/v1.0/posts/recent/<community_name>/<posts_amount>', methods=['GET'])
def get_community_recent_post(community_name, posts_amount):
    # community_name = request.args.get('community_name');
    # posts_amount = request.args.get('posts_amount');
    # com_name = community_name
    # pos_amount = posts_amount
    
    # pcommunity =request.json['community']
    # purl = request.json.get('url',"")
    conn = sqlite3.connect('project1.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    query = "SELECT * FROM posts WHERE community=? ORDER BY id DESC limit ?;"
    to_filter = []
    to_filter.append(community_name)
    to_filter.append(posts_amount)
    results = cur.execute(query, to_filter).fetchall()
    if len(results)==0:
        abort(404)
    return jsonify(results),200

#List the n most recent posts to any community
@app.route('/todo/api/v1.0/posts/recent/<posts_amount>', methods=['GET'])
def get_any_recent_post(posts_amount):
    conn = sqlite3.connect('project1.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    query = "SELECT * FROM posts ORDER BY id DESC limit ?;"
    to_filter = []
    to_filter.append(posts_amount)
    results = cur.execute(query, to_filter).fetchall()
    if len(results)==0:
        abort(404)
    return jsonify(results),200

if __name__ == '__main__':
    app.run(debug=True)