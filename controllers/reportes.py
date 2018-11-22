# -*- coding: utf-8 -*-
# intente algo como
# ReportesClientes-------------------------------------------------------------------------------------------------------------

def reportes_clientes():
    subtitulo=T('Listado de Clientes')
    listado =db(db.clientes).select(db.clientes.ALL)
    return dict(dc=listado)
#-------------------------------------------------------------------------------------------------------------------------------------
# ReportesProveedores

def reportes_proveedores():
    subtitulo=T('Listado de Proveedores')
    listado =db(db.proveedor).select(db.proveedor.ALL)
    return dict(dc=listado)
#------------------------------------------------------------------------------------------------------------------------------------------------------
#reportes por productos
def reportes_productos():
    subtitulo=T('Listado de Productos')
    listado =db(db.producto).select(db.producto.ALL)
    return dict(dc=listado)

#------------------------------------------------------------------------------------------------------------------------------------------------------------#Reportes de empleados

def reportes_empleados():
    subtitulo=T('Listado de Empleados')
    listado =db(db.empleado).select(db.empleado.ALL)
    return dict(dc=listado)


#------------------------------------------------------------------------------------------------------------------------------------------------------------#Reportes de VentasOnline
def reportes_venta_online():

    return dict()
#------------------------------------------------------------------------------------------------------------------------------------------------------------#Reportes de Remitos
def reportes_remitos():

    return dict()
#------------------------------------------------------------------------------------------------------------------------------------------------------------#Reportes de Remitos
def remitos_detalles():

    return dict()
