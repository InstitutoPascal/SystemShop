#alta_proveedor
def alta_proveedor():
    form = SQLFORM(db.proveedor)
    if form.accepts(request.vars, session):
        response.flash = 'Formulario aceptado'
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Complete el formulario'
    return dict(f=form)

#alta_producto
def alta_productos():
    form = SQLFORM(db.productos)
    if form.accepts(request.vars, session):
        response.flash = 'Formulario aceptado'
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Complete el formulario'
    return dict(f=form)

#alta_empleado
def alta_empleados():
    form = SQLFORM(db.empleados)
    if form.accepts(request.vars, session):
        response.flash = 'Formulario aceptado'
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Complete el formulario'
    return dict(f=form)

#alta_cliente
def alta_clientes():
    form = SQLFORM(db.clientes)
    if form.accepts(request.vars, session):
        response.flash = 'Formulario aceptado'
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Complete el formulario'
    return dict(f=form)
#alta usuario
def altas_usuario():
    subtitulo=T('Listado de Usuarios Registrados Pendientes de Aprobación - Sistema de Datos Preocupacionales')#Asigna mensaje a mostrar
    nombre=auth.user.first_name
    apellido=auth.user.last_name
    registrados = db(db.auth_user.registration_key == 'pending').select(db.auth_user.ALL)
    return dict(subtitulo=subtitulo, nombre=nombre, apellido=apellido, registrados=registrados)

###################################FIN FUNCION usuario para daministrador ###################################################

#definir rol

def definir_rol():
    grupo_elegido=db(request.args(1)==db.auth_group.role).select(db.auth_group.id)
    for x in grupo_elegido:
        clave=x.id
    cd=db.auth_membership.insert(user_id=request.args(0),group_id=clave)
    usuario=db(request.args(0)==db.auth_user.id).select(db.auth_user.ALL)
    reg=usuario[0]
    reg.update_record(registration_key='')
    redirect(URL('altas_usuario'))
    return dict()

###################################FIN FUNCION AGREGAR usuario para daministrador ###################################################
