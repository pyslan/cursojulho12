#coding: utf-8

from customvalidators import IS_VALID_BARCODE
from thumb import THUMB

# validadores para tabelas

db.product.description.requires = \
   IS_NOT_EMPTY(error_message="Insira uma description")
db.product.barcode.requires = \
   [
   IS_NOT_EMPTY(error_message="Insira um barcode"),
   IS_VALID_BARCODE("987", T("BARCODE INVALID"))
   ]

# IS_IN_SET([(1, "um"),
#             (2, "dois"),
#             (3, "tres")])

db.product.origin.requires = IS_IN_SET(origins.keys())

# computations

db.product.total_price.compute = \
    lambda row: float(row.unit_price) * float(row.qtd)

db.product.thumbnail.compute = \
   lambda row: THUMB(row.picture, (200, 200))

# form widgets
# visibility
# campos virtuais
# funcoes de validators
# validadores customizados