# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class CarMaintenance(models.Model):
    _name = 'car.maintenance'
    _description = 'Manage services performed to cars'
    _rec_name = "car_plate"

    car_plate = fields.Char('Car Plate',required=True)
    partner_id = fields.Many2one('res.partner', string='Client',required=True)
    amount_service = fields.Float('Amount Service',required=True)
    date_service = fields.Date('Date Service')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_process', 'In Process'),
        ('invoiced', 'Invoiced'),
        ('finalized', 'Finalized')
    ], string='state',default='draft')

    service_ids = fields.One2many('car.maintenance.services', 'car_maintenance_id', string='Services')

    



class CarMaintenanceServices(models.Model):
    _name = 'car.maintenance.services'
    _description = 'Manage services performed to cars'


    product_id = fields.Many2one('product.template', string='Service',
    domain=[('detailed_type','=','service')])


    car_maintenance_id = fields.Many2one('car.maintenance', string='Car Maintenance')
