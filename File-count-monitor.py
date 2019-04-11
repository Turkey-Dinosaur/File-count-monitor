#file count monitor
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import win32com.client as win32
import os

#Add the path to the folder you want to monitor between the quotes
path = "C:/Users/USERNAME/Desktop/Images/"

#Identifies the files in the folder
files = os.listdir(path)

#Get's the number of files in the folder
index = len(files)

#prints the number of files in the folder
print(index)

#Uncomment lines 23-32 and add your own information to send an email if the folder contains less than 10 files
# This is only if Outlook is your native email application, such as in a corporate environment.

#def emailer():
#	outlook = win32.Dispatch('outlook.application')
#	mail = outlook.CreateItem(0)
#	mail.To = 'RECIPIENT EMAIL ADDRESS'
#	mail.Subject = 'SUBJECT OF THE EMAIL '
#	mail.Body = 'BODY OF THE EMAIL'
#	mail.Send()

#if index < 10:
#	emailer()

#Uncomment the below function to send an email via hotmail or Gmail
#Add your email account details to lines 40, 41 & 43 and the email details to lines 42 & 44
#Choose either Hotmail or Gmail by uncommenting either line 47 or 48. 

#def alt_emailer():
#	msg = MIMEMultipart()
#	msg['From'] = 'SENDER EMAIL ADDRESS'
#	msg['To'] = 'RECIPIENT EMAIL ADDRESS'
#	msg['Subject'] = 'SUBJECT OF THE EMAIL'
#	password = 'SENDER EMAIL ACCOUNT PASSWORD'
#	body = 'BODY OF THE EMAIL'
#	msg.attach(MIMEText(body, 'html'))
#	print(msg)
#	server = smtplib.SMTP("smtp-mail.outlook.com")
# server = smtplib.SMTP("smtp.gmail.com")
#	server.starttls()
#	server.login(msg['From'], password)
#	server.sendmail(msg['From'], msg['To'], msg.as_string())
#	server.quit()

#if index < 10:
#	alt_emailer()
