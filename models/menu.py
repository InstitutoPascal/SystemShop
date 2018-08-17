# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# Customize your APP title, subtitle and menus here
# ----------------------------------------------------------------------------------------------------------------------

response.logo = A(B('SystemShop'), XML('&trade;&nbsp;'),
                  _class="navbar-brand", _href="http://127.0.0.1:8000/SystemShop",
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


DEVELOPMENT_MENU = True


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

#------------------------------------------------------------------------------------------------------------------------------------02-05-17

#---------------------------------------------------------------------------------------------------------------------------------------
response.menu += [
            (T('Altas'), False, URL('altas','index'), [
                (T('Productos'), False, URL('altas', 'alta_productos'),[]),
                (T('Empleados'), False, URL('altas', 'alta_empleados'),[]),
                (T('Proveedores'), False, URL('altas', 'alta_proveedor'),[]),
                (T('Clientes'), False,URL('altas', 'alta_clientes'),[])])]

response.menu += [
            (T('Reportes'), False, URL('reportes','index'), [
                (T('Productos'), False, URL('reportes','reportes_productos' ),[]),
                (T('Empleados'), False, URL('reportes','reportes_empleados' ),[]),
                (T('Ventas Online'), False, URL('reportes','reportes_venta_online' ),[]),
                (T('Ventas Local'), False, URL('reportes','reportes_venta_local' ),[]),
                (T('Proveedores'), False, URL('reportes','reportes_proveedores' ),[]),

                ])]

response.menu += [
            (T('Compras'), False, URL('compras','index'), [
                (T('Proveedores'), False, URL('compras', 'compras_proveedores'),[])])]

response.menu += [
            (T('ventas'), False, URL('ventas','index'), [
                (T('Ventas Local'), False, URL('ventas', 'venta_local'),[]),
                (T('Ventas Online'), False, URL('carrito', 'ver_producto'),[]),
        ])]

if DEVELOPMENT_MENU:
    _()

if "auth" in locals():
    auth.wikimenu()
