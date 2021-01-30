import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SENDER_EMAIL = 'your username'
SENDER_PASSWORD = 'Your password'
SERVER = 'smtp.gmail.com:587'
RECEIVER_EMAIL = 'sender email id'
# demo user
name = 'sumith'
age = '20'
ph = '8197316602'
status ='not normal'

SUBJECT = 'SIDAR-S Report'
HTML = """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8"/>
<style>
ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
    overflow: hidden;
    background-color: #333;
    }
.active{
    display: block;
    color: #FFFFFF;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
    float: left;
    font-size: 20px
    }
pre {
    display: block;
    font-family: monospace;
    white-space: pre;
    margin: 1em 0;
    font-size: 15px
    }
</style>
</head>
<body>
<nav class="navbar">
    <ul class="nav navbar-nav">
      <li class="active">SIDAR-S</li>
    </ul>
</nav>
<pre>
  Hello Mr/Mrs/Ms."""+ name +""" Your son/daughter/sibling wanted to contact you. Their mental health status was predicted as - """+ status +""" . Please get in touch with them immediately.
  Here are the contact details -
  Mr."""+ name +"""
  Age:"""+ age +"""
  Ph:"""+ ph +"""
</pre>
  </body>
</html>"""


def _generate_message() -> MIMEMultipart:
    message = MIMEMultipart("alternative", None, [MIMEText(HTML, 'html')])
    message['Subject'] = SUBJECT
    message['From'] = SENDER_EMAIL
    message['To'] = RECEIVER_EMAIL
    return message


def send_message():
    message = _generate_message()
    server = smtplib.SMTP(SERVER)
    server.ehlo()
    server.starttls()
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message.as_string())
    server.quit()


if __name__ == '__main__':
    send_message()
