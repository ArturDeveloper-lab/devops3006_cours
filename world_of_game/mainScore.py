from flask import Flask

from guessGame import play

app = Flask("Game")
totalScore = play()

@app.route('/')
def win_point():
    return "<html>" \
           "<head>" \
           "<title>Scores Game</title>" \
           "</head>" \
           "<body>" \
           f"<h1>The score is <div id='score'>{totalScore}</div></h1>" \
                                           "</body>" \
                                           "</html>"


app.run(host="0.0.0.0", port=5001, debug=False)
