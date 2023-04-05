from odoo import fields, models, api
from datetime import timedelta


class Rent(models.Model):
    _name = 'rent'

    customer_id = fields.Many2one('customer', string="Cliente")
    book_id = fields.Many2one('book', string="Livro", domain="[('rent_id','=',False)]")
    expire_date = fields.Selection([('15', '15 dias'),
                                    ('30', '1 mês'),
                                    ('60', '2 meses')], string="Seleção de Vencimento")
    date_time_fixed = fields.Date(string="Data de Vencimento", readonly=1)
    state = fields.Selection([('rented', 'Alugado'),
                              ('pending', 'Devolução Pendente'),
                              ('returned', 'Devolvido')],
                             compute="expire", store=True)

    # fazer função que calcula a data de vencimento de acordo com o selection
    @api.onchange('expire_date')
    def calculate_expire(self):
        if self.expire_date:
            self.date_time_fixed = fields.Date.today()
            self.date_time_fixed += timedelta(int(self.expire_date))

    @api.model
    def create(self, vals_list):
        vals_list['state'] = 'rented'
        return super(Rent, self).create(vals_list)

    @api.depends('date_time_fixed')
    def expire(self):
        for rec in self:
            if rec.date_time_fixed and rec.state:
                now = fields.Date.today()
                if now >= rec.date_time_fixed and rec.state != 'returned':
                    rec.state = 'pending'

    def return_book(self):
        for rec in self:
            rec.state = 'returned'