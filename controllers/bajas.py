def borrar_cliente():
    # obtengo el primer argumento (ver URL)
    id_cliente = request.args[0]
    # busco y borro el registro
    db(db.clientes.id == id_clientes).delete()
    session.flash = "El cliente %s se borro exitosamente" % id_clientes
    # redirijo al usuario al listado
    redirect(URL(c="reportes", f="reportes_clientes"))
