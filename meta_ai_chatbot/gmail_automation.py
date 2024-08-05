
from simplegmail import Gmail


def send_email_to(to_who, sender, data):
    gmail = Gmail()

    params = {
    "to": f"{to_who}",
    "sender": f"{sender}",
    "subject": "Student Concern",
    "msg_html": f"<h1>Woah, my first email!</h1> <p>{data}</p>"
    }
    message = gmail.send_message(**params)


