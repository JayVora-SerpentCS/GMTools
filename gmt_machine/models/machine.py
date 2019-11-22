# See LICENSE file for full copyright and licensing details.

from odoo import api,fields,models


#PRODUCT_TYPE = ('machine', 'Machine')


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    type = fields.Selection(selection_add=[('machine', 'Machine')])
    program_name = fields.Char('Program name')
    mode = fields.Char("Mode")
    draft_number = fields.Char("Dra. Number")
    part_counter = fields.Char("Part Counter")
    cycle_time = fields.Float("Cycle Time")
    feed_override = fields.Char("Feed Override")
    rpm_override = fields.Char("RPM Override")
    machine_image_ids = fields.One2many('machine.image','machine_id','Machines')

