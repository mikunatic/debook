from odoo import fields, models, api
from datetime import date
import datetime


class Rent(models.Model):
    _name = 'rent'

    customer_id = fields.Many2one('customer', string="Cliente")
    book_id = fields.Many2one('book', string="Livro", domain="[('rent_id','=',False)]")
    expire_selection = fields.Selection([('fortnight', '15 dias'),
                                         ('one_month', '1 mês'),
                                         ('two_months','2 meses')])
    expire_date = fields.Datetime()
    date_time_fixed = fields.Datetime(string="Data de Vencimento")
    state = fields.Selection([('rented','Alugado'),
                              ('pending','Devolução Pendente'),
                              ('expired','Devolvido'),
                              ], default='rented')

    # fazer função que calcula a data de vencimento de acordo com o selection
    @api.onchange('expire_selection')
    def calculate_expire(self):
        for rec in self:
            if rec.expire_selection == 'fortnight':
                date = datetime.datetime.now() + datetime.timedelta(days=15)
                date = date.replace(hour=0, minute=0, second=0, microsecond=0)
                date += datetime.timedelta(hours=17)
                rec.expire_date = date
            elif rec.expire_selection == 'one_month':
                date = datetime.datetime.now() + datetime.timedelta(days=30)
                date = date.replace(hour=0, minute=0, second=0, microsecond=0)
                date += datetime.timedelta(hours=17)
                rec.expire_date = date
            else:
                date = datetime.datetime.now() + datetime.timedelta(days=60)
                date = date.replace(hour=0, minute=0, second=0, microsecond=0)
                date += datetime.timedelta(hours=17)
                rec.expire_date = date
            rec.date_time_fixed = rec.expire_date + datetime.timedelta(hours=3)

    # fazer função que envia email para o customer quando o aluguel for vencido