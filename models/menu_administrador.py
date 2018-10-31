response.logo = A(B('SystemShop'), XML('&trade;&nbsp;'),
                  _class="navbar-brand", _href="http://127.0.0.1:8000/SystemShop_github",
                  _id="web2py-logo")
response.title = request.application.replace('_', ' ').title()
response.subtitle = ''
response.title = request.application.replace('_', ' ').title()
response.subtitle = ''

# ----------------------------------------------------------------------------------------------------------------------
response.meta.author = myconf.get('app.author')
response.meta.description = myconf.get('app.description')
response.meta.keywords = myconf.get('app.keywords')
response.meta.generator = myconf.get('app.generator')

# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
response.google_analytics_id = None
# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menu_administrador = [
    (T('Inicio'), False, URL('default', 'index'), [])
]


######################################## FIN  DEL MENU ###############################################



response.menu_administrador += [
            (T('Reportes'), False, '#', [
                (T('Productos'), False, URL('reportes','reportes_productos' ),[]),
                (T('Empleados'), False, URL('reportes','reportes_empleados' ),[]),
                (T('Proveedores'), False, URL('reportes','reportes_proveedores' ),[]),
                (T('Clientes'), False, URL('reportes','reportes_clientes' ),[])


                ])]

response.menu_administrador += [
            (T('Altas'), False, '#', [
                (T('Productos'), False, URL('altas', 'alta_productos'),[]),
                (T('Empleados'), False, URL('altas', 'alta_empleados'),[]),
                (T('Proveedores'), False, URL('altas', 'alta_proveedor'),[]),
                (T('Clientes'), False,URL('altas', 'alta_clientes'),[]),
                (T('Altas Usuarios'), False, URL('altas', 'altas_usuario'),[])


                ])]

response.menu_administrador += [
            (T('Categorias'), False, URL('productos','index'), [
                (T('Almacen'), False, URL('productos', 'venta_productos'),[]),
                (T('Bebidas'), False, URL('productos', 'venta_bebidas'),[]),
                (T('Limpieza'), False, URL('productos', 'venta_limpieza'),[]),


        ])]

DEVELOPMENT_MENU = True


def _():

    
    app = request.application
    ctr = request.controller





if DEVELOPMENT_MENU:
    _()

if "auth" in locals():
    auth.wikimenu()
