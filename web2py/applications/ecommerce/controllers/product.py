# coding: utf-8

def show():
    # pegar produto no banco de dados
    # buscar pelo slug
    # acessar api do twitter
    pass


def search():
    # receber parametros e efetuar busca
    pass

# @auth.requires_login()
def list():
    # exibir todos os produtos
    # apenas para admin

    # DEFINITION OF FIELDS AND VIRTUAL FIELDS
    db.product.tax_price = Field.Virtual(lambda row: row.product.unit_price * origins.get(row.product.origin, 1))
    db.product.edit = Field.Virtual(lambda row: A("Edit", _href=URL('edit', args=row.product.id)))
    query = db.product.id > 2
    rows = db(query).select()
    headers = ["Name", "Unit Price", "Tax", "Edit"]
    fields = ['name', 'unit_price', 'tax_price', "edit"]

    #  HARD WAY
    table = TABLE()

    thead = THEAD(TR())
    for header in headers:
        thead[0].append(TD(B(header)))
    table.append(thead)

    for row in rows:
        tr = TR()
        for field in fields:
            tr.append(row[field])
        table.append(tr)
    table["_class"] = "table table-striped table-bordered table-condensed"

    # table.append(TR(TD(*[A(p, _href=URL(), _class="btn") for p in xrange(pages)], _colspan=4)))

    # # EASY WAY
    # table = TABLE(THEAD(TR(*[B(header) for header in headers])),
    #           TBODY(*[TR(*[TD(row[field]) for field in fields]) for row in rows]))
    # table["_class"] = "table table-striped table-bordered table-condensed"

    # # MAGIC WAY
    # db.product.category.represent = lambda value, row: value.name
    # tax_price = lambda row: row.unit_price * origins.get(row.origin, 1)
    # links = [dict(header='Tax', body=tax_price)]
    # table = SQLFORM.grid(query,
    #                      user_signature=False,
    #                      links=links
    #                      )

    return dict(table=table)

def log_edit_form(form):
    if "apple" in form.vars.description:
        form.errors.name = "Voce nao pode editar este produto"
    print "formulario editado", form.vars


def edit():
    response.view = 'product/new.html'
    # pegar produto pelo id ou slug
    # criar formulario de edicao
    # apenas para admin
    pid = request.args(0) or redirect(URL('home', 'index'))
    form = SQLFORM(db.product, pid, formstyle="divs", submit_button="ENVIAR")
    message = ""
    form.process(onvalidation=log_edit_form)
    return dict(form=form, message=message)
    
    # pid = request.args(0)
    # form = SQLFORM(db.product, pid, formstyle="divs")
    # button = form.elements('input[type=submit]')[0]
    # button["_value"] = "banana"
    # if form.process().accepted:
    #     redirect(URL('list'))
    # return form


@auth.requires_login()
@auth.requires_membership("admin")
def new():
    # if request.vars:
    #     name = request.vars.name
    #     description = request.vars.description
    #     db.product.description.requires = IS_NOT_EMPTY()
    #     print db.product.validate_and_insert(name=name, description=description, qtd=1)
    #     db.commit()   
    # form para add novo produto
    # apenas para admin

    hide_fields("product", ["total_price"])
    message = None
    form = SQLFORM(db.product, formstyle="divs")
    if form.process().accepted:
        message = T("Product registered")
    elif form.errors:
        message = T("Error in form")

    return dict(form=form, message=message)




# def grid(query,
#          fields=None,
#          field_id=None,
#          left=None,
#          headers={},
#          orderby=None,
#          groupby=None,
#          searchable=True,
#          sortable=True,
#          paginate=20,
#          deletable=True,
#          editable=True,
#          details=True,
#          selectable=None,
#          create=True,
#          csv=True,
#          links=None,
#          links_in_grid=True,
#          upload = '<default>',
#          args=[],
#          user_signature = True,
#          maxtextlengths={},
#          maxtextlength=20,
#          onvalidation=None,
#          oncreate=None,
#          onupdate=None,
#          ondelete=None,
#          sorter_icons=(XML('&#x2191;'),XML('&#x2193;')),
#          ui = 'web2py',
#          showbuttontext=True,
#          _class="web2py_grid",
#          formname='web2py_grid',
#          search_widget='default',
#          ignore_rw = False,
#          formstyle = 'table3cols',
#          exportclasses = None,
#          formargs={},
#          createargs={},
#          editargs={},
#          viewargs={},
#         ):