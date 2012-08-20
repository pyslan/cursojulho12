# coding: utf-8

@auth.requires_membership("admin")
def list():
    # grid de categorias
    # apenas admin
    grid = SQLFORM.grid(db.category.id>0)
    return dict(grid=grid)

@auth.requires_membership("admin")
def new():
    form = SQLFORM(db.category, formstyle="divs")
    return dict(form=form.process())
