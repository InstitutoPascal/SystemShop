from ConfigParser import SafeConfigParser
import time
#prducto.html
def producto():
    if request.vars["producto"]:
        # obtengo los valores del formulario
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


#ver_producto.html
def ver_producto():
    regs = db(db.productos.id_producto>0).select()
    return dict(productos=regs)

def mostrar():
    #obtengo el id de prodcuto desde la URL
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

def ver():
   # obtengo el id de prodcuto desde la URL
    prod_id = request.args[0]
   # consultamos a la bd para que traiga el registro del primer producto:
    reg = db(db.productos.id_producto==prod_id).select().first()
    return dict(productos=reg)
