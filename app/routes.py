from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Miguel'}
	posts = [
		{
			'author':{'username': 'John'},
			'body': 'Beautiful day in Rio!'
		},
		{
			'author':{'username':'Susan'},
			'body': 'The Avengers movie was so cool!'
		},
		{
			'author':{'username':'Pedro Almeida'},
			'body': 'Cadê meu linkedin'
		}
	]

	return render_template('index.html', user = user, posts = posts)