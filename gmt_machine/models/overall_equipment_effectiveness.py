# See LICENSE file for full copyright and licensing details.

from odoo import fields,models


class OverallEquipmentEffectiveness(models.Model):
    _name = 'overall.equipment.effectiveness'

    machine_id = fields.Many2one('product.template','Machine',domain=[('type', '=', 'machine')])
    oee_type = fields.Selection([('run time','Run time'),('idle time','Idle time'),('down time','Down time')],'OEE Type')
    oee_time_duration = fields.Float("Time Duration")

