import smtplib
email = '269mehta@gmail.com' # Your email
password = '************' # Your email account password
send_to_email = '270mehta@gmail.com' # Who you are sending the message to
message1 = 'Website is not running due to some error'
server = smtplib.SMTP('smtp.gmail.com', 587) # Connect to the server
server.starttls() # Use TLS
server.login(email, password) # Login to the email server
server.sendmail(email, send_to_email , message1) # Send the email
server.quit() # Logout of the email server
