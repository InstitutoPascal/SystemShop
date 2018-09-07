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
auth.define_tables(username=False, signature=False)

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
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

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
   Field('fecha_ingreso','string'),
   Field('numero_remito','integer'),
   Field('numero_lote','integer'),
   Field('alicuota_iva','float'),
   Field('imagen','upload'),
   Field('observaciones','text'),

                 )

#############################COMIENZO DE LA TABLA "PROVEEDOR"###################################

db.define_table('proveedor',
   Field('id_proveedor', 'string',),
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
   Field('pagina_web','string'),
   Field('estado',requires=IS_IN_SET(['activo','inactivo'])),
   Field('observaciones','text'),
                )
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
   Field('tipo_categoria', requires=IS_IN_SET(['Resp. Inscr.','Monotributo'])),  #agregada by enrique
   Field ('provincia','string'),
   Field ('pais','string'),
   Field ('codigo_postal','integer'),
   Field('estado', requires=IS_IN_SET(['activo','inactivo'])),
   Field ('observaciones','text')
                )


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
   Field('fecha_ingreso','string'),
   Field('fecha_salida','string')
                )

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
db.define_table('empleados',
   Field('usuario_id', db.auth_user, default=auth.user_id ),
   Field('codigo_empleados','integer'),
   Field('dni','integer'),
   Field('apellido','string'),
   Field('nombre','string'),
   Field('usuario','string'),
   Field('password','password'),
   Field('email','string'),
   Field('direccion', 'string'),
   Field('localidad','string'),
   Field('codigo_postal','integer'),
   Field('provincia','string'),
   Field('pais','string'),
   Field('telefono','string'),
   Field('fecha_ingreso','date'),
   Field('estado', requires=IS_IN_SET(['activo','inactivo'])),
   Field('cargo','string'),
   Field('sector','string'),)
