# app.py

# Import packages / modules
from flask import Flask
from flask import render_template
from flask import request, redirect
from datetime import datetime
import math

# Init flask
app = Flask(__name__)

# COnfigs
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Routes

allTasks = []

# Generate a random integer based on current time in UTC format
def IDgenerator():
	return math.floor((datetime.utcnow() - datetime(1970,1,1)).total_seconds())

# Home page
@app.route('/')
def index():
	return render_template('index.html', t = allTasks)

# Create a new task
@app.route('/task', methods=['POST'])
def tasks():
	new_task = {
		'id': IDgenerator(),
		'task': request.form['task'],
		'complete': False
	}
	allTasks.append(new_task)
	return redirect('/', 302)
	
# Read a specific task
@app.route('/task/<id>', methods=['GET'])
def getTask(id):
	return id

# Update a task
@app.route('/updatetask/<id>', methods=['GET', 'POST'])
def updateTask(id):
	if request.method == 'POST':
		return redirect('/', 302)

	if request.method == 'GET':
		return render_template('update.html', taskname = id)

# Delete a task
@app.route('/deletetask/<taskID>', methods=['GET'])
def deleteTask(taskID):
	
	# Iterate and remove the item acording to the id
	for theTask in allTasks:
		if int(taskID) == int(theTask['id']):
			allTasks.remove(theTask)

	# redirect to homepage
	return redirect('/', 302)

if __name__ == '__main__':
	app.run(debug=True)