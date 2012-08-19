#coding: utf-8


import json

def productjson():
    nome = request.vars.nome
    if nome:
        query = db.product.name.like("%%%s%%" % name)
    else:
        query = db.product

    # as_list para retornar json
    products = db(query).select().as_list()
    return json.dumps(products)

#########

@service.xmlrpc
def query(key=None):
    if key:
        query = db.product.name.like("%%%s%%" % key)
    else:
        query = db.product

    # as_list para retornar json
    products = db(query).select().as_list()
    return products

@service.xmlrpc
def addproduct(name, category, description, price):
    newid = db.product.insert(**kwargs)
    db.commit()
    return newid

@service.soap("Soma", returns={'result':int}, args={'x': int, 'y': int})
def soma(x, y):
    return x + y



## final
def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()