from flask import Flask, render_template, jsonify
import random
app = Flask(__name__)
@app.route('/')
def index():
    return render_templates('index.html')
@app.route('/shuffle')
def shuffle():
# Create a random configuration of the 8-puzzle
    numbers = list(range(1, 9)) + [None]
    random.shuffle(numbers)
    board = [numbers[i:i+3] for i in range(0, 9, 3)]
    return jsonify({'board': board})
if __name__ == '_main_':
    app.run(debug=True)