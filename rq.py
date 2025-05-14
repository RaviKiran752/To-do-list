import requests

# Add
res = requests.post("http://127.0.0.1:8000/todos", json={"name": "Read", "desc": "Python FastAPI docs"})
print(res.json())

print(requests.get("http://127.0.0.1:8000/todos").json())

# Update
requests.put("http://127.0.0.1:8000/todos/1", json={"name": "Read more", "desc": "More docs"})

# Delete
requests.delete("http://127.0.0.1:8000/todos/delete/2")

print(requests.get("http://127.0.0.1:8000/todos").json())

print(requests.delete("http://127.0.0.1:8000/todos/delete/3").json())