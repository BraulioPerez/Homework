from flask import Flask, request, render_template
from meta_ai_test import psyc_assistant

app = Flask(__name__)
assistant = psyc_assistant()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_message = request.form['message']
        assistant.user_input = user_message
        response = assistant.get_response()
        return render_template('chat.html', user_message=user_message, response=response["message"])
    else:
        initial_message = assistant.first_response()
        return render_template('chat.html', initial_message=initial_message["message"])

if __name__ == "__main__":
    app.run(debug=True)
