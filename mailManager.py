from flask import Flask,request
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
#
# app = Flask(__name__)
#
# @app.route('/mailer', methods=['POST'])
# def send_mail():
#     # Set up the email server connection
#     smtp_server = 'smtp.gmail.com'
#     smtp_port = 587
#     smtp_username = 'timeline.sass@gmail.com'
#     smtp_password = 'crosogofbxvasouy'
#     smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
#     smtp_connection.starttls()
#     smtp_connection.login(smtp_username, smtp_password)
#
#     # Set up the email message
#     msg = MIMEMultipart()
#     msg['From'] = 'timeline.sass@gmail.com'
#     msg['To'] = 'galoyir660@youke1.com'
#     msg['Subject'] = 'Dynamic Email Subject'
#
#     # Create the body of the email message
#     message_template = 'Hello, {name}!\n\nThis is a dynamic email message sent from Python.'
#     message = message_template.format(name='John')
#
#     # Attach the message to the email
#     msg.attach(MIMEText(message, 'plain'))
#
#     # Send the email
#     smtp_connection.sendmail(msg['From'], msg['To'], msg.as_string())
#
#     # Close the connection to the email server
#     smtp_connection.quit()



import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/mailer', methods=['POST'])
def compile_mail():
    network = {}
    if(request.method == "POST"):
        network['uname'] = request.json['username']
        network['word'] = request.json['word']
        network['server'] = request.json['server']
        network['port'] = request.json['port']
        network['isSSL'] = request.json['isSSL']
        subject = request.json['subject']
        recepient = request.json['recepient']
        message_template = request.json['payload']
        variables = request.json['variables']


    #message_template = 'Hello, {name}!\n\nThis is a dynamic email message sent from Python. Your age is {age}.'
    try:
        send_email(network, recepient, subject, message_template, variables=variables)
    except:
        return("Error")
    finally:
        return("success")

def send_email(network,recipient, subject, message_template, variables):
    # Set up the email server connection
    smtp_server = network['server']
    smtp_port = network['port']
    smtp_username = network['uname']
    smtp_password = network['word']
    # smtp_server = 'smtp.gmail.com'
    # smtp_port = 587
    # smtp_username = 'timeline.sass@gmail.com'
    # smtp_password = 'crosogofbxvasouy'
    smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
    smtp_connection.starttls()
    smtp_connection.login(smtp_username, smtp_password)

    # Set up the email message
    msg = MIMEMultipart()
    msg['From'] = network['uname']
    msg['To'] = recipient
    msg['Subject'] = subject

    # Create the body of the email message
    message = message_template.format(**variables)
    html_message = MIMEText(message, 'html')
    msg.attach(html_message)
    # Attach the message to the email
    #msg.attach(MIMEText(message, 'html'))

    # Send the email
    smtp_connection.sendmail(msg['From'], msg['To'], msg.as_string())

    # Close the connection to the email server
    smtp_connection.quit()



if __name__ == "__main__":
    app.run(debug=True)