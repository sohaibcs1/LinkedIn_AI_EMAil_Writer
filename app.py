from flask import Flask,redirect,flash,request, render_template,url_for,abort,json,send_from_directory
import urllib.request
import json
from flask import Markup
import pandas as pd
import warnings
warnings.filterwarnings("ignore")    

from linkedin_api import Linkedin

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('index.html')

@app.errorhandler(500)
def internal_error(error):
    return render_template('index.html')

def data(usrname):
    api=Linkedin('sohaib.cs1@gmail.com','12Sohaib')
    contact = api.get_profile_contact_info('billy-g')
    profile = api.get_profile(str(usrname))
    formatedProfile = json.dumps(profile, indent=2)
    firstName=profile['firstName']
    lastname=profile['lastName']
    headline=profile['headline']
    return formatedProfile,firstName,lastname,headline,contact

@app.route('/scrap')
def scrap():
	return render_template('index.html')

@app.route('/scrap',methods=['GET','POST'])
def scr():
    if request.method == 'POST':
        username = request.form['Linkusername']
        if username == '' or username==None:
            return render_template('index.html')
        else:
            formatedProfile,firstName,lastname,headline,contact = data(username)
            email_tem=Markup('Hey '+firstName+" "+lastname+',\n\n'+'Wow, we are happy that you are '+headline+'. You have great analytical and problem-solving skills. We noticed that your overall performance is excellent and you are a productive employee of your organization. you also have strong management and leadership qualities.\n\nWanted to reach out because we are working with some folks and I believe this would match up well to what you are currently doing.\n\nCheck out the following to learn a bit more:\n\n'+firstName+" "+lastname)
            return render_template('index.html',formatedProfile=formatedProfile,email_tem=email_tem,firstName=firstName,lastname=lastname,headline=headline,contact=contact)
          
if __name__ =='__main__':
    app.run()
    # app.run(host='127.0.0.1')
