# Final Project - Basic Python 
# Program untuk mengirimkan email kepada beberapa penerima
# Menggunakan smtp GMAIL, sebelumnya email pengirim di setting untuk menerima low security.

# Imports Library smtplib
import smtplib
import getpass

# SETUP EMAIL LOGIN 
gmail_user = input(str("Masukkan akun gmail: "))
gmail_password = getpass.getpass("Masukkan password gmail: ")

# SETUP Pengirim, penerima, judul dan isi email
sent_from = gmail_user
sent_to = input(str("Masukkan gmail penerima: "))
subject = input(str("Masukkan  subjek atau judul: "))
body = input(str("Masukkan pesan anda: "))

#SETUP PENERIMA EMAIL
file = open("receiver_list.txt", "a")
file.write(f'\n {sent_to}')
file.close

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(sent_to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, sent_to, email_text)
    server.close()

    print('Email sent!')
except Exception as exception:
    print("Error: %s!\n\n" % exception)

#sumber : https://stackoverflow.com/questions/10147455/how-to-send-an-email-with-gmail-as-provider-using-python