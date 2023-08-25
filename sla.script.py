import subprocess
import time
import logging
import smtplib
from email.mime.text import MIMEText


def send_email(sender_email, sender_password, recipient_email, subject, message):
    # Set up SMTP server
    smtp_server = "smtp-mail.outlook.com"
    smtp_port = 587
    smtp_username = sender_email
    smtp_password = sender_password

    # Create message
    email_message = MIMEText(message)
    email_message['Subject'] = subject
    email_message['From'] = sender_email
    email_message['To'] = recipient_email

    # Send message
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(email_message)




# Set up logging
logging.basicConfig(filename='sla.log', level=logging.INFO)

# Load configuration
rb_name = "RB EL AGUACATE"
backup_interface = "eth1"
main_interface = "eth0"
backup_ip = "192.168.1.1"
main_ip = "172.29.3.1"
sleep_time = 3
sender_email = "no@grupohemac.com.mx"
sender_password = "password"
recipient_email = "alarmasnoc@grupohemac.com.mx"

# Set up default route
subprocess.call(['ip', 'route', 'del', 'default'])
subprocess.call(['ip', 'route', 'add', 'default', 'via', main_ip, 'dev', main_interface, 'metric', '80'])

# Main loop
while True:
    # Ping Google DNS server
    result = subprocess.run(['ping', '-c', '1','-I', main_interface, '8.8.8.8'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if result.returncode != 0:
        # Ping failed, change the default route to use backup interface
        subprocess.call(['ip', 'route', 'del', 'default', 'via', main_ip, 'dev', main_interface, 'metric', '80'])
        subprocess.call(['ip', 'route', 'add', 'default', 'via', backup_ip, 'dev', backup_interface, 'metric', '88'])
        logging.info("Ping failed. Switching to backup interface: %s", backup_interface)

        '''# Send email notification
        subject = "Main interface failed"
        message = "HELP " + rb_name + " ping on the main interface has failed. Switching to backup interface: {}.".format(backup_interface)
        send_email(sender_email, sender_password, recipient_email, subject, message)'''

    else:
        # Ping successful, switch back to main interface
        subprocess.call(['ip', 'route', 'del', 'default', 'via', backup_ip, 'dev', backup_interface, 'metric', '88'])
        subprocess.call(['ip', 'route', 'add', 'default', 'via', main_ip, 'dev', main_interface, 'metric', '80'])
        logging.info("Ping successful. Switching back to main interface: %s", main_interface)

    # Sleep for specified amount of time
    time.sleep(sleep_time)

