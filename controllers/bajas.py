def borrar_cliente():
    # obtengo el primer argumento (ver URL)
    id_cliente = request.args[0]
    # busco y borro el registro
    db(db.clientes.id == id_clientes).delete()
    session.flash = "El cliente %s se borro exitosamente" % id_clientes
    # redirijo al usuario al listado
    redirect(URL(c="reportes", f="reportes_clientes"))

    
def borrar_producto():
    # obtengo el primer argumento (ver URL)
    id_producto = request.args[0]
    # busco y borro el registro
    db(db.productos.id == id_producto).delete()
    session.flash = "El producto %s se borro exitosamente" % id_producto
    # redirijo al usuario al listado
    redirect(URL(c="reportes", f="reportes_productos"))

    
def borrar_proveedor():
    # obtengo el primer argumento (ver URL)
    id_proveedor = request.args[0]
    # busco y borro el registro
    db(db.proveedor.id == id_proveedor).delete()
    session.flash = "El proveedor %s se borro exitosamente" % id_proveedor
    # redirijo al usuario al listado
    redirect(URL(c="reportes", f="reportes_proveedores"))

    
def borrar_empleado():
    # obtengo el primer argumento (ver URL)
    id_empleados = request.args[0]
    # busco y borro el registro
    db(db.empleado.id == id_empleado).delete()
    session.flash = "El empleado %s se borro exitosamente" % id_empleados
    # redirijo al usuario al listado
    redirect(URL(c="reportes", f="reportes_empleados"))
