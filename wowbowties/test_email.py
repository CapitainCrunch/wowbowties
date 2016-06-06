__author__ = 'Bogdan'
__email__ = 'evstrat.bg@gmail.com'
__mobile_phone__ = 89252608400

import smtplib

def prompt(prompt):
    return input(prompt).strip()

fromaddr = prompt("From: ")
toaddrs  = prompt("To: ").split()
print ("Enter message, end with ^D (Unix) or ^Z (Windows):")

# Add the From: and To: headers at the start!
msg = ("From: %s\r\nTo: %s\r\n\r\n"
       % (fromaddr, ", ".join(toaddrs)))
while 1:
    try:
        line = input()
    except EOFError:
        break
    if not line:
        break
    msg = msg + line

print ("Message length is " + repr(len(msg)))

server = smtplib.SMTP('smtp.gmail.com:587')
server.set_debuglevel(1)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
print('sended')