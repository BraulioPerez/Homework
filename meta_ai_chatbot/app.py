from flask import Flask, request, jsonify, render_template
from meta_ai_test import psyc_assistant

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/start', methods=['GET'])
def start():
    assistant = psyc_assistant()
    response = assistant.first_response()
    return jsonify({'message': response})

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    assistant = psyc_assistant(user_input=user_message)
    response = assistant.get_response()
    return jsonify({'message': response})

if __name__ == "__main__":
    app.run(debug=True)
