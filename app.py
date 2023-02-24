from flask import Flask                         # import flask
app = Flask(__name__)                           # create an app instance
 
@app.route("/")                                 # at the end point /
def welcome():                                  # call method welcome
    return "Cloud Yolculuguna Hosgeldiniz !"    #returns "hello world"
@app.route("/<name>")                           # at the end point /<name>
def welcome_name(name):                         # call method hello_name
    return "Hosgeldin "+ name                   # which returns "hello + name
if __name__ == "__main__":                      # on running python app.py
    app.run(host='0.0.0.0', port=8080)          # change host and port of application
    app.run()    
