from flask import Flask, render_template, url_for, redirect, request
import mukvnd_sudoku

app = Flask(__name__)
app.config['SERVER_NAME'] = '127.0.0.1:5000'

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/unsolved')
def unsolved():
    return render_template("unsolved.html")

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        board = [["." for j in range(0, 9)] for i in range(0, 9)]
        for i in range(9):
            for j in range(9):
                key = f"{i}{j}"
                board[i][j] = str(request.form[key])
        print(board)
        for i in range(9):
            for j in range(9):
                if (mukvnd_sudoku.isvalid(board, i, j, board[i][j])==False 
                    and board[i][j]!='.'):
                    return redirect(url_for("unsolved"))
        mukvnd_sudoku.solveboard(board)
        a = 0
        for i in board:
            for j in i:
                if j == ".":
                    a = 1
                    break
            if (a==1):
                break
        if (a==1):
            return redirect(url_for("unsolved"))
        else:      
            return render_template("solved.html", board = board)
if __name__ == "__main__":
    app.run()
