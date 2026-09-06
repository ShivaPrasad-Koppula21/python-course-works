import json
with open ('data.json','r') as file:
    data=json.load(file)
data['username']='shiva'  
data['skills'].append('flask')   
with open ('data.json','w') as file:
    json.dump(data,file,indent=4)


student={'name':"shiva",'age':23,'course':'python'}
json=json.dumps(student)
print(json)
student=json.loads(json)
print(student)
print(type(student))