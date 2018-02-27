# app.py

# Import packages / modules
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime
import math

# Init flask
app = Flask(__name__)

# Configs
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:tosh@localhost/todo-py'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Init SQLAlchemy
db = SQLAlchemy(app)


# Models
class Task(db.Model):
	__tablename__ = 'tasks'
	idTask = db.Column('idTask', db.Integer, primary_key = True)
	task = db.Column('task', db.String)
	status = db.Column('status', db.String, default = 'uncomplete')
	creation_date = db.Column('creation_date', db.DateTime, default = datetime.utcnow())

	def __init__(self, task):
		self.task = task

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
	new_task = Task(request.form['task'])
	db.session.add(new_task)
	db.session.commit()
	return redirect('/', 302)
	
# Read a specific task
@app.route('/task/<id>', methods=['GET'])
def getTask(id):
	return id

# Update a task
@app.route('/updatetask/<taskID>', methods=['GET'])
def updateTask(taskID):
	displayTask = ""
	# Iterate the list to find the right task
	for theTask in allTasks:
		if int(taskID) == int(theTask['id']):
			displayTask = theTask

	return render_template('update.html', task = displayTask)

@app.route('/do_updatetask', methods=['POST'])
def do_updatetask():
	if request.method == 'POST':
		taskID = request.form['taskID']
		for theTask in allTasks:
			if int(taskID) == int(theTask['id']):
				theTask['task'] =  request.form['task']
		return redirect('/', 302)

# Delete a task
@app.route('/deletetask/<taskID>', methods=['GET'])
def deleteTask(taskID):
	
	# Iterate and remove the item acording to the id
	for theTask in allTasks:
		if int(taskID) == int(theTask['id']):
			allTasks.remove(theTask)

	# redirect to homepage
	return redirect('/', 302)

@app.route('/complete/<taskID>')
def complete(taskID):

	# Iterate to find that requested task
	for theTask in allTasks:
		if int(taskID) == int(theTask['id']):
			theTask['complete'] = True

	# Redirect to the homepage
	return redirect('/', 302)

@app.route('/uncomplete/<taskID>')
def uncomplete(taskID):

	# Iterate to find that requested task
	for theTask in allTasks:
		if int(taskID) == int(theTask['id']):
			theTask['complete'] = False

	# Redirect to the homepage
	return redirect('/', 302)

if __name__ == '__main__':
	app.run(debug=True)