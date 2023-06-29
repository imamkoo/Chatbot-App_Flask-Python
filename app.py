from flask import Flask, render_template, request, jsonify
from chatbot_module import get_bot_response

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['message']
    bot_response = get_bot_response(user_message)
    return jsonify({'message': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
