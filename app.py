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
    return render_template("featuredcamps.html", camps=mongo.db.camps.find())

@app.route('/get_camps')
def get_camps():
    return render_template("camps.html", page='get_camps', camps=mongo.db.camps.find())
    return render_template("camps.html", page='get_camps', camps=mongo.db.camps.find())

@app.route('/add_camp')
def add_camp():
    return render_template("addcamp.html",)

@app.route('/insert_camp', methods=['POST'])
def insert_camp():
    camps = mongo.db.camps
    camps.insert_one(request.form.to_dict())
    return redirect(url_for('get_camps'))

@app.route('/edit_camp/<camp_id>')
def edit_camp(camp_id):
    the_camp = mongo.db.camps.find_one({"_id": ObjectId(camp_id)})
    return render_template('editcamp.html', camp=the_camp,)

@app.route('/update_camp/<camp_id>', methods=["POST"])
def update_camp(camp_id):
    camps = mongo.db.camps
    camps.update( {'_id': ObjectId(camp_id)},
    {
        'camp_title':request.form.get('camp_title'),
        'camp_state':request.form.get('camp_state'),
        'camp_address': request.form.get('camp_address'),
        'camp_availability': request.form.get('camp_availability'),
        'camp_description':request.form.get('camp_description'),
        'camp_featured':request.form.get('camp_featured')
    })
    return redirect(url_for('get_camps'))

@app.route('/delete_camp/<camp_id>')
def delete_camp(camp_id):
    mongo.db.camps.remove({'_id': ObjectId(camp_id)})
    return redirect(url_for('get_camps'))

@app.route('/apply_form')
def apply_form():
    return render_template('applyform.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)
