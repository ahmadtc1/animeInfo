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

	elif (request.method == 'POST'):
		if ('animeSearch' in request.form):
			return redirect('/animesearch')

		elif ('genreSearch' in request.form):
			return redirect('/genresearch')

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

@app.route("/genresearch", methods=["GET", "POST"])
def genreSearch():
	if (request.method == "GET"):
		return render_template("genresearch.html")

	elif (request.method == "POST"):
		genre = request.form["genre"].lower()
		if (model.isValidGenreStatusCode(genre)):
			session["genre"] = genre
			return redirect('/genre')

@app.route("/anime")
def anime():
	submittedAnime = session.get('submittedAnime', None)
	results = model.getAnimeInfo(submittedAnime)

	return render_template("anime.html", anime=submittedAnime, results=results)

@app.route("/genre")
def genre():
	genre = session.get("genre")
	results = model.getAnimeGenreInfo(genre)
	
	return render_template("genre.html", genre=genre, results=results)

@app.route("/invalid")
def invalid():
	return render_template("invalid.html")

if __name__ == "__main__":
	app.run(debug=True)
