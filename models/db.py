# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------
# This scaffolding model makes your app work on Google App Engine too
# File is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

#if request.global_settings.web2py_version < "2.14.1":
  #  raise HTTP(500, "Requires web2py 2.17.1 or newer")
if request.global_settings.web2py_version < "2.15.5":
    raise HTTP(500, "Requires web2py 2.15.5 or newer")

# -------------------------------------------------------------------------
# if SSL/HTTPS is properly configured and you want all HTTP requests to
# be redirected to HTTPS, uncomment the line below:
# -------------------------------------------------------------------------
# request.requires_https()

# -------------------------------------------------------------------------
# app configuration made easy. Look inside private/appconfig.ini
# -------------------------------------------------------------------------
from gluon.contrib.appconfig import AppConfig

# -------------------------------------------------------------------------
# once in production, remove reload=True to gain full speed
# -------------------------------------------------------------------------
myconf = AppConfig(reload=True)

if not request.env.web2py_runtime_gae:
    # ---------------------------------------------------------------------
    # if NOT running on Google App Engine use SQLite or other DB
    # ---------------------------------------------------------------------
    db = DAL(myconf.get('db.uri'),
             pool_size=myconf.get('db.pool_size'),
             migrate_enabled=myconf.get('db.migrate'),
             check_reserved=['all'])
else:
    # ---------------------------------------------------------------------
    # connect to Google BigTable (optional 'google:datastore://namespace')
    # ---------------------------------------------------------------------
    db = DAL('google:datastore+ndb')
    # ---------------------------------------------------------------------
    # store sessions and tickets there
    # ---------------------------------------------------------------------
    session.connect(request, response, db=db)
    # ---------------------------------------------------------------------
    # or store session in Memcache, Redis, etc.
    # from gluon.contrib.memdb import MEMDB
    # from google.appengine.api.memcache import Client
    # session.connect(request, response, db = MEMDB(Client()))
    # ---------------------------------------------------------------------

# -------------------------------------------------------------------------
# by default give a view/generic.extension to all actions from localhost
# none otherwise. a pattern can be 'controller/function.extension'
# -------------------------------------------------------------------------
response.generic_patterns = ['*'] if request.is_local else []
# -------------------------------------------------------------------------
# choose a style for forms
# -------------------------------------------------------------------------
response.formstyle = myconf.get('forms.formstyle')  # or 'bootstrap3_stacked' or 'bootstrap2' or other
response.form_label_separator = myconf.get('forms.separator') or ''

# -------------------------------------------------------------------------
# (optional) optimize handling of static files
# -------------------------------------------------------------------------
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'

# -------------------------------------------------------------------------
# (optional) static assets folder versioning
# -------------------------------------------------------------------------
# response.static_version = '0.0.0'

# -------------------------------------------------------------------------
# Here is sample code if you need for
# - email capabilities
# - authentication (registration, login, logout, ... )
# - authorization (role based authorization)
# - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
# - old style crud actions
# (more options discussed in gluon/tools.py)
# -------------------------------------------------------------------------

from gluon.tools import Auth, Service, PluginManager

# host names must be a list of allowed host names (glob syntax allowed)
auth = Auth(db, host_names=myconf.get('host.names'))
service = Service()
plugins = PluginManager()

# -------------------------------------------------------------------------
# create all tables needed by auth if not custom tables
# -------------------------------------------------------------------------

# after
# auth = Auth(globals(),db)
db.define_table(
    auth.settings.table_user_name,
    Field('dni', 'integer',label=T('DNI')),
    Field('first_name', length=128, default='', label=T('Nombres')),
    Field('last_name', length=128, default='',label=T('Apellido')),
    Field('email', length=128, default='', unique=True,label=T('Correo electrónico')),
    Field('username', length=128,label=T('Nombre de Usuario')),
    Field('password', 'password', length=512,
          readable=False, label=T('Password')),
    Field('registration_key', length=512,
          writable=False, readable=False, default=''),
)

custom_auth_table = db[auth.settings.table_user_name] # get the custom_auth_table
custom_auth_table.first_name.requires = IS_NOT_EMPTY(error_message=auth.messages.is_empty)
custom_auth_table.last_name.requires = IS_NOT_EMPTY(error_message=auth.messages.is_empty)
custom_auth_table.password.requires = [CRYPT()]
custom_auth_table.email.requires = [
  IS_EMAIL(error_message=auth.messages.invalid_email),
  IS_NOT_IN_DB(db, custom_auth_table.email)]
auth.settings.table_user = custom_auth_table # tell auth to use custom_auth_table
# before
# auth.define_tables()





# -------------------------------------------------------------------------
# create all tables needed by auth if not custom tables
# -------------------------------------------------------------------------
auth.define_tables(username=True, signature=False)

# -------------------------------------------------------------------------
# configure email
# -------------------------------------------------------------------------
mail = auth.settings.mailer
mail.settings.server = 'logging' if request.is_local else myconf.get('smtp.server')
mail.settings.sender = myconf.get('smtp.sender')
mail.settings.login = myconf.get('smtp.login')
mail.settings.tls = myconf.get('smtp.tls') or False
mail.settings.ssl = myconf.get('smtp.ssl') or False

# -------------------------------------------------------------------------
# configure auth policy
# -------------------------------------------------------------------------
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = True
auth.settings.reset_password_requires_verification = True
auth.settings.create_user_groups=False

# -------------------------------------------------------------------------
# Define your tables below (or better in another model file) for example
#
# >>> db.define_table('mytable', Field('myfield', 'string'))
#
# Fields can be 'string','text','password','integer','double','boolean'
#       'date','time','datetime','blob','upload', 'reference TABLENAME'
# There is an implicit 'id integer autoincrement' field
# Consult manual for more options, validators, etc.
#
# More API examples for controllers:
#
# >>> db.mytable.insert(myfield='value')
# >>> rows = db(db.mytable.myfield == 'value').select(db.mytable.ALL)
# >>> for row in rows: print row.id, row.myfield
# -------------------------------------------------------------------------

# -------------------------------------------------------------------------
# after defining tables, uncomment below to enable auditing
# -------------------------------------------------------------------------
# auth.enable_record_versioning(db)

db.define_table('productos',
   Field('id_producto', 'string',),
   Field('codigo_barras', 'string'),
   Field('cantidad','integer'),
   Field('nombre','string'),
   Field('marca','string'),
   Field('descripcion','string'),
   Field('categoria','string'),
   Field('precio','float'),
   Field('proveedor','string'),
   Field('codigo_producto','string'),
   Field('fecha_ingreso','date'),
   Field('numero_remito','integer'),
   Field('numero_lote','integer'),
   Field('alicuota_iva','float'),
   Field('imagen','upload'),
   Field('observaciones','text'),

                 )
db.productos.cantidad.requires=IS_NOT_EMPTY(error_message='Campo obligatorio')
db.productos.nombre.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(20, error_message='Solo hasta 20 caracteres'),IS_UPPER()
db.productos.marca.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_UPPER()
db.productos.categoria.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(16, error_message='Solo hasta 16 caracteres'),IS_UPPER()
db.productos.precio.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(6, error_message='Solo hasta 6 caracteres')
#db.productos.proveedor.requires=IS_IN_DB(db,db.proveedor,'%(nombre_empresa)s',) #subconsulta que obtiene datos de la tabla proveedor y campo codigo_proveedor
#,'%(field)s'  #permite mostrar el valor de un campo para que sea mas facil identificarlo 
#db.productos.fecha_ingreso.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.productos.numero_lote.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.productos.observaciones.requires=IS_LENGTH(200, error_message='Solo hasta 200 caracteres')
#############################COMIENZO DE LA TABLA "PROVEEDOR"###################################

db.define_table('proveedor',
   Field('nombre_empresa','string'),
   Field('codigo_proveedor','integer'),
   Field('nombre', 'string',),
   Field('telefono', 'integer',),
   Field('direccion', 'string',),
   Field('cuit_proveedor','string'),
   Field('codigo_postal','integer'),
   Field('localidad','string'),
   Field('provincia','string'),
   Field('pais','string'),
   Field('telefono','integer'),
   Field('email','string'),
   Field('estado',requires=IS_IN_SET(['activo','inactivo'])),
   Field('observaciones','text'),
                )
db.proveedor.codigo_proveedor.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(4, error_message='Solo hasta 4 caracteres')
db.proveedor.nombre_empresa.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_UPPER()
db.proveedor.cuit_proveedor.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(18, error_message='Solo hasta 13 caracteres')
db.proveedor.direccion.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(30, error_message='Solo hasta 15 caracteres')
db.clientes.codigo_postal.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(8, error_message='Solo hasta 8 caracteres')
db.proveedor.localidad.requires=IS_NOT_EMPTY(error_message='Campo obligatorio')
db.proveedor.provincia.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(30, error_message='Solo hasta 10 caracteres')
db.proveedor.pais.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(20, error_message='Solo hasta 20 caracteres')
db.proveedor.telefono.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(15, error_message='Solo hasta 15 caracteres')
db.proveedor.email.requires=IS_LENGTH(30, error_message='Solo hasta 30 caracteres')
#############################FIN DE LA TABLA "PROVEEDOR"#################################



#############################COMIENZO DE LA TABLA "cliente"###################################
##Clientes##
db.define_table ('clientes',
   Field('id_clientes','id'), 
   Field ('codigo_cliente','integer'),
   Field ('nombre','string'),
   Field ('apellido','string'),
   Field ('email','string'),  
   Field ('dni','integer',unique=True),
   Field('cuil','string'),
   Field('sexo', requires=IS_IN_SET(['Masculino', 'Femenino', 'Otro'])),
   Field('telefono','integer'),
   Field('direccion','string'),
   Field('localidad_cliente','string'),
   Field('tipo_categoria', requires=IS_IN_SET(['Resp. Inscr.','Monotributo'])),  
   Field ('provincia','string'),
   Field ('pais','string'),
   Field ('codigo_postal','integer'),
   Field('estado', requires=IS_IN_SET(['activo','inactivo'])),
   Field ('observaciones','text')
                )
db.clientes.nombre.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_UPPER(),IS_LENGTH(30)
db.clientes.apellido.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_UPPER(),IS_LENGTH(30)
db.clientes.dni.requires=IS_NOT_IN_DB (db,db.clientes.dni),IS_INT_IN_RANGE(2500000,100000000)
db.clientes.telefono.requires=IS_LENGTH(12, error_message='Solo hasta 12 caracteres')
#db.clientes.localidad_cliente.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_UPPER(),IS_LENGTH(50),IS_IN_DB(db,'localidad.nombre_localidad','%(nombre_localidad)s')
#db.clientes.direccion.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_UPPER(),IS_LENGTH(20)
#db.clientes.numero_calle.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(8, error_message='Solo hasta 8 caracteres')
db.clientes.provincia.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_UPPER()
db.clientes.pais.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_UPPER()
db.clientes.codigo_postal.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(8, error_message='Solo hasta 8 caracteres')

#############################FIN DE LA TABLA "CLIENTE"###################################################
##Categoria##

#db.define_table ('categorias',
#                db.Field('categoria','string'),
#                 primarykey=['categoria'] )
#db.categorias_prod.categoria.requires=IS_UPPER(),IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(8, error_message='Solo hasta 8 caracteres')

####################33########COMIENZO TABLA STOCK#########################################################
db.define_table ('stock',
   Field('codigo_producto','string'),
   Field ('nombre','string'),
   Field ('marca','string'),
   Field ('categoria','string'),
   Field('fecha_ingreso','date'),
   Field('fecha_salida','date')
                )
db.stock.categoria.requires=IS_UPPER(),IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(4, error_message='Solo hasta 4 caracteres')
db.stock.fecha_ingreso.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.stock.fecha_salida.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.stock.marca.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.stock.codigo_producto.requires=IS_UPPER(),IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(9, error_message='Solo hasta 9 caracteres',)
db.stock.nombre.requires=IS_UPPER(),IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
####################33########FIN TABLA STOCK #########################################################

####################33########COMIENZO TABLA COMPRAS#########################################################
db.define_table ('compras',
   Field('codigo_producto','string'),
   Field ('nombre','string'),
   Field ('marca','string'),
   Field ('categoria','string'),
   Field ('precio','integer'),
   Field('fecha_ingreso','string'),
   Field('proveedor','string'),
   Field('remito','string'),
   Field('cantidad','integer')
                )

####################33########FIN TABLA COMPRAS #########################################################
#############################COMIENZO DE LA TABLA EMPLEADOS#################################

db.define_table('empleado',
   Field('id_empleado', 'string',),
   Field('apellido', 'string',),
   Field('nombres','string',),
   Field ('dni','integer',label=T ('DNI')),
   Field('fecha_de_nacimiento', 'date',),
   Field('nacionalidad', 'string',),
   Field('sexo', 'string',),
   Field('localidad', 'string',),
   Field('sector','string'),
   Field('correo_electronico', 'string',label=T('Correo Electrónico',)),
   Field('ocupado','string',)
               )
db.empleados.id_empleados.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(4, error_message='Solo hasta 4 caracteres'),IS_NOT_IN_DB (db,db.empleados.codigo_empleados)
db.empleados.dni.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio') ,IS_INT_IN_RANGE(2500000,100000000, error_message= 'Ingrese un DNI entre 2.500.000 y 100.000.000')
db.empleados.apellido.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(30, error_message='Solo hasta 30 caracteres'),IS_UPPER()
db.empleados.nombres.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(30, error_message='Solo hasta 30 caracteres'),IS_UPPER()
db.empleados.correo_electronico.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(50, error_message='Solo hasta 50 caracteres')
db.empleados.direccion.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(50, error_message='Solo hasta 50 caracteres'),IS_UPPER()
db.empleados.localidad.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(50, error_message='Solo hasta 50 caracteres')
db.empleados.codigo_postal.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(6, error_message='Solo hasta 6 caracteres')
db.empleados.provincia.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(30,error_message='Solo hasta 30 caracteres')
db.empleados.pais.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(20, error_message='Solo hasta 20 caracteres')
db.empleados.telefono.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(20, error_message='Solo hasta 20 caracteres')
db.empleados.fecha_ingreso.requires=IS_NOT_EMPTY(error_message='Campo obligatorio')
db.empleados.sector.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(20, error_message='Solo hasta 20 caracteres')
