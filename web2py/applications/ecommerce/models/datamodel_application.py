#coding: utf-8

# definir objetos da app (Auth, Mail, Service)

from gluon.tools import Auth, Mail, Service

service = Service()

auth = Auth(db, hmac_key=Auth.get_or_create_key(), controller="home", function="user")

#session.connect(request, response, db)

auth.settings.login_next = URL('home', 'index')

# CAPTCHA

# from gluon.tools import Recaptcha
# auth.settings.captcha = Recaptcha(request,
#     'PUBLIC_KEY', 'PRIVATE_KEY')

# auth_user, auth_groups, auth_membership, auth_permission

auth.settings.extra_fields["auth_user"] = [
    Field("picture", "upload"),
    Field("zipcode"),
    Field("address"),
    Field("house_number")
]

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