import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextField, IntegerField, DateField, BooleanField
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
    form = EditForm()
    form.validate_on_submit()
    return render_template("addcamp.html", form=form)

@app.route('/insert_camp', methods=['POST'])
def insert_camp():
    camps = mongo.db.camps
    camps.insert_one(request.form.to_dict())
    return redirect(url_for('get_camps'))

class EditForm(FlaskForm):
    camp_title = TextField('Camp title', validators=[InputRequired()], id='camp_title', _name='camp_title')
    camp_img = TextField('Camp image', validators=[InputRequired()], id='camp_img', _name='camp_img')
    camp_state = SelectField('Select camp state', validators=[InputRequired()], id='camp_state', _name='camp_state', choices=[('',''), ('Alabama', 'Alabama'), ('Alaska', 'Alaska'), ('Arizona', 'Arizona'), ('Arkansas', 'Arkansas'),
    ('California', 'California'), ('Colorado', 'Colorado'), ('Connecticut', 'Connecticut'), ('Delaware', 'Delaware'), ('Florida', 'Florida'), ('Georgia', 'Georgia'), ('Hawaii', 'Hawaii'), ('Idaho', 'Idaho'), ('Illanois', 'Illanois'), ('Indiana', 'Indiana'),
     ('Iowa', 'Iowa'), ('Kansas', 'Kansas'), ('Kentucky', 'Kentucky'), ('Louisiana', 'Louisiana'), ('Maine', 'Maine'), ('Maryland', 'Maryland'), ('Massachusetts', 'Massachusetts'), ('Michigan', 'Michigan'), ('Minnesota', 'Minnesota'), ('Mississippi', 'Mississippi'), ('Missouri', 'Missouri'),
     ('Montana', 'Montana'), ('Nebraska', 'Nebraska'), ('Nevada', 'Nevada'), ('New Hampshire', 'New Hampshire'), ('New Jersey', 'New Jersey'), ('New Mexico', 'New Mexico'), ('New York', 'New York'), ('North Carolina', 'North Carolina'), ('Noth Dakota', 'Noth Dakota'), ('Ohio', 'Ohio'), ('Oklahoma', 'Oklahoma'),
     ('Oregon', 'Oregon'), ('Pennsylvania', 'Pennsylvania'), ('Rhode Island', 'Rhode Island'), ('South Carolina', 'South Carolina'), ('South Dakota', 'South Dakota'), ('Tennessee', 'Tennessee'), ('Texas', 'Texas'), ('Utah', 'Utah'), ('Vermont', 'Vermont'), ('Virginia', 'Virginia'), ('Washington', 'Washington'),
     ('West Virginia', 'West Virginia'), ('Wisconsin', 'Wisconsin'), ('Wyoming', 'Wyoming')])
    camp_address = TextField('Camp address', validators=[InputRequired()], id=['camp_address'], _name=['camp_address'])
    camp_availability = SelectField('Select availability', validators=[InputRequired()], id='camp_availability', _name='camp_availability', choices=[('', ''), ('Currently available', 'Currently available'), ('Available soon enquire futher', 'Available soon enquire futher'), ('Currently unavailable', 'Currently unavailable')])
    camp_description = TextField('Camp description', validators=[InputRequired()], id='camp_description', _name='camp_description')
    camp_featured = BooleanField('', id='camp_featured', _name='camp_featured')

@app.route('/edit_camp/<camp_id>')
def edit_camp(camp_id):
    the_camp = mongo.db.camps.find_one({"_id": ObjectId(camp_id)})
    form = EditForm()
    if form.validate_on_submit():
        return '<h1>successful</h1>'

    return render_template('editcamp.html', camp=the_camp, form=form)

@app.route('/update_camp/<camp_id>', methods=["GET", "POST"])
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

    return render_template('applyform.html', form=form)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)
