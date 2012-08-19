# coding: utf-8

def list():
    # grid de categorias
    # apenas admin
    grid = SQLFORM.grid(db.category.id>0)
    return dict(grid=grid)

def new():
    form = SQLFORM(db.category, formstyle="divs")
    return dict(form=form.process())