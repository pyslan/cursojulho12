# coding: utf-8

def show():
    # exibir carrinho de compras
    # criar sessao caso nao exista
    # forulario para tipo de pagamento
    
    headers = ["Img","Name", "Unit Price", "Qtd", "Total", "remove"]
    fields = ["thumbnail","name", "price", "qtd", "total", "remove"]

    #  HARD WAY
    table = TABLE()

    thead = THEAD(TR())
    for header in headers:
        thead[0].append(TD(B(header)))
    table.append(thead)

    for item in session.cart:
        tr = TR(_id=item["id"])
        for field in fields:
            if field == "thumbnail":
                if not item['thumbnail']:
                    img = IMG(_src="http://placehold.it/50x50")
                else:
                    img = IMG(_width=50, _heught=50,_src=URL('home', 'download', args=item['thumbnail']))
                tr.append(img)
            elif field == "remove":
                a = A(T("remove"),
                      _class="btn btn-danger removebutton",
                      _href=URL('cart', 'remove', args=item['id']))
                tr.append(a)
            elif field in ["price", "total"]:
                tr.append(format_price(item[field]))
            else:
                tr.append(item[field])
        table.append(tr)
    
    table["_class"] = "table table-striped table-bordered table-condensed"
    

    total = sum([item["total"] for item in session.cart])

    return dict(cart=table, total=total)

def remove():
    # remover item do carrinho via ajax
    pid = request.args(0)
    newcart = []
    for item in session.cart:
        if int(item["id"]) != int(pid):
            newcart.append(item)
    session.cart = newcart
    # usamos apenas em teste
    # nao usar eval em produção
    return "jQuery('#%s').remove(); alert('HEY! Implemente o redirect caso o carrinho seja vazio!');" % pid

def clear():
    # limpar carrinho
    pass

def checkout():
    # apenas para usuario logado
    # gerar pedido
    # enviar email para o cliente
    return dict(message="Implemente o fechamento do pedido, inserção nas tabelas order e order_items (crie essas tabelas), envie um email para o usuario e notifique o admin que entrou um novo pedido")

