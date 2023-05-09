from odoo import fields, models, api
from datetime import timedelta


class Rent(models.Model):
    _name = 'rent'

    customer_id = fields.Many2one('customer', string="Cliente", required=True)
    rent_ids = fields.One2many(related='customer_id.rent_ids', string="Cliente")
    book_id = fields.Many2one('book', string="Livro", domain="[('available_quantity','>',0)]", required=True)

    available_book = fields.Boolean(related="book_id.available_book", invisible=True)
    expire_date = fields.Selection([('15', '15 dias'),
                                    ('30', '1 mês'),
                                    ('60', '2 meses')], string="Seleção de Vencimento", required=True)
    date_time_fixed = fields.Date(string="Data de Vencimento", readonly=1)
    state = fields.Selection([('rented', 'Alugado'),
                              ('pending', 'Devolução Pendente'),
                              ('returned', 'Devolvido')],
                             compute="expire", store=True, string="Status")
    is_expired = fields.Boolean(compute="_compute_is_expired")

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

    def _compute_is_expired(self):
        for rec in self:
            if rec.date_time_fixed and rec.state:
                now = fields.Date.today()
                if now >= rec.date_time_fixed and rec.state != 'returned':
                    rec.is_expired = True
                elif now < rec.date_time_fixed and rec.state != 'returned':
                    rec.is_expired = False
                if rec.is_expired == True:
                    rec.state = 'pending'
                elif rec.is_expired == False and rec.state != 'returned':
                    rec.state = 'rented'

    def return_book(self):
        for rec in self:
            rec.state = 'returned'

    def name_get(self):
        result = []
        for record in self:
            rec_name = str(record.customer_id.name) + " - " + str(record.book_id.title)
            result.append((record.id, rec_name))
        return result

    def undo(self):
        for rec in self:
            rec.state = 'rented'
