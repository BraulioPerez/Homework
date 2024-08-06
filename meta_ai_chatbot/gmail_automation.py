
from simplegmail import Gmail


def send_email_to(to_who, sender, data):
    gmail = Gmail()

    params = {
    "to": f"{to_who}",
    "sender": f"{sender}",
    "subject": "Bot Assistant - Student Report",
    "msg_html": f"<h2>Student Report</h2> <p style='color: #333333; font-size: 16px; line-height: 1.5; margin: 10px 0; font-family: Arial, sans-serif;'>{data}</p>"
    }
    message = gmail.send_message(**params)
    
if __name__ == "__main__":
    send_email_to('braulioprez.contacto@gmail.com', 'braulioprez.contacto@gmail.com', 'Hola')


