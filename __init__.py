from flask import Flask, render_template
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == "__main__":
	app.run(debug=True)
