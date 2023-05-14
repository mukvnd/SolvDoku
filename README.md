# Sudoku Solver using Flask, Python, HTML and Backtracking Algorithm

SolvDoku - a web based application that solves Sudoku puzzles using the backtracking algorithm. The application is built using Flask, Python, HTML, and CSS.

## Installation

1. Clone the repository:
```
git clone https://github.com/mukvnd/sudoku-solver.git
```

2. Install the dependencies:
```
pip install -r requirements.txt
```

3. Run the application:
```
python app.py
```

4. Open your browser and go to http://localhost:5000

## Usage

To use the Sudoku solver, simply enter the puzzle you want to solve in the 9x9 grid on the web page. Use numbers 1-9 for the given cells and leave the blank cells empty. Once you have entered the puzzle, click the "Solve" button to solve it.

If the puzzle is solvable, the solved puzzle will be displayed in the grid. If the puzzle is not solvable, an HTML file with error will be displayed.

## Algorithm

Backtracking is a general algorithmic technique that involves exploring all possible solutions to a problem by incrementally building up a candidate solution and backing off when it becomes clear that the candidate solution cannot be completed to a valid solution.

The Sudoku solver uses the backtracking algorithm to solve puzzles. This algorithm works by trying a number in a cell, and then moving on to the next cell. If all of the numbers in the current cell lead to a dead end, the algorithm backtracks to the previous cell and tries a different number.

The backtracking algorithm is a brute force method, but it is very effective for solving Sudoku puzzles. In fact, it is the same algorithm that humans use to solve Sudoku puzzles!


The Sudoku solver was created using Flask, Python, HTML, and CSS. The backtracking algorithm used in the solver is a common algorithm used for Sudoku puzzles.
