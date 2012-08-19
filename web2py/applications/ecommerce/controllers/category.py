# coding: utf-8

def list():
    # grid de categorias
    # apenas admin
    pass

def new():
    form = SQLFORM(db.category, formstyle="divs")
    return dict(form=form.process())