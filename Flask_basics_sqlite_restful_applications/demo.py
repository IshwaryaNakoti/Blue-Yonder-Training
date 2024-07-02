from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
@app.route('/index')
def hello_world():
    #return "welcome to Flask by Jyothi shreyas"
    return render_template("index.html")




if __name__=='__main__':
    app.run(debug=True)