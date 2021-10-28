#!/usr/bin/env python3
#########################-Gmail Email sender-#########################
#########################-by your friendly  -#########################
#########################-beginner Akrotag  -#########################

##################################################################################################-Little Tutorial-##################################################################################################
# To use this script, simply open a terminal in the directory where you
# extracted this script (or use the "cd" command to go to this directory).
# Then you can simply type in the cmd the following:
#    (for Linux) python3 gmail_sender.py -ue "your email" -p "your password" -r "the receiver's email" -s "subject of the mail" -t "the body/content of the mail" -a "attachment's path(if you have any attachment to put)"
#    (for Windows) py gmail_sender.py -ue "your email" -p "your password" -r "the receiver's email" -s "subject of the mail" -t "the body/content of the mail" -a "attachment's path(if you have any attachment to put)"
#
# You can use a "\n" as a return in the body of the mail (obviously not in the subject).
# 
# There's still on important limitation: your attachment can't weight more than 25MB due to Gmail's limitations
#    
#
# I tried to handle as much errors as I could so that the errors are clearer in the terminal.
#  
######################################################################################################################################################################################################################


import argparse

def send(sender, password, receiver, subject, message, attachment):
    ########################-Sending email-########################
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders

    ###-Sets message service up-###
    msg = MIMEMultipart()

    ###-sets adresses, subject and body of the mail-###
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject

    body = message

    msg.attach(MIMEText(body, 'plain'))

    ###-Setting up attachment-###
    if attachment and attachment != " " and not(attachment is None):
        attach = open(attachment, "rb")
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attach).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % attach)
        msg.attach(p)

    ###-Connecting to gmail smtp server-###
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    try:
        s.login(sender, password) #logging in
    except (smtplib.SMTPAuthenticationError) as error:
        print("An error occured: wrong ceditentials\n\nCheck your email and password and make sure that you have enabled the less secure apps acess on your gmail account.\nFor more informations about less secure apps, go to https://support.google.com/a/answer/6260879")
        return    
    text = msg.as_string()
    try:
        s.sendmail(sender, receiver, text) #sending
    except TypeError as error:
        print("Error: the receiver was not defined")
        return
    except smtplib.SMTPSenderRefused as error:
        print("Error: the message exceeded Gmail's maximum message size limit (probably due to your attachment)\nPlease refer to https://support.google.com/mail/?p=MaxSizeError for more info")
        return

    ###-Leaving the server-###
    s.quit()

    print("Mail successfully sent to " + receiver)


#############-Actual program-#############
parser = argparse.ArgumentParser(description="Gmail email sender by Akrotag")

#############-Creating the commands-#############
parser.add_argument(
    "-ue",
    "--user_email",
    type= str,
    help= "from: user email, so your email"
)

parser.add_argument(
    "-p",
    "--password",
    type= str,
    help= "password: your password"
)

parser.add_argument(
    "-r",
    "--receiver",
    type= str,
    help= "receiver: the email adress person that will get the mail"
)

parser.add_argument(
    "-s",
    "--subject",
    type= str,
    help= "subject of your mail"
)

parser.add_argument(
    "-t",
    "--text",
    type= str,
    help= "text that you want to put in your email"
)

parser.add_argument(
    "-a",
    "--attachment",
    type= str,
    help= "attachment that you want to put in your mail"
)

args = parser.parse_args()

#############-Getting informations from the commands-#############
message = " "

if not(args.text is None):
    message = args.text.split("\\n")
    message = "\n".join(message)

sender = args.user_email
password = args.password
receiver = args.receiver
subject = args.subject
attachment = args.attachment

send(sender, password, receiver, subject, message, attachment)
