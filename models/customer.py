from odoo import fields, models


class Customer(models.Model):
    _name = 'customer'

    name = fields.Char("Name")
    cpf = fields.Char()
    email = fields.Char()
    city = fields.Char()
    cep = fields.Char()
    state = fields.Many2one('res.country.state')
    country = fields.Many2one('res.country', default=31)
    rent_ids = fields.One2many(comodel_name="rent", inverse_name="customer_id", readonly=True)