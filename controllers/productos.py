#Funcion de almacen
def venta_productos():

    # buscar todos los productos:
    condicion = db.productos.marca == 'almacen'
    campos = db.productos.nombre, db.productos.id_producto, db.productos.descripcion, db.productos.precio
    registros = db(condicion).select(*campos)
    return dict(registros=registros)

#Funcion de bebidas
def venta_bebidas():

    # buscar todos los productos:
    condicion = db.productos.marca == 'bebidas'
    campos = db.productos.nombre, db.productos.id_producto, db.productos.descripcion, db.productos.precio
    registros = db(condicion).select(*campos)
    return dict(registros=registros)

#Funcion de menu limpieza
def venta_limpieza():

    # buscar todos los productos:
    condicion = db.productos.marca == 'limpieza'
    campos = db.productos.nombre, db.productos.id_producto, db.productos.descripcion, db.productos.precio
    registros = db(condicion).select(*campos)
    return dict(registros=registros)


#Funcion del carrito
def carrito():
    # obtengo los valores del formulario
    if request.vars["producto"]:
        id_prod = request.vars["producto"]
        cantidad = request.vars["cantidad"]
        print "este es el id", id_prod
        # revisar que request.vars.codigo cumpla con las validaciones
        #session.codigo_barras = request.vars.id_producto
        # buscamos el producto en la base datos
        #cantidad = request.vars["cantidad"]
        item = {"id_producto": id_prod, "cantidad": int(cantidad)}
        # busco en la base de datos el registro del producto seleccionado
        reg_producto = db(db.productos.id_producto==id_prod).select().first()
        item["descripcion"] = reg_producto.nombre
        item["precio"] = reg_producto.precio
        item["alicuota_iva"] = reg_producto.alicuota_iva
        # si no está definida la lista de items, lo creamos vacia en la sesión:
        if "items_venta" not in session:
            session["items_venta"] = []
        # guardo el item en la sesión
        session["items_venta"].append(item)
        #print"usuario ",session["vendedor_logueado"]
    return dict(items_venta=session["items_venta"])

def confirmar():
    #reg_cliente = db(db.clientes.id==session["id_cliente"]).select().first()
    total = 0
    for item in session["items_venta"]:
        total += (item["precio"] * item["cantidad"] + item["precio"] * item["cantidad"] *item["alicuota_iva"]/100.00)
    return dict (mensaje= "Finalizar venta", total=total)

def borrar_item():
    # eliminar el elemento de la lista en posicion pos
    del session["items_venta"][int(request.vars.pos)]
    return dict()

def mostrar():
    # obtengo el id de prodcuto desde la URL
    prod_id = request.args[0]
    # consultamos a la bd para que traiga el registro del primer producto:
    reg = db(db.productos.id_producto==prod_id).select(db.productos.imagen).first()
    # obtenemos la imagen (nombre de archivo completo, stream=flujo de datos=archivo abierto -open-):
    (filename, stream) = db.productos.imagen.retrieve(reg.imagen)
    # obtenemos extension original para determinar tipo de contenido:
    import os.path
    ext = os.path.splitext(filename)[1].lower()
    if ext in (".jpg", ".jpeg", ".face"):
        formato = "image/jpeg"
    elif ext in (".png"):
        formato = "image/png"
    response.headers['Content-Type'] = formato
    # devolver al navegador el contenido de la image
    return stream


def cancelar_venta():
    del session["items_venta"]
    return dict()
