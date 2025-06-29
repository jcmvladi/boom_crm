# -*- coding: utf-8 -*-
# from odoo import http


# class BoomCrm(http.Controller):
#     @http.route('/boom_crm/boom_crm', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/boom_crm/boom_crm/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('boom_crm.listing', {
#             'root': '/boom_crm/boom_crm',
#             'objects': http.request.env['boom_crm.boom_crm'].search([]),
#         })

#     @http.route('/boom_crm/boom_crm/objects/<model("boom_crm.boom_crm"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('boom_crm.object', {
#             'object': obj
#         })

