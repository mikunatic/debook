from odoo import fields, models, api
import datetime


class Rent(models.Model):
    _name = 'rent'

    customer_id = fields.Many2one('customer', string="Cliente")
    book_id = fields.Many2one('book', string="Livro", domain="[('rent_id','=',False)]")
    expire_selection = fields.Selection([('fortnight', '15 dias'),
                                         ('one_month', '1 mês'),
                                         ('two_months','2 meses')], string="Seleção de Vencimento")
    expire_date = fields.Datetime()
    date_time_fixed = fields.Datetime(string="Data de Vencimento")
    state = fields.Selection([('rented','Alugado'),
                              ('pending','Devolução Pendente'),
                              ('returned','Devolvido'),
                              ], compute="expire")

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

    @api.model
    def create(self, vals_list):
        vals_list['state'] = 'rented'
        return super(Rent, self).create(vals_list)

    @api.depends('expire_date')
    def expire(self):
        for rec in self:
            now = datetime.datetime.now()
            expire_date = rec.expire_date
            if now > expire_date:
                rec.state = 'pending'
            elif rec.state == 'returned':
                break
            elif now < expire_date:
                rec.state = 'rented'

    def return_book(self):
        for rec in self:
            rec.state = 'returned'