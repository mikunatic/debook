from odoo import fields, models


class Genre(models.Model):
    _name = 'genre'

    name = fields.Char("Genre")
    book_ids = fields.Many2many('book', compute="populate_books")

    def populate_books(self):
        for rec in self:
            book_ids = self.env['book'].search([('genre_ids','in',rec.id)])
            rec.book_ids = book_ids.ids