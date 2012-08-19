# -*- coding: utf-8 -*-

routers = dict(
    # base router
    BASE=dict(
        default_application='ecommerce',
    ),
    # app specific router
    ecommerce=dict(
            default_controller='home',
            default_function='index'
    )
)

# logging = 'print' # warning, error, debug


# routes_onerror = [
#     (r'ecommerce/404', r'/ecommerce/static/fail404.html'),
#     (r'ecommerce/*', r'/ecommerce/static/fail.html'),
#     (r'*/404', r'/ecommerce/static/cantfind.html'),
#     (r'*/*', r'/ecommerce/error/index'),
# ]

# error_message = ('<html><body>'
#                  '<strong>ERROR DETECTED </strong>'
#                  '<hr><span>DEU UM ERRO! </span>'
#                  '<h1 style="display:none">%s</h1>'
#                  '</body></html>')

# error_message_ticket = ('<html><body style="background:yellow"><h1>Internal error</h1>Ticket issued:'
#                         '<a href="/admin/default/ticket/%(ticket)s"'
#                         ' target="_blank">%(ticket)s</a>'
#                         '<h1>ERROR DETECTED</h1>'
#                         '</body></html>')
