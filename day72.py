print ('hello world!')
import requests


resp = requests.get("http://www.google.com")
print (resp.text)
print (resp.ok)
print(resp.status_code)
print(resp.headers['content-type'])
print(resp.headers['date'])


print('what is github status?')
resp = requests.get('https://status.github.com/api/status.json')
git_status_json = resp.json()
print(git_status_json)

print("Github status is currently:" ,git_status_json['status'], 'as of' , git_status_json['last_updated'])
