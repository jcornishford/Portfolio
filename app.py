import jinja2
from flask import Flask, render_template
import os


# Main class obstantiated
app = Flask(__name__) 
app.jinja_loader = jinja2.FileSystemLoader('/home/ubuntu/workspace/work/website/templates')


#Routes bound to website pages
@app.route('/') 
def index():
    return render_template('index.html') 

@app.route('/contact') 
def contact():
    return render_template('contact.html')
    
@app.route('/projects')
def projects():
    return render_template('projects.html')

 
@app.route('/testimonials')
def customer_testimonials():
    return render_template('testimonials.html')


#This either runs the program as a standalone or a module
if __name__ == '__main__':
    app.run(debug = True,host=os.getenv('IP','0.0.0.0'), port=int(os.getenv('PORT', 8080)))
    '''Will not run on cloud 9 without these parameters passed in'''
    #Debugger should output that the file is not working
   
    
