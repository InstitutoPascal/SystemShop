# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------


def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    nombre_rol='SIN ROL'
    if auth.user_id:#esta variable tiene el id del usuario que se registro.
        reg_id_del_logueado= db(auth.user.id==db.auth_membership.user_id).select(db.auth_membership.group_id)
        id_grupo_del_logueado= reg_id_del_logueado[0].group_id
        reg_nombre_rol= db(db.auth_group.id==id_grupo_del_logueado).select(db.auth_group.role)
        nombre_rol=reg_nombre_rol[0].role
        response.flash = T("Bienvenido/a ")
        if nombre_rol=='Administrador':
            redirect (URL('principal_administrador'))
        elif nombre_rol=='Clientes':
            redirect (URL('principal_clientes'))
    return dict(message=T('Bienvenido al Sistema!'))


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

def principal_administrador():
    
    return dict()
