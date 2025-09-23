from flask import Flask,render_template

app = Flask(__name__)

@app.route('/',methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/form',methods = ['GET','POST'])
def form():
    return render_template('form.html')


# @app.route('/<name>')
# def print_name(name):
#     return 'Hello, {}'.format(name)

if __name__ == '__main__':
    app.run(debug = True)