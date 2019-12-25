from flask import Flask, render_template, request, session
import model

app = Flask(__name__)

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


@app.route("/anime")
def default():
	submittedAnime = session.get('anime', None)
	result = model.getAnimeInfo(submittedAnime)

	return render_template("anime.html", anime=submittedAnime, result=result)


if __name__ == "__main__":
	app.run(debug=True)
