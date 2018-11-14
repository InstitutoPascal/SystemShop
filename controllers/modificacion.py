def editar_cliente():
    # obtengo el primer argumento (ver URL)
    id_cliente = request.args[0]
    # busco el registro en la bbdd
    cliente =  db(db.clientes.id == id_cliente).select().first()
    # armo el formulario para modificar este registro:
    form=SQLFORM(db.clientes, cliente)
    if form.accepts(request.vars, session):
        session.flash = 'Formulario correctamente cargado'
        # redirijo al usuario al listado
        redirect(URL(c="reportes", f="reportes_clientes"))
    elif form.errors:
		response.flash = 'Su formulario contiene errores, porfavor modifiquelo'
    else:
		response.flash = 'Por favor rellene el formulario'
    return dict(f=form)


# Editar Cliente --------------------------------------------------------------------------------------------
def editar_proveedor():
    # obtengo el primer argumento (ver URL)
    id_proveedor = request.args[0]
    # busco el registro en la bbdd
    proveedor =  db(db.proveedor.id == id_proveedor).select().first()
    # armo el formulario para modificar este registro:
    form=SQLFORM(db.proveedor, proveedor)
    if form.accepts(request.vars, session):
        session.flash = 'Formulario correctamente cargado'
        # redirijo al usuario al listado
        redirect(URL(c="reportes", f="reportes_clientes"))
    elif form.errors:
		response.flash = 'Su formulario contiene errores, porfavor modifiquelo'
    else:
		response.flash = 'Por favor rellene el formulario'
    return dict(f=form)


def editar_producto():
    producto = db(db.producto.id==request.args(0)).select()
    id_producto = producto[0]
    form = SQLFORM(db.producto, id_producto, deletable=False)
    if form.accepts(request.vars, session):
        session.flash = " Los datos modificados se guardarán en la Base de Datos"
        redirect(URL(c= 'reportes', f='reportes_productos'))

    return dict( form=form)
