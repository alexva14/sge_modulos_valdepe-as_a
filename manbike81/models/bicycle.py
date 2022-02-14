# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Bicycle(models.Model):
    _name = fields.Text()
    _description= fields.Text()
    _price= fields.Integer()
