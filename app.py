from flask import Flask,  render_template
from boggle import Boggle

boggle_game = Boggle()

app = Flask(__name__)
app.config['SECRET_KEY'] = "sesstiontime"


app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


@app.route('/')
def home_page():
    return render_template("home.html", board=boggle_game.make_board())