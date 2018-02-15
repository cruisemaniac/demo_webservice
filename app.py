# app.py

# Import packages / modules
from flask import Flask
from flask import render_template
from flask import request, redirect

# Init flask
app = Flask(__name__)

# COnfigs
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Routes

allTasks = []

# Home page
@app.route('/')
def index():
	return render_template('index.html', t = allTasks)

# Create a new task
@app.route('/task', methods=['POST'])
def tasks():
	allTasks.append(request.form['task'])
	return redirect('/', 302)
	
# Read a specific task
@app.route('/task/<id>', methods=['GET'])
def getTask(id):
	return id

# Update a task
@app.route('/updatetask/<id>', methods=['POST'])
def updateTask(id):
	return id

# Delete a task
@app.route('/deletetask/<taskname>', methods=['GET'])
def deleteTask(taskname):
	allTasks.remove(taskname)
	return redirect('/', 302)

if __name__ == '__main__':
	app.run(debug=True)