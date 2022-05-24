import requests
import json
def get_function(id = 3):
   dt = json.dumps({'id':id})
   res = requests.get(url='http://127.0.0.1:8000/api/',data=dt)
   print(res.json())

#get_function()

def post_function(id = None):
   dt = json.dumps({
       'name':'Suman  Khanal',
       'address':'thali',
       'email':"sumarajkhanal@gmail.com",
       'desc':"lorem",
       'schoolname':"GGIC",
       'subjectname':"BIT",
       'skills':"django",
       'project':"chatbot"
       })
   res = requests.post(url='http://127.0.0.1:8000/api/',data=dt)
   print(res.json())

#post_function()

def put_function():
   dt = json.dumps({
       'id':3,
       'name':'Sujan Raj',
       'address':'123@gmail.com',
       'email':"lorem",
       'desc':"lorem",
       'schoolname':"lorem",
       'subjectname':"lorem",
       'skills':"lorem",
       'project':"lorem"
       })
   res = requests.put(url='http://127.0.0.1:8000/api/',data=dt)
   print(res.json())

#put_function()

def delete_function():
   dt = json.dumps({'id':2})
   res = requests.delete(url='http://127.0.0.1:8000/api/',data=dt)
   print(res.json())

#delete_function()
