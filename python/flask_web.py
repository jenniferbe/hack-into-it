from flask import Flask
from flask import request
from flask import render_template
from query_data import query

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])

def hello_world():
	if request.method == 'POST':
		return render_template('posts.html', name=None)
	return render_template('index.html', name=None)


@app.route('/about')
def about():
    return 'Our webapp aims to provide advice to people who are expecting a baby. The advice given is based on previous user experiences.'


if __name__ == '__main__':
    app.run()