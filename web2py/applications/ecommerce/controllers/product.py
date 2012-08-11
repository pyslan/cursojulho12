# coding: utf-8

def show():
    # pegar produto no banco de dados
    # buscar pelo slug
    # acessar api do twitter
    pass


def search():
    # receber parametros e efetuar busca
    pass


def list():
    # exibir todos os produtos
    # apenas para admin
    db.product.tax_price = Field.Virtual(lambda row: row.product.unit_price * origins.get(row.product.origin, 1))
    rows = db(db.product).select()
    headers = ["Name", "Unit Price", "Tax"]
    fields = ['name', 'unit_price', 'tax_price']

    table = TABLE(THEAD(TR(*[B(header) for header in headers])),
                  TBODY(*[TR(*[TD(row[field]) for field in fields]) for row in rows]))

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

    table["_class"] = "table table-striped table-bordered table-condensed"

    table = SQLFORM.grid(db.product)

    return dict(table=table)

def edit():
    # pegar produto pelo id ou slug
    # criar formulario de edicao
    # apenas para admin
    pass

def new():
    # form para add novo produto
    # apenas para admin
    pass