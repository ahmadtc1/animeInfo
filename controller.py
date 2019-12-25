from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/home", methods=['GET', 'POST'])
def home():
	if request.method == 'GET':
		return render_template("home.html")

	else:
		submittedAnime = request.form['anime']
		return 


@app.route("/")
def default():
	return render_template("home.html")


if __name__ == "__main__":
	app.run(debug=True)
