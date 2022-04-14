from flask import Flask
app=Flask(__name__)
@app.route("/")
def hello():
    s="<body bgcolor='green' text='yellow'><h1> I am Flask </h1>"
    return s
if __name__=='__main__':
app.run(debug=True)    

