import serial
import smtplib
print ("connecting to server.....")
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("sashwata21@gmail.com", "hellosashwata21%")
print("connected! yeahhhhhhh")
msg = "koi usko uthaooo......\n\n"

server.sendmail("sashwata21@gmail.com", "sashwata21@gmail.com",msg)

print("email sent\n")
