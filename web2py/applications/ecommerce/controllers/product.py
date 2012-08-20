# coding: utf-8

def show():
    # pegar produto no banco de dados
    # buscar pelo slug
    # acessar api do twitter
    db.product.tax_price = Field.Virtual(lambda row: row.product.unit_price * origins.get(row.product.origin, 1))
    try:
        pid = int(request.args(0))
        product = db.product[pid]
    except Exception:
        try:
            pid = int(request.args(0)[:5])
            product = db.product[pid]
        except Exception:
            redirect(URL('home', 'index'))

    # banco
    colors = ["amarelo", "azul", "vermelho"]

    fields = [
        Field("qtd", "integer", requires=IS_NOT_EMPTY(error_message=T("You have to inform the quantity")), label=T("Quantity")),
        Field("pid", default=product.id, label=""),
        Field("color", label=T("Color"), requires=IS_IN_SET(colors))
    ]
    form = SQLFORM.factory(*fields,
          formstyle="divs",
          submit_button=T("Add to cart"),
          _method="POST"
          )

    if form.process().accepted:
        session.cart = session.cart or []

        item = {
           "id": product.id,
           "qtd": form.vars.qtd,
           "name": product.name,
           "thumbnail": product.thumbnail,
           "price": product.unit_price,
           "total": float(form.vars.qtd) * float(product.unit_price)
        }

        session.cart.append(item)
        redirect(URL('cart', 'show'))

    btn = form.elements('input[type=submit]')
    btn[0]["_class"] = "btn btn-primary"

    form.elements("input#no_table_pid")[0]["_type"] = "hidden"

    return dict(product=product, form=form)


def get_miniatura_grid(row):
    if row.thumbnail:
        return IMG(_width=50, _height=50,_src=URL('home', 'download', args=[row.thumbnail]))
    else:
        return IMG(_src="http://placehold.it/50x50")

def search():
    # receber parametros e efetuar busca
    q = request.vars.q
    if q:
        term = "%%%s%%" % q
        query = db.product.name.like(term)
        query |= db.product.description.like(term)
    else:
        query = db.product

    db.product.thumbnail.represent = lambda value, row: get_miniatura_grid(row)

    links = [dict(header=T("View"),
                  body=lambda row: A(T("View details"), _class="btn btn-info", _href=URL('product', 'show', args=row.id)))]

    results = SQLFORM.grid(query,
        create=False,
        details=False,
        csv=False,
        editable=False,
        deletable=False,
        user_signature=False,
        links=links,
        fields=[db.product.thumbnail, db.product.name, db.product.category]
    )
    return dict(results=results)


def get_miniatura(row):
    if row.product.thumbnail:
        return IMG(_width=50, _height=50,_src=URL('home', 'download', args=[row.product.thumbnail]))
    else:
        return IMG(_src="http://placehold.it/50x50")


@auth.requires_membership("admin")
def list():
    # exibir todos os produtos
    # apenas para admin

    # DEFINITION OF FIELDS AND VIRTUAL FIELDS
    db.product.tax_price = Field.Virtual(lambda row: row.product.unit_price * origins.get(row.product.origin, 1))
    db.product.edit = Field.Virtual(lambda row: A("Edit", _href=URL('edit', args=row.product.id)))
    db.product.img = Field.Virtual(lambda row: get_miniatura(row))

    query = db.product.id > 2

    rows = db(query).select() # paginacao com limitby=(0, 10)

    headers = ["Foto","Name", "Unit Price", "Tax", "Edit"]
    fields = ['img', 'name', 'unit_price', 'tax_price', "edit"]

    #  HARD WAY
    # table = TABLE()

    # thead = THEAD(TR())
    # for header in headers:
    #     thead[0].append(TD(B(header)))
    # table.append(thead)

    # for row in rows:
    #     tr = TR()
    #     for field in fields:
    #         tr.append(row[field])
    #     table.append(tr)

    # table["_class"] = "table table-striped table-bordered table-condensed"

    # table.append(TR(TD(*[A(p, _href=URL(), _class="btn") for p in xrange(pages)], _colspan=4)))

    # # EASY WAY
    # table = TABLE(THEAD(TR(*[B(header) for header in headers])),
    #           TBODY(*[TR(*[TD(row[field]) for field in fields]) for row in rows]))
    # table["_class"] = "table table-striped table-bordered table-condensed"

    # # MAGIC WAY
    # db.product.category.represent = lambda value, row: value.name
    tax_price = lambda row: row.unit_price * origins.get(row.origin, 1)
    img = lambda row: get_miniatura_grid(row)

    links = [dict(header='Tax', body=tax_price),
             dict(header='Img', body=img)]

    table = SQLFORM.grid(query, user_signature=False, links=links, paginate=5)

    return dict(table=table)

def log_edit_form(form):
    if "apple" in form.vars.description:
        form.errors.name = "Voce nao pode editar este produto"
    print "formulario editado", form.vars

@auth.requires_login()
@auth.requires_membership("admin")
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
