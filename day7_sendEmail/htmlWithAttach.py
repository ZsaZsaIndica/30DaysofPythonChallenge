# import necessary modules
import smtplib
import ssl
import os
import email

# subclasses for email.mime, a module part of an email API.
# MIMEMultipart base class for multipart messages.
from email.mime.multipart import MIMEMultipart
# MIMEtext changes data type to text string for payload
from email.mime.text import MIMEText
# MIMEApplication a class to represent MIME message objects
from email.mime.application import MIMEApplication

# email authentication info saved in another app for security
from email_config import from_this_email, python_email_password, one_recieving_email_address

# store the sender email, sender email password, and receiver email in variables
from_email = from_this_email
the_email_password = python_email_password
to_email = one_recieving_email_address
# a variable to store a list of emails for multiple recepients in config app
# (ex. multiple_emails  = ['Vangie23@gmail.com', 'Pearl234@gmail.com'])
# to_email = multiple_emails

# the MIMEMultipart subclass is used here for the multi-parts FROM, TO, SUBJECT fields
email_message = MIMEMultipart()
email_message['From'] = from_email
email_message['To'] = to_email
email_message['Subject'] = 'Guess who\'s back in the house'

# the HTML document for the body of the email
html = '''
<!DOCTYPE html>
<html lang="en">
  <body style=-webkit-background-size: cover;
      -moz-background-size: cover;
      -o-background-size: cover;
      background-size: cover;
      background-image: linear-gradient(to bottom, #000000, #171110, #241c16, #2d291c, #303726, #354730, #34583f, #2c6a52, #2a8160, #25996f, #1ab27d, #00cb8b);    background-repeat: no-repeat;>
    <h2 color: rgb(127, 127, 168);
      font-family:'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;>Let me tell you a story about...</h2>
    <h1 style=color: rgb(6, 6, 43);
      font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
      font-size: 300%;>Aqua Teen Hunger Force</h1>
    <p style=color: rgb(0, 0, 0);
      font-family:'Courier New', Courier, monospace;
      font-size: 160%;
      font-weight: bold;>Aqua Teen Hunger Force is the greatest cartoon of all time. Story Over. 😎
    </p>
  </body>
</html>
'''

# using MIMEtext html content attatch method , attach the html to the email message
email_message.attach(MIMEText(html, "html"))

# a function to attatch files as MIMEApplication to the email
def attatching_file_to_email(email_message, filename):
  with open(filename, "rb") as my_file:
    file_attatchment = MIMEApplication(my_file.read())
  file_attatchment.add_header(
    'Content-Disposition',
    'attachment',
    filename=filename
  )
  email_message.attach(file_attatchment)

# attach the documents to be sent using the function defined above
attatching_file_to_email(email_message, 'day7_sendEmail/Book1.xlsx')
attatching_file_to_email(email_message, 'day7_sendEmail/selfie2.jpg')
attatching_file_to_email(email_message, 'day7_sendEmail/a_text.txt')

# email message is converted to a string
email_string = email_message.as_string()

# to connect to Gmail SMTP server by creating a secure default settings context
context = ssl.create_default_context()
# and then initilizing the connection to the Gmail SMTP Outgoing Mail server with the context created
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
  server.login(from_email, the_email_password) # login info
  server.sendmail(from_email, to_email, email_string)
