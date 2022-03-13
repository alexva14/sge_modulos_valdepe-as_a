# -*- coding: utf-8 -*-

from datetime import date
from random import randint
from odoo import models, fields, api
from pyrsistent import field
from odoo.exceptions import ValidationError
import re



class bicycle(models.Model):
     _name = 'manbike81.bicycle'
     _description = 'manbike81.bicycle'

     name = fields.Char(string="Modelo", required=True)
     help="Modelo exacto de bicicleta sin fabricación"
     description = fields.Text(string="Descripcion")
     precio= fields.Float(string="Precio", required=True)
     inShop=fields.Date(string="Entrada en tienda", default=lambda self:date.today())
     year= fields.Integer(string="Año", default=2021)
     chainring=fields.Integer(string="Nº de paltos", default=1)
     cassette= fields.Integer(string="Nº de piñones")
     speed= fields.Integer(string="Nº de velocidades", compute="_cal_speed", store=True)
     wheel= fields.Selection([('tipo26', '26\"'),('tipo27', '27.5\"'),('tipo29', '29\"')], string="Diametro Rueda")

     single_chainring= fields.Boolean(string="Monoplato", compute="_set_single_chainring", store=True)
     photo=fields.Image(string="Fotografia", max_width=400, max_height=400)
     manufacturer= fields.Many2one("manbike81.manufacturer", string="Fabricante")
     trader= fields.Many2many("manbike81.trader", related= "manufacturer.trader" , string="Comerciales", readonly=True)
     discount=fields.Boolean(string="Descuento", readonly=True, default=False)
     delivery= fields.Many2one("manbike81.delivery", string="Paqueteria")
     end_date= fields.Date(string="Fecha Fin", store=True, default=lambda self:date.today())

     def calc_discount(self):
               for bike in self:
                    if bike.discount !=True:
                         try:
                              bike.precio=bike.precio-bike.precio*0.1
                              bike.discount=True
                         except:
                              raise ValidationError("Discount can´t be applied")
                    else:
                         raise ValidationError("Discount can´t be applied")
     

     @api.depends("chainring", "cassette")
     def _cal_speed(self):
          print("--->>>", type(self))
          print("--->>>", self)
          for bike in self:
               print("\t----->>>", bike.name)
               try:
                    bike.speed=bike.chainring*bike.cassette
               except:
                    bike.speed=1

     @api.depends("chainring")
     def _set_single_chainring(self):
          for bike in self:
               if(bike.chainring==1):
                    bike.single_chainring=True
               else:
                    bike.single_chainring=False
               print("\t----->>>", bike.chainring)


class manufacturer(models.Model):
     _name = 'manbike81.manufacturer'
     _description = 'manbike81.manufacturer'

     name = fields.Char(string= "Fabricante", required=True)
     web = fields.Char(string="Web")
     bicycles= fields.One2many("manbike81.bicycle", "manufacturer")
     trader= fields.Many2many("manbike81.trader", string="Comerciales")
     trader_main= fields.One2many("manbike81.trader", "manuf_main", string="Sol principal de:")

class trader(models.Model):
     _name = 'manbike81.trader'
     _description = 'manbike81.trader'

     name= fields.Char(string="Comercial", required=True)
     phone=fields.Char(string="Telefono")
     dni = fields.Char(string="DNI")
     manuf_main=fields.Many2one("manbike81.manufacturer", string= "Fabricante principal",  compute="_set_manuf_main", store=True)

     manufacturer= fields.Many2many("manbike81.manufacturer", string="Fabricante")
     
     @api.constrains("dni")
     def _validate_dni(self):
        DNI_REGEX = '^(\d{8})([A-Z])$'
        for trade_current in self: 
            if not trade_current.dni:
                print("----_validate_dni >>> DNI: Not Value")
            else: 
                print("----")
                if re.match(DNI_REGEX, trade_current.dni, re.I) == None:
                    raise ValidationError("DNI: Not valid")
                else: 
                    print("---_validate_dni >>> DNI: Valid")
                    
                    #if (self._exist_dni(trade_current.dni)):
                     #    raise ValidationError("DNI: ALREADY EXIST")
                    #else:
                     #    print("---_validate_dni DNI: Valid and don´t exist")
     _sql_constraints=[("dni_uniq", "unique(dni)", "DNI: ALREADY EXIST")]
     
     def _exist_dni(self, dni_to_check):
          print(self)
          all_trades= self.env["manbike81.trader"].search([])
          print("-------_exist_dni>>>>>", type(all_trades))
          print("-------_exist_dni>>>>>", all_trades)
          for at in all_trades:
               if at.dni == dni_to_check and at.id != self.id:
                    return True
          return False


     @api.constrains("phone")
     def _validate_phone(self):
          PHONE_REGEX = '^(6|7|8|9)([0-9]){8}$'
          for trade_current in self:
               if not trade_current.phone:
                    print("---validate PHONE not value")
               else:
                    if re.match(PHONE_REGEX, trade_current.phone)==None:
                         raise ValidationError("PHONE: Not valid")
                    else:
                         print("-----PHONE VALIDO")

     @api.depends("manufacturer")
     def _set_manuf_main(self):
          for trader in self:
               size_man=len(trader.manufacturer)
               if(size_man>0):
                    pos=randint(0, size_man-1)
                    trader.manuf_main=trader.manufacturer[pos].id
               else:
                    trader.manuf_main=None

class delivey(models.Model):
     _name = 'manbike81.delivery'
     _description = 'The Delivery'

     name= fields.Char(string="Empresa", required=True)
     price=fields.Float(string="Precio")
     shipment_days = fields.Integer(string="Núm. días de envio")

class member(models.Model):
     _name = 'manbike81.member'
     _description = 'The Member'

     name=fields.Char(string="Nombre y Apellido", required=True)
     dni = fields.Char(string="DNI")



     @api.constrains("dni")
     def _validate_dni(self):
        DNI_REGEX = '^(\d{8})([A-Z])$'
        for trade_current in self: 
            if not trade_current.dni:
                print("----_validate_dni >>> DNI: Not Value")
            else: 
                print("----")
                if re.match(DNI_REGEX, trade_current.dni.upper(), re.I) == None:
                    raise ValidationError("DNI: Not valid")
                else: 
                    print("---_validate_dni >>> DNI: Valid")
                    
                    #if (self._exist_dni(trade_current.dni)):
                     #    raise ValidationError("DNI: ALREADY EXIST")
                    #else:
                     #    print("---_validate_dni DNI: Valid and don´t exist")
     _sql_constraints=[("dni_uniq", "unique(dni)", "DNI: ALREADY EXIST")]
     
     def _exist_dni(self, dni_to_check):
          print(self)
          all_member= self.env["manbike81.member"].search([])
          print("-------_exist_dni>>>>>", type(all_member))
          print("-------_exist_dni>>>>>", all_member)
          for at in all_member:
               if at.dni == dni_to_check and at.id != self.id:
                    return True
          return False

#    value = fields.Integer()
#    value2 = fields.Float(compute="_value_pc", store=True)
#    description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
