# See LICENSE file for full copyright and licensing details.

from odoo import api,fields,models


PRODUCT_TYPE = ('machine', 'Machine')


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    @api.model
    def _setup_fields(self):
        
        cls = type(self)
        type_selection = cls._fields['type'].selection
        if PRODUCT_TYPE not in type_selection:
            tmp = list(type_selection)
            tmp.append(PRODUCT_TYPE)
            cls._fields['type'].selection = tuple(set(tmp))
        super()._setup_fields()
    
    program_name = fields.Char('Program name')
    mode = fields.Char("Mode")
    draft_number = fields.Char("Dra. Number")
    part_counter = fields.Char("Part Counter")
    cycle_time = fields.Float("Cycle Time")
    feed_override = fields.Char("Feed Override")
    rpm_override = fields.Char("RPM Override")
    machine_image_ids = fields.One2many('machine.image','machine_id','Machines')
    activity_log_ids = fields.One2many('activity.log','machine_id','Activity Logs')
    oee_ids = fields.One2many('overall.equipment.effectiveness','machine_id','OEE')
    qc_ids = fields.One2many('quality.control','machine_id','QC')