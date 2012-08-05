# coding: utf-8

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
    return dict(form=auth())

def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request,db)
    
