from flask import Flask, request, render_template
from meta_ai_test import psyc_assistant
from gmail_automation import send_email_to
import json

app = Flask(__name__)
assistant = psyc_assistant()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_message = request.form['message']
        assistant.user_input = user_message
        response = assistant.get_response()
        
        if ":)" in response["message"]:
            last_one = assistant.last_response()
            try:
                last_one_string = last_one['message']
                last_one_dictionary = json.loads(last_one_string)
                
                content_mail = f"Full name of the student:{last_one_dictionary['full_name']} <br>" + f"Major:{last_one_dictionary['major']} <br>" + f"Term: {last_one_dictionary['fourth_month_period']}<br>" + f"Description of the problem: {last_one_dictionary['description_problem']} <br>" + f"An appointment is needed: {last_one_dictionary['appointment_is_needed']} <br>"
                send_email_to('franciscochan551@gmail.com', 'franciscochan415@gmail.com', content_mail)
            
            except json.JSONDecodeError as e:
                print(f"Error decodificando JSON: {e}")
                last_one_string = last_one['message']
                content_mail = last_one["message"]
                send_email_to('francisochan551@gmail.com', 'franciscochan415@gmail.com', content_mail)
                
        return render_template('chat.html', user_message=user_message, response=response["message"])
    else:
        initial_message = assistant.first_response()
        
        return render_template('chat.html', initial_message=initial_message["message"])

if __name__ == "__main__":
    #app.run(host="0.0.0.0", port="5000")
    app.run(debug=True)
