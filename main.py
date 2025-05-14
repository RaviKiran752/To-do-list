from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from fastapi import HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

api=FastAPI()
api.mount('/static',StaticFiles(directory="static"),name="static")
templates=Jinja2Templates(directory="templates")


class ToDoIn(BaseModel):
    name: str
    desc: str
"""todos=[
    {'id':1, 'name':'something','desc':'do nothing'},
    {'id':2, 'name':'something2','desc':'do nothing once'},
    {'id':3, 'name':'something3','desc':'do nothing 3'},
    {'id':4, 'name':'something4','desc':'do nothing 4'},
    {'id':5, 'name':'something5','desc':'do nothing 5'},

]"""
todos=[]
# GET, POST, PUT, DELETE
@api.get("/",response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html",{"request":request})
@api.get('/')
def index():
    return {"Message": "Hello World"}

@api.get('/todos/{id}')# path parameter
def get_todo(id: int):
    for todo in todos:
        if todo['id']==id:
            return {'result':todo}
    raise HTTPException(status_code=404,detail="Todo not found")

@api.get('/todos')
def get_todos(first_n: Optional[int]=None):#query parameter /todos?first_no=__
    if first_n is not None:
        return todos[:first_n]
    
    return todos
    
@api.post('/todos')
def create_todo(todo: ToDoIn):
    new_todo_id=max(t['id'] for t in todos)+1 if todos else 1
    new_todo={
        "id":new_todo_id,
        "name":todo.name,
        "desc":todo.desc
    }
    todos.append(new_todo)
    return new_todo

@api.put('/todos/{id}')
def update_todo(id: int,  updated_todo: ToDoIn):
    for todo in todos:
        if todo['id']==id:
            todo['name']=updated_todo.name
            todo['desc']=updated_todo.desc
            return {"Message":"Todo updated","todo":todo}
    raise HTTPException(status_code=404,detail="Todo not found")

@api.delete('/todos/{id}')
def delete_todo(id: int):
    for i, todo in enumerate(todos):
        if todo['id'] == id:
            deleted = todos.pop(i)
            return {"message": "Todo deleted", "deleted": deleted}
    raise HTTPException(status_code=404, detail="Todo not found")
