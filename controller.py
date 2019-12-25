from flask import Flask, render_template, request, session, redirect
import model

app = Flask(__name__)
app.secret_key='Jabu is a cool boi'

@app.route("/home", methods=['GET', 'POST'])
def home():
	if request.method == 'GET':
		return render_template("home.html")

	else:
		submittedAnime = request.form['anime']
		if (model.isValidStatusCode(submittedAnime)):
			session['submittedAnime'] = submittedAnime
			return redirect('/anime')
		else:
			return redirect('/invalid')


@app.route("/anime")
def default():
	submittedAnime = session.get('submittedAnime', None)
	results = model.getAnimeInfo(submittedAnime)

	return render_template("anime.html", anime=submittedAnime, results=results)


@app.route("/invalid")
def invalid():
	return render_template("invalid.html")

if __name__ == "__main__":
	app.run(debug=True)
