import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


fromaddr = "raspduinoss@gmail.com"
eliaddr = "eroch2093@gmail.com"
uriaddr = "ugcascante@gmail.com"

emails = [ "eroch2093@gmail.com", "ugcascante@gmail.com" ]



def create_msg(fromaddr, toaddr, subject, body):
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = subject

	msg.attach(MIMEText(body, 'plain'))
	return msg

def send_msg(msg):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, "rdSS2016")
	text = msg.as_string()
	server.sendmail(msg['From'], msg['To'], text)
	server.quit()

def fire_alert(fire_to):
	body = "RaspDuino ha detectado un incendio en su casa"
	msg = create_msg(fromaddr, fire_to, "ALERTA DE INCENDIO", body)
	send_msg(msg)

def intr_alert(intr_to):
	body = "RaspDuino ha detectado un intruso en su casa"
	msg = create_msg(fromaddr, intr_to, "ALERTA DE INTRUSO", body)
	send_msg(msg)


if __name__ == "__main__":
	for e in emails:
		fire_alert(e)
