from odoo import fields, models


class Publisher(models.Model):
    _name='publisher'

    name = fields.Char("Editora")
    book_ids = fields.Many2many('book', compute="populate_books", string="Livros")

    def populate_books(self):
        for rec in self:
            book_ids = self.env['book'].search([('publisher_id','=',rec.id)])
            rec.book_ids = book_ids.ids