from odoo import fields, models


class City(models.Model):
    _name = 'city'

    name = fields.Char()