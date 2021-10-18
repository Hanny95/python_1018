import json

jsonText = '''
{
	"std00001":{
		"id":"std00001",
		"name":"hong gil dong",
		"mail":"gildong@gmail.com",
		"address":"korea seoul",
		"age":39,
		"hobbys":["sport", "music", "cook"],
		"active":true
	},
	"std00002":{
		"id":"std00002",
		"name":"park se ri",
		"mail":"seri@gmail.com",
		"address":"korea daejeon",
		"age":29,
		"hobbys":["music", "cook"],
		"active":false
	},
	"std00003":{
		"id":"std00003",
		"name":"son heungmin",
		"mail":"heungmin@gmail.com",
		"address":"korea jeju",
		"age":49,
		"hobbys":["music"],
		"active":true
	}
	
}
'''
# json 불러오기 (json.loads)
jsonData = json.loads(jsonText)
print(jsonData)

# 컴퓨터는 배열로 인식 --> 대괄호 사용
print(f'id : {jsonData["std00001"]["id"]}')
print(f'name : {jsonData["std00001"]["name"]}')
print(f'mail : {jsonData["std00001"]["mail"]}')
print(f'address : {jsonData["std00001"]["address"]}')
print(f'age : {jsonData["std00001"]["age"]}')
for idx, hobby in enumerate(jsonData["std00001"]["hobbys"]):
    print(f'idx : {idx} \t hobbys : {hobby}')
print(f'active : {jsonData["std00001"]["active"]}')
print('='*30)

print(f'id : {jsonData["std00002"]["id"]}')
print(f'name : {jsonData["std00002"]["name"]}')
print(f'mail : {jsonData["std00002"]["mail"]}')
print(f'address : {jsonData["std00002"]["address"]}')
print(f'age : {jsonData["std00002"]["age"]}')
for idx, hobby in enumerate(jsonData["std00002"]["hobbys"]):
    print(f'idx : {idx} \t hobbys : {hobby}')
print(f'active : {jsonData["std00002"]["active"]}')
print('='*30)

print(f'id : {jsonData["std00003"]["id"]}')
print(f'name : {jsonData["std00003"]["name"]}')
print(f'mail : {jsonData["std00003"]["mail"]}')
print(f'address : {jsonData["std00003"]["address"]}')
print(f'age : {jsonData["std00003"]["age"]}')
for idx, hobby in enumerate(jsonData["std00003"]["hobbys"]):
    print(f'idx : {idx} \t hobbys : {hobby}')
print(f'active : {jsonData["std00003"]["active"]}')
print('='*30)