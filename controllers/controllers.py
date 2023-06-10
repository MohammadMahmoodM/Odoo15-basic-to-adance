# -*- coding: utf-8 -*-
# from odoo import http


# class OmHospitall(http.Controller):
#     @http.route('/om_hospitall/om_hospitall', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/om_hospitall/om_hospitall/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('om_hospitall.listing', {
#             'root': '/om_hospitall/om_hospitall',
#             'objects': http.request.env['om_hospitall.om_hospitall'].search([]),
#         })

#     @http.route('/om_hospitall/om_hospitall/objects/<model("om_hospitall.om_hospitall"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('om_hospitall.object', {
#             'object': obj
#         })
