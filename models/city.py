from odoo import fields, models


class City(models.Model):
    _inherit = 'res.city'

    ibge_code = fields.Char()