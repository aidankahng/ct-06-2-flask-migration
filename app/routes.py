from flask import request, render_template
from app import app
from datetime import datetime
from app.models import Task

tasks = [{
    'id' : 1,
    'title' : 'Get a job',
    'description' : 'I need to get a job or I will be broke',
    'completed' : False,
    'createdAt' : 'Tue, 26 Mar 2024 15:07:06 GMT"'
},
{
    'id' : 2,
    'title' : 'Get a good night of sleep',
    'description' : 'Sleep is good for the mind, and the body',
    'completed' : False,
    'createdAt' : 'Tue, 26 Mar 2024 15:07:06 GMT"'
}]

##################TESTING###########
@app.route('/create-task', methods=['POST'])
def create_task():
    if not request.is_json:
        return {'error' : 'Content not a JSON'}, 400
    
    data = request.json
    # check to make sure the data is valid
    required_keys = ["title", "description"]
    missing_keys = []
    for key in required_keys:
        if key not in data:
            missing_keys.append(key)
    if missing_keys:
        return {"error" : f"Keys: {', '.join(missing_keys)} are missing from request"}, 400
    
    title = data.get('title')
    description = data.get('description')
    completed = data.get('completed', False)
    createdAt = data.get('createdAt', datetime.now())

    new_task = {
        "id" : len(tasks) + 1,
        "title" : title,
        "description" : description,
        "completed" : completed,
        "createdAt" : createdAt
    }
    tasks.append(new_task)
    Task(title, description, completed)

    return new_task, 201
#####################################


@app.route("/")
def display_homepage():
    return render_template("index.html")


@app.route('/tasks')
def get_tasks():
    t = tasks
    return t

@app.route('/tasks', methods=['POST'])
def add_task():
    if not request.is_json:
        return {'error' : 'Content not a JSON'}, 400
    
    data = request.json
    # check to make sure the data is valid
    required_keys = ["title", "description"]
    missing_keys = []
    for key in required_keys:
        if key not in data:
            missing_keys.append(key)
    if missing_keys:
        return {"error" : f"Keys: {', '.join(missing_keys)} are missing from request"}, 400
    
    title = data.get('title')
    description = data.get('description')
    completed = data.get('completed', False)
    createdAt = data.get('createdAt', datetime.now())

    new_task = {
        "id" : len(tasks) + 1,
        "title" : title,
        "description" : description,
        "completed" : completed,
        "createdAt" : createdAt
    }
    tasks.append(new_task)

    return new_task, 201


@app.route('/tasks/<task_id>')
def get_task(task_id):
    t = tasks
    for task in t:
        if task['id'] == int(task_id):
            return task
    return {'error' : f'Unable to find task of id: {task_id}'}, 404