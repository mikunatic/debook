from odoo import fields, models


class Book(models.Model):
    _name = 'book'
    _rec_name = 'title'

    title = fields.Char()
    author_id = fields.Many2one('author')
    publisher_id = fields.Many2one('publisher')
    genre_ids = fields.Many2many('genre')
    book_cover = fields.Binary("Book Cover")
    rent_ids = fields.One2many(comodel_name="rent", inverse_name="book_id", readonly=True)

    def name_get(self):
        result = []
        for rec in self:
            recname =  rec.title + " " + "(" +str(rec.id)+")"
            result.append((rec.id, recname))
        return result