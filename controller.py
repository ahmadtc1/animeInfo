from flask import Flask, render_template, request, session, redirect
import model

app = Flask(__name__)
app.secret_key='Jabu is a cool boi'

@app.route("/", methods=["GET"])
def default():
	return redirect('/home')



@app.route("/home", methods=["GET", "POST"])
def home():
	if (request.method == 'GET'):
		return render_template("home.html")

	if (request.method == 'POST'):
		if ('animeSearch' in request.form):
			return redirect('/animesearch')

		elif ('genreSearch' in request.form):
			return redirect('/invalid')

@app.route("/animesearch", methods=["GET", "POST"])
def animeSearch():
	if request.method == 'GET':
		return render_template("animesearch.html", animeImage="ylia2.jpg")

	else:
		submittedAnime = request.form['anime']
		if (model.isValidStatusCode(submittedAnime)):
			session['submittedAnime'] = submittedAnime
			return redirect('/anime')
		else:
			return redirect('/invalid')

@app.route("/anime")
def anime():
	submittedAnime = session.get('submittedAnime', None)
	results = model.getAnimeInfo(submittedAnime)

	return render_template("anime.html", anime=submittedAnime, results=results)


@app.route("/invalid")
def invalid():
	return render_template("invalid.html")

if __name__ == "__main__":
	app.run(debug=True)
