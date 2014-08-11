import os
from flask import Flask, template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def hello():
    return render_template('template.html')

if __name__ == '__main__':
	app.run(port = 5000, debug=True)