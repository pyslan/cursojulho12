# coding: utf-8

def list():
    # se o usuario for cliente exibir apenas suas compras
    # se for admin, exibir todas as compras
    # se for admin permitir alterar status
    if auth.has_membership("admin"):
	    query = "Crie aqui a query que exibe os dados que o admin pode ver"
    else:
	    query = "Crie aqui a query que exibe apenas os pedidos feitos pelo usuário logado"
    orders = "Crie aqui umm SQLFORM.grid para exibir os pedidos"
    # NOTA: Se for admin pode editar o pedido
    # se for usuario pode apenas ver os detalhes 
    return dict(orders=orders) 
