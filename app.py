import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'milestone_project_3'
app.config["MONGO_URI"] = 'mongodb+srv://daryl:puertorico123@cluster0-zqj1t.mongodb.net/milestone_project_3?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/get_tasks')
def get_tasks():
    return render_template("tasks.html", tasks=mongo.db.tasks.find())

@app.route('/add_task')
def add_task():
    return render_template('addtask.html')

@app.route('/insert_task', methods=['POST'])
def insert_task():
    tasks = mongo.db.tasks
    tasks.insert_one(request.form.to_dict())
    return redirect(url_for('get_tasks'))

@app.route('/edit_task/<task_id>')
def edit_task(task_id):
    the_task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    return render_template('edittask.html', task=the_task)

@app.route('/update_task/<task_id>', methods=["POST"])
def update_task(task_id):
    tasks = mongo.db.tasks
    tasks.update( {'_id': ObjectId(task_id)},
    {
        'camp_title':request.form.get('camp_title'),
        'camp_state':request.form.get('camp_state'),
        'camp_address': request.form.get('camp_address'),
        'camp_availability': request.form.get('camp_availability'),
        'camp_description':request.form.get('camp_description')
    })
    return redirect(url_for('get_tasks'))

@app.route('/delete_task/<task_id>')
def delete_task(task_id):
    mongo.db.tasks.remove({'_id': ObjectId(task_id)})
    return redirect(url_for('get_tasks'))

@app.route('/apply_form')
def apply_form():
    return render_template('applyform.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)
