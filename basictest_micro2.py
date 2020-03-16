import requests

print('USER MICRSOSERVICE')
print('Create a user:')
auser = {"username":"tester99","email":"tester3@gmail.com","karma":0}
resp = requests.post('http://localhost:5100/todo/api/v1.0/users', json=auser)
if resp.status_code != 201:
    print(' Fail! Status code: {}'.format(resp.status_code))
else:
    print(' Passed! Status code:{}'.format(resp.status_code))

print('Update email:')
update_from_user = {"email":"tester3_update@gmail.com","username":"tester3"}
resp = requests.put('http://localhost:5100/todo/api/v1.0/users', json=update_from_user)
if resp.status_code != 200:
    print(' Failed! Status code: {}'.format(resp.status_code))
else:
    print(' Passed! Status code:{}'.format(resp.status_code))

print('Increment Karma:')    
increase_karma = {"username":"tester3"}
resp = requests.put('http://localhost:5100/todo/api/v1.0/users/inckarma', json=increase_karma)
if resp.status_code != 200:
    print(' Failed! Status code: {}'.format(resp.status_code))
else:
    print(' Passed! Status code:{}'.format(resp.status_code))
    
print('Decrement Karma:')    
increase_karma = {"username":"tester3"}
resp = requests.put('http://localhost:5100/todo/api/v1.0/users/deckarma', json=increase_karma)
if resp.status_code != 200:
    print(' Failed! Status code: {}'.format(resp.status_code))
else:
    print(' Passed! Status code:{}'.format(resp.status_code))

print('Deactivate account:')    
deactive_username = {"username":"tester3"}
resp = requests.put('http://localhost:5100/todo/api/v1.0/users/deactivate', json=deactive_username)
if resp.status_code != 200:
    print(' Failed! Status code: {}'.format(resp.status_code))
else:
    print(' Passed! Status code:{}'.format(resp.status_code))
