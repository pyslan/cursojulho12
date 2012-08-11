#coding: utf-8

# Criar objeto de configuracao com storage

# import sys
# sys.path.insert(0, r"c:\Users\rochacbruno\jul12\cursojulho12\web2py")

from gluon.storage import Storage
config = Storage(
    db=Storage(),
    mail=Storage(),
    auth=Storage()
) 

# definir settings para db, auth, mail

config.db.uri = "sqlite://ecommerce.db"
config.db.pool_size = 0
config.db.check_reserved = ["all"]
config.db.migrate_enabled = True # desligar quando em produção

config.mail.sender = "ecommerce@ecoomerce.com"
config.mail.server = "logging" # "smtp.dddd:25"
config.mail.login = "usuario:senha"


# definir nivel de acesso a views genericas
# criar/importar funcoes globais

response.title = "Ecommerce do Bruno | CursodePython.com.br"
response.description = "Ecommerce"

response.generic_patterns = ['*']