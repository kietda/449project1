import requests

print('POST MICRSOSERVICE')
print('Create new post:')
apost = {"title":"Socimedia","text":"Reddit ran wild with Boston bombing conspiracy theories in 2013","community":"Technology", "url":"https://www.theverge.com/tech/2020/2/26/21153525/firefox-dns-encryption-amazon-go-browsing-shopping-privacy","username":"tester1"}
resp = requests.post('http://localhost:5000/todo/api/v1.0/posts', json=apost)
if resp.status_code != 201:
    print(' Fail! Status code: {}'.format(resp.status_code))
else:
    print(' Passed! Status code:{}'.format(resp.status_code))

print('Delete an existing post:')    
resp = requests.delete('http://localhost:5000/todo/api/v1.0/posts/2')
if resp.status_code != 200:
    print(' Failed! Status code: {}'.format(resp.status_code))
else:
    print(' Passed! Status code:{}'.format(resp.status_code))

print('Retrieve an existing post:')    
resp = requests.get('http://localhost:5000/todo/api/v1.0/posts/3')
if resp.status_code != 200:
    print(' Failed! Status code: {}'.format(resp.status_code))
else:
    print(' Passed! Status code:{}'.format(resp.status_code))
    
print('List the n most recent posts to a particular community:')    
resp = requests.get('http://localhost:5000/todo/api/v1.0/posts/recent/Technology/3')
if resp.status_code != 200:
    print(' Failed! Status code: {}'.format(resp.status_code))
else:
    print(' Passed! Status code:{}'.format(resp.status_code))
    
print('List the n most recent posts to any community:')    
resp = requests.get('http://localhost:5000/todo/api/v1.0/posts/recent/6')
if resp.status_code != 200:
    print(' Failed! Status code: {}'.format(resp.status_code))
else:
    print(' Passed! Status code:{}'.format(resp.status_code))    


