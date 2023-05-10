from odoo import fields, models


class Publisher(models.Model):
    _name='publisher'

    name = fields.Char("Editora", required=True)
    book_ids = fields.One2many(comodel_name="book", inverse_name="publisher_id", string="Livros")
