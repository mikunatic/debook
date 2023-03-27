from odoo import fields, models


class Rent(models.Model):
    _name = 'rent'

    customer_id = fields.Many2one('customer', string="Customer")
    book_id = fields.Many2one('book', string="Book")
    expire_selection = fields.Selection([('fortnight', '15 days'),
                                         ('one_month', '1 month'),
                                         ('two_months','2 months')])
    expire_date = fields.Datetime()

    #fazer função que calcula a data de vencimento de acordo com o selection
    # def calculate_expire(self):
    #     for rec in self:
