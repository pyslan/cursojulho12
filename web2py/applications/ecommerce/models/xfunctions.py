
def hide_fields(tablename, fields):
    for field in fields:
        db[tablename][field].writable = \
            db[tablename][field].readable = False  


def slugfy(product):
    template = "%(id_formatado)s-%(name)s"
    id_formatado = str(product.id).zfill(5)
    return template % dict(id_formatado=id_formatado, name=product.name)


def format_price(value):
    val = "R$ %.2f" % float(value)
    return val.replace(".", ",")

#T.force("en")