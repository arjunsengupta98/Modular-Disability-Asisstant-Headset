#import serial
import smtplib
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.IN)

ip=0



while 1:
    ip=GPIO.input(8)
    if(ip==1):

        print ("connecting to server.....\n")
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("sashwata21@gmail.com", "hellosashwata21%")
        print("Connection established successfully\n")
        msg = "Dear Arjun. The patient has fallen. Please help."

        server.sendmail("sashwata21@gmail.com", "arjunsengupta98@gmail.com",msg)

        print("email sent\n")
        break
