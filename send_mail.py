import smtplib
from email.mime.text import MIMEText


def send_mail(cliente, producto, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '75fc037f34e46e'
    password = '285c09c6c7d1fa'
    message = f"<h3>Nuevo Mensaje Pedido</h3><ul><li>Cliente: {cliente}</li><li>Producto: {producto}</li><li>Comments: {comments}</li></ul>"

    sender_email = 'andrucahechoamano@gmail.com'
    receiver_email = 'to@example.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Pedido'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

