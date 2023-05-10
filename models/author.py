from odoo import fields, models


class Author(models.Model):
    _name = 'author'

    name = fields.Char("Autor", required=True)
    book_ids = fields.One2many(comodel_name="book", inverse_name="author_id", string="Livros")