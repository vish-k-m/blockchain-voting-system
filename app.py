from flask import Flask, render_template, request
from voting_system import cast_vote, candidates

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", candidates=candidates)


@app.route("/vote", methods=["POST"])
def vote():
    voter = request.form["voter"]
    candidate = request.form["candidate"]

    result = cast_vote(voter, candidate)

    return result


if __name__ == "__main__":
    app.run(debug=True)
