from flask import Flask,render_template,redirect,url_for

app = Flask(__name__)

@app.route('/',methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/form',methods = ['GET','POST'])
def form():
    return render_template('form.html')




if __name__ == '__main__':
    app.run(debug = True)

