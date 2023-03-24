from odoo import fields, models


class Book(models.Model):
    _name = 'book'
    _rec_name = 'title'

    title = fields.Char()
    author_id = fields.Many2one('author')
    publisher_id = fields.Many2one('publisher')
    genre_ids = fields.Many2many('genre')
    book_cover = fields.Image("Book Cover")

    def name_get(self):
        for rec in self:
            result = []
            result.append((rec.id, rec.title))
        return result