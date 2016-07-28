from flask import current_app, render_template_string

from flask_mail import Mail, Message

mailer = Mail()

def send_user_mail(recipient, **kwargs):
	params = dict(**current_app.config["AMU_USERMODMAIL"])
	params["body"] = render_template_string(params["body"], **kwargs).encode("UTF-8")
	params["charset"] = "UTF-8"

	msg = Message(recipients=[recipient], **params)
	return mailer.send(msg)

