# -*- coding: utf-8 -*-
# from odoo import http


# class Manbike81(http.Controller):
#     @http.route('/manbike81/manbike81/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/manbike81/manbike81/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('manbike81.listing', {
#             'root': '/manbike81/manbike81',
#             'objects': http.request.env['manbike81.manbike81'].search([]),
#         })

#     @http.route('/manbike81/manbike81/objects/<model("manbike81.manbike81"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('manbike81.object', {
#             'object': obj
#         })
