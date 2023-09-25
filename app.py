

#module flask importing a class called Flask
from flask import Flask, render_template, jsonify

app = Flask(__name__) #creating a flask application and giving it a name


JOBS = [
    {
        'id':1,
        'title': 'Data Analyst',
        'location': 'Dhaka, Bangladesh',
        'salary': '100000'

    },
    {
        'id': 2,
        'title': 'Jr. Data Analyst',
        'location': 'Dhaka, Bangladesh',
        'salary': '10000'

    },
    {
        'id': 3,
        'title': 'Data Scientist',
        'location': 'Dhaka, Bangladesh',
        #'salary': '144000'

    }

]
#creating a route
#@ is a decorator, provided by librarires to provide some advanced functionalities
@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)
"""
When the script is run, __name__ is set to "__main__" in that script.
When the script is imported as a module into another script, __name__ is set to the script's name 
(i.e., the name of the Python file without the .py extension).
"""
if __name__  == "__main__": #running as a module or a standalone script
    app.run(host='0.0.0.0', debug=True)#This line runs the Flask development server, which listens for incoming HTTP requests on a port (by default, port 5000). It's only executed if the script is being run directly.



