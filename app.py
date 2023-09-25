from flask import Flask #module flask importing a class called Flask

app = Flask(__name__) #creating a flask application and giving it a name

#creating a route
#@ is a decorator, provided by librarires to provide some advanced functionalities
@app.route("/")
def hello_world():
    return "Hello me"

"""
When the script is run, __name__ is set to "__main__" in that script.
When the script is imported as a module into another script, __name__ is set to the script's name 
(i.e., the name of the Python file without the .py extension).
"""
if __name__  == "__main__": #running as a module or a standalone script
    app.run(host='0.0.0.0', debug=True)#This line runs the Flask development server, which listens for incoming HTTP requests on a port (by default, port 5000). It's only executed if the script is being run directly.


