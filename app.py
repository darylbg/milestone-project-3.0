import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextField, IntegerField, DateField
from wtforms.validators import InputRequired, Length, AnyOf

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'milestone_project_3'
app.config["MONGO_URI"] = 'mongodb+srv://daryl:puertorico123@cluster0-zqj1t.mongodb.net/milestone_project_3?retryWrites=true&w=majority'
app.config["SECRET_KEY"] = 'thisisasecret'


mongo = PyMongo(app)

@app.route('/')

@app.route('/index')
def index():
    return render_template("featuredcamps.html", camps=mongo.db.camps.find())

@app.route('/get_camps')
def get_camps():
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
    return render_template('editcamp.html', camp=the_camp)

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
        'camp_featured':request.form.get('camp_featured'),
        'camp_img':request.form.get('camp_img')
    })
    return redirect(url_for('get_camps'))

@app.route('/delete_camp/<camp_id>')
def delete_camp(camp_id):
    mongo.db.camps.remove({'_id': ObjectId(camp_id)})
    return redirect(url_for('get_camps'))

class ApplyForm(FlaskForm):
    first_name = TextField('First Name', validators=[InputRequired(), Length(max=12, message='max 12 characters')], id=['full_name'])
    last_name = TextField('Last Name', validators=[InputRequired(), Length(max=12, message='max 12 characters')], id=['full_name'])
    email = TextField('Email', validators=[InputRequired(), Length(max=20, message='max 20 characters')], id=['email'])
    phone = TextField('Phone number', validators=[InputRequired(), Length(max=15, message='max 20 numbers')], id=['phone'])
    date_arrive = TextField('Date arrive', validators=[InputRequired()])
    date_leave = TextField('Date leave', validators=[InputRequired()])

@app.route('/apply_form', methods=['GET', 'POST'])
def apply_form():

    form = ApplyForm()

    if form.validate_on_submit():
        return '<h3>The form has been submitted!</h3>'

    return render_template('applyform.html', form=form, camp=mongo.db.camps.find_one())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)
