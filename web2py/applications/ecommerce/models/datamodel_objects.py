#coding: utf-8

# definir tabelas de objetos do sistema

# Category
# id, name, description

# Table, Field, define_table

db.define_table("category",
    # Field("cod_cat", "id"),
    Field("name", length=128, notnull=True, unique=True),
    Field("description", "text"),
    Field("picture", "upload"),
    auth.signature,
    format="%(name)s"
    # migrate=False,
    # primary_key=["cod_cat", "name"],
    )

# Product
# id, name, category, description, qtd, origin, unit_price, 
# total_price, tax_price, picture, thumbnail, barcode (signature)


db.define_table("product",
    Field("name", notnull=True),
    Field("category", "reference category", required=True),
    Field("description", "text"),
    Field("qtd", "integer", notnull=True),
    Field("origin", "string"),
    Field("unit_price", "double"),
    Field("total_price", "double"), # computed fields
    # campo virtual tax_price
    Field("picture", "upload"),
    Field("thumbnail", "upload"),
    Field("barcode", "string"),
    Field("featured", "boolean", default=False),
    auth.signature
    )

origins = {"BR": 1.0, "JP": 1.2, "EUA": 1.8, "UK": 1.5 }

# Order
# id, client, total_items, total_price, payment, (signature)  

# OrderItems
# id, order_id, product_id, unit_price, qtd, total_price (signature)


meus_menus = [
    {"title": "Home", "url": URL('home', 'index')},
    {"title": "Products", "url": URL('products', 'list')},
    {"title": "Cart", "url": URL('cart', 'show')},
    {"title": "Admin", "url": URL(a="admin")},
    {"title": "Contact", "url": URL('home', 'contact')},
]