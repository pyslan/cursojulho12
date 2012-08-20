# coding: utf-8

from gluon.template import render
import os


@auth.requires_membership("admin")
def userlist():
    return dict(userlist="Implemente um SQLFORM.grid ou uma tabela para gerenciar os usuários, apenas o admin tem acesso")


@auth.requires_membership("admin")
def admin():
    items = {
       "product": {
          "list": URL('product', 'list'),
          "new": URL('product', 'new')
       },
       "category": {
           "list": URL('category', 'list')
       },
       "users": {
           "list": URL('home', 'userlist')
       },
       "orders": {
           "list": URL("order", "list")
       }
    }
    menu = UL()
    for item, subitems in items.items():
        li = LI(item.title(), ":", BR())
        for  name, url in subitems.items():
            li.append(A(name.title(), _href=url, _class="btn"))
        menu.append(li)

    return dict(menu=menu)

def render_email_confirma(form, template_file):
    caminho = os.path.join(request.folder, "views", template_file)
    with open(caminho, "r") as template:
        message = render(content=template.read(), context=form.vars)
    return message


def contact():
    form =  FORM(
                 INPUT(_type="text", requires=IS_NOT_EMPTY(), _name="name", _placeholder=T("Your name")),
                 BR(),
                 INPUT(_type="email", requires=IS_EMAIL(), _name="email", _placeholder=T("Your email")),
                 BR(),
                 TEXTAREA("Sua mensagem",_name="message", requires=IS_NOT_EMPTY()),
                 BR(),
                 BUTTON("Enviar")
                )

    if form.process().accepted:
        #adm
        mail.send(
              to="alunos+admin@gmail.com",
              subject="Novo contato - site",
              message=[None, render_email_confirma(form, "email_contato.html")]
            )
        # confirma usuario
        mail.send(
              to=form.vars.email,
              subject="Recebemos sua mensagem",
              message=[None, render_email_confirma(form, "email_confirma.html")]
            )

        form.insert(0, P(T("Successfully sent"), _class="alert"))
    return dict(form=form)


def index():
    products = db(db.product).select(limitby=(0, 100))
    featured = products.exclude(lambda registro: registro.featured == True)
    #print db._timings
    #response.view = "alternate/myhome.html"
    return dict(products=products, featured=featured)



    # objetos = [1,2,3]
    # import json
    # return json.dumps(dict(objetos=objetos))


    # return DIV(
    #             UL(
    #               LI(A("Hello")),
    #               LI(A("Google", _href="http://www.google.com"))
    #               )
    #             )


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    if request.args(0) == "not_authorized":
        return dict(form=DIV("YOU DONT HAVE ACCESS!! BASTARD!"))
    if request.args(0) in ['login', 'register']:
        redirect(URL('home', 'account', vars=request.vars))

    if request.args(0) == "register":
        hidden_fields = ['zipcode', 'picture', 'address', 'house_number']
        hide_fields("auth_user", hidden_fields)
    return dict(form=auth())

def account():
    hidden_fields = ['zipcode', 'picture', 'address', 'house_number']
    hide_fields("auth_user", hidden_fields)
    return dict(register=auth.register(),
                login=auth.login())

def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request,db)


import time

def testcache():
    t = cache.ram('time', lambda: time.ctime(), time_expire=60)
    return dict(t=t, link=A('refresh', _href=request.url))

@cache('time2', time_expire=15, cache_model=cache.ram)
def testcache2():
    return time.ctime()

def testcache3():
    rows = db(db.product).select(cache=(cache.ram, 60))
    return rows

