from ConfigParser import SafeConfigParser
import time

def index():
    regs = db(db.productos.id_producto>0).select()
    return dict(productos=regs)
