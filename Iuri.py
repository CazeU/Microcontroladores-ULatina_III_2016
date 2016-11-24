import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


fromaddr = "raspduinoss@gmail.com"
toaddr = "ugcascante@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "ALERTA DE INTRUSO"

body = "RaspDuino ha detectado un intruso en su casa"
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "rdSS2016")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
