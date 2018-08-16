# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------
# This scaffolding model makes your app work on Google App Engine too
# File is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

if request.global_settings.web2py_version < "2.14.1":
    raise HTTP(500, "Requires web2py 2.13.3 or newer")

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

#############################COMIENZO DE LA TABLA "PRODUCTOS"###################################
db.define_table('productos',
   Field('id_producto', 'string',),
   Field('codigo_barras', 'string'),
   Field('cantidad_prod','integer'),
   Field ('nombre','string'),
   Field ('marca','string'),
   Field('descripcion','string'),
   Field('envase','string'),
   Field ('categoria','string'),
   Field('precio','float'),
   Field('proveedor','string'),
   Field ('codigo_producto','string'),
   Field ('fecha_ingreso','string'),
   Field('numero_remito','integer'),
   Field('numero_lote','integer'),
   Field('imagen','upload'),
   Field('observaciones','text'),
                 )

#############################FIN DE LA TABLA "PRODUCTOS"#################################


#############################COMIENZO DE LA TABLA "VENTAS"###################################

db.define_table('ventas',
   Field('cantidad', 'string',),
   Field('id_venta', 'integer',),
   Field('id_producto', 'string',),
               )
#############################FIN DE LA TABLA "VENTAS"#################################


#############################COMIENZO DE LA TABLA "PROVEEDOR"###################################

db.define_table('proveedor',
   Field('nombre', 'string',),
   Field('telefono', 'integer',),
   Field('id_proveedor', 'string',),
   Field('direccion', 'string',),
               )
#############################FIN DE LA TABLA "PROVEEDOR"#################################


#############################COMIENZO DE LA TABLA "CATEGORIA"###################################

db.define_table('categorias',
   Field('nombre', 'string',),
   Field('id_categoria', 'string',),
   Field('descripcion', 'string',),
               )
#############################FIN DE LA TABLA "PROVEEDOR"#################################


#############################COMIENZO DE LA TABLA "cliente"###################################

db.define_table('cliente',
   Field("id_clientes","id"), 
   Field ('codigo_cliente','integer'),
   Field('nombre', 'string',),
   Field ('dni','integer',label=T ('DNI')),
   Field('telefono', 'string',),
   Field('direccion', 'string',),
   Field ('email','string'),  
   Field ('dni','integer',unique=True),
   Field('cuil','string'),
   Field('sexo', requires=IS_IN_SET(['Masculino', 'Femenino', 'Otro'])),
   Field('telefono','integer'),
   Field('direccion','string'),
   Field('localidad_cliente','string'),            )
#############################FIN DE LA TABLA "CLIENTE"###################################################
