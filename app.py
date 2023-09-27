from database import load_jobs_from_db, load_job_from_db

#module flask importing a class called Flask
from flask import Flask, render_template, jsonify

app = Flask(__name__) #creating a flask application and giving it a name


#creating a route
#@ is a decorator, provided by librarires to provide some advanced functionalities
jobs = load_jobs_from_db()
@app.route("/")
def hello_world():
    jobs = load_jobs_from_db()
    return render_template('home.html', jobs=jobs)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(jobs)

@app.route("/job/<id>")
def show_job(id):
    job = load_job_from_db(id)
    print("JOB is ", job)
    return jsonify(job)

"""
When the script is run, __name__ is set to "__main__" in that script.
When the script is imported as a module into another script, __name__ is set to the script's name 
(i.e., the name of the Python file without the .py extension).
"""
if __name__  == "__main__": #running as a module or a standalone script
    app.run(host='0.0.0.0', debug=True)#This line runs the Flask development server, which listens for incoming HTTP requests on a port (by default, port 5000). It's only executed if the script is being run directly.



