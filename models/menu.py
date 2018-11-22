# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# Customize your APP title, subtitle and menus here
# ----------------------------------------------------------------------------------------------------------------------

response.logo = A(B('SystemShop'), XML('&trade;&nbsp;'),
                  _class="navbar-brand", _href="http://127.0.0.1:8000/SystemShop_github",
                  _id="web2py-logo")
response.title = request.application.replace('_', ' ').title()
response.subtitle = ''

# ----------------------------------------------------------------------------------------------------------------------
# read more at http://dev.w3.org/html5/markup/meta.name.html
# ----------------------------------------------------------------------------------------------------------------------
response.meta.author = myconf.get('app.author')
response.meta.description = myconf.get('app.description')
response.meta.keywords = myconf.get('app.keywords')
response.meta.generator = myconf.get('app.generator')

# ----------------------------------------------------------------------------------------------------------------------
# your http://google.com/analytics id
# ----------------------------------------------------------------------------------------------------------------------
response.google_analytics_id = None

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menu = [
    (T('Inicio'), False, URL('default', 'index'), [])
]


# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. remove in production
# ----------------------------------------------------------------------------------------------------------------------


response.menu += [
            (T('Categorias'), False, URL('productos','index'), [
                (T('Almacen'), False, URL('productos', 'venta_productos'),[]),
                (T('Bebidas'), False, URL('productos', 'venta_bebidas'),[]),
                (T('Limpieza'), False, URL('productos', 'venta_limpieza'),[]),


        ])]

response.menu += [
                (T('Almacen'), False, URL('productos', 'venta_productos'),[
        ])]
response.menu += [

                (T('Bebidas'), False, URL('productos', 'venta_bebidas'),[

        ])]
response.menu += [
                (T('Limpieza'), False, URL('productos', 'venta_limpieza'),[

        ])]
DEVELOPMENT_MENU = True

#if auth.has_membership("Administrador"):

# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. remove in production
# ----------------------------------------------------------------------------------------------------------------------
def _():
    # ------------------------------------------------------------------------------------------------------------------
    # shortcuts
    # ------------------------------------------------------------------------------------------------------------------
    app = request.application
    ctr = request.controller
    # ------------------------------------------------------------------------------------------------------------------
    # useful links to internal and external resources
    # ------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------
