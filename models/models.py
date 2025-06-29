# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class boom_crm(models.Model):
#     _name = 'boom_crm.boom_crm'
#     _description = 'boom_crm.boom_crm'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from datetime import date
from odoo import models, fields, api

class Boom(models.Model):
    _inherit = 'crm.lead'
    
    x_lead_category = fields.Selection([
        ('residencial', 'Residencial'),
        ('empresarial', 'Empresarial'),
        ('gubernamental', 'Gubernamental')
    ], string='Categoría de Lead', tracking=True) # Campo de selección para la categoría
    x_delivery_deadline = fields.Date(string='Fecha Límite para Procesar', tracking=True) # Campo de fecha para la fecha límite de procesamiento
    x_approved_by = fields.Many2one('res.users', string='Aprobado Por', tracking=True, readonly=True) # Campo muchos a uno relacionado con res.users para el aprobador 
    x_approved_date = fields.Date(string='Fecha de Aprobación', tracking=True) # Campo de fecha para la fecha de aprobación
    x_duration_since_approved = fields.Integer(
        string='Duración Desde Aprobación (Días)',
        compute='_compute_duration_since_approved',
        store=True,
        readonly=True,
        help="Tiempo transcurrido en días desde que el lead fue aprobado."
    ) # Campo para la duración desde la aprobación, se recalcula cada vez que cambia x_approved_date
    x_installation_required = fields.Boolean(string='Requiere Instalación Técnica', tracking=True) # Campo para indicar si requiere instalación
    x_installation_date = fields.Date(string='Fecha Programada de Instalación/Entrega', tracking=True) # Campo para la fecha de instalación
    x_contract_reference = fields.Char(string='Referencia de Contrato', tracking=True) # Campo para la referencia del contrato 
    x_support_required = fields.Boolean(string='Requiere Soporte Postventa', tracking=True) # Campo para indicar si requiere soporte postventa

    @api.depends('x_approved_date')
    def _compute_duration_since_approved(self):
        for record in self:
            if record.x_approved_date:
                delta = date.today() - record.x_approved_date
                record.x_duration_since_approved = delta.days
            else:
                record.x_duration_since_approved = 0

    def action_approve_lead(self):
        for record in self:
            if not record.x_approved_by:
                record.x_approved_by = self.env.user.id 
                record.x_approved_date = date.today() 
                record.x_delivery_deadline = date.today() 
                record.message_post(body=f"Lead aprobado por {self.env.user.name} el {record.x_approved_date}.")