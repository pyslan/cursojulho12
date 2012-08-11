#coding: utf-8

# definir objetos da app (Auth, Mail, Service)

from gluon.tools import Auth, Mail

auth = Auth(db, hmac_key=Auth.get_or_create_key())


# CAPTCHA

# from gluon.tools import Recaptcha
# auth.settings.captcha = Recaptcha(request,
#     'PUBLIC_KEY', 'PRIVATE_KEY')

# auth_user, auth_groups, auth_membership, auth_permission

#auth.settings.extra_fields["auth_user"] = [CPF]

# auth.settings.registration_requires_verification = False
# auth.settings.registration_requires_approval = False
# auth.settings.reset_password_requires_verification = True

mail = Mail()
mail.settings.sender = config.mail.sender
mail.settings.server = config.mail.server
mail.settings.login = config.mail.login

auth.settings.mailer = mail

# auth.settings.login_field = 'cpf'
auth.define_tables()

# definir classes e funcoes da app
# definir autenticacao
# definir datamodel de autenticacao
# definir emails de autenticacao

# signature