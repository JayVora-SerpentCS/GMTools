# See LICENSE file for full copyright and licensing details.

from odoo import fields,models


class QualityControl(models.Model):
    _name = 'quality.control'

    machine_id = fields.Many2one('product.template','Machine',domain=[('type', '=', 'machine')])    
    error_number = fields.Integer('Error Number')
    error_time = fields.Float("Time")
    error_date = fields.Date("Date")

