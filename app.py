from flask import Flask,request
import smtplib
from email.utils import formataddr
from email.message import EmailMessage

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/mailer', methods=['POST'])
def send_mail():
    # print(request.form['sender'])
    # print(request.form['receiver'])
    # print(request.form['spwd'])
    name = "Karthick"
    sender = "timeline.sass@gmail.com"
    receiver = "galoyir660@youke1.com"
    spwd = "crosogofbxvasouy"
    company = "Timeline"
    SERVER = "smtp.gmail.com"
    PORT = 587
    bod_draft = f"""/<h1>Hi {name},</h1>
                    <p>Hope you are doing well</p>
                    <h6><i>this</i> is to test the mailing service of timeline</h6>
                    <p>Regards, <br/> {company}</p>"""
    bod = f'{bod_draft}'

    txxt = "Hey! Lets see if it works or not"
    httml = f"""\<h1>Hi {name},</h1>
                    <p>Hope you are doing well</p>
                    <h6><i>this</i> is to test the mailing service of timeline</h6>
                    <p>Regards, <br/> {company}</p>"""

    textPart = MIMEText(txxt,'plain')
    htmlPart = MIMEMultipart(httml,'html')

    msg = EmailMessage()
    msg['Subject'] = "This is a test mail from Timeline dev"
    msg['From'] = formataddr(("Welcome to timeline",f"{sender}"))
    msg['To'] = receiver

    msg.attach(payload=htmlPart)
    # msg.set_content(
    #     f"""\
    #     Hi {name},
    #     Hope you are doing well.
    #     I'm just checking the mail function using flask API.
    #     Regards,
    #     {company}
    #     """
    # )


    # msg.add_alternative(bod,
    #     subtype="html"
    # )

    with smtplib.SMTP(SERVER,PORT) as server:
        server.starttls()
        server.login(sender, spwd)
        server.sendmail(sender,receiver,msg.as_string())

if __name__ == "__main__":
    app.run(debug=True)