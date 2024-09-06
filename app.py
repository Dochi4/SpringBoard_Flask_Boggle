from flask import Flask, render_template, request , session, jsonify
from boggle import Boggle

boggle_game = Boggle()

app = Flask(__name__)
app.config['SECRET_KEY'] = "sesstiontime"


app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


@app.route('/', methods=["GET", "POST"])
def home_page():
    current_board = boggle_game.make_board()
    session['current_board'] = current_board  
    session['score'] = 0
    
    return render_template("home.html", board=current_board)

@app.route('/check-word', methods=['POST'])

def check_word():
    word = request.json.get('word')  
    current_board = session.get('current_board')  
    result = boggle_game.check_valid_word(current_board, word)

    if result == 'ok':
        return jsonify({'result': 'ok'}) 
    elif result == 'not-on-board':
        return jsonify({'result': 'not-on-board'})
    else:
        return jsonify({'result': 'not-a-word'})
    
@app.route('/update-score', methods=['POST'])
def update_score():
    result = request.json.get('result')
    if result == 'ok':
        session['score'] += 1
    else:
        session['score'] += 0

    return jsonify({'score': session['score']})