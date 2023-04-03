from odoo import fields, models


class Book(models.Model):
    _name = 'book'
    _rec_name = 'title'

    title = fields.Char("Título")
    author_id = fields.Many2one('author', string="Autor")
    publisher_id = fields.Many2one('publisher', string="Editora")
    genre_ids = fields.Many2many('genre', string="Gênero")
    book_cover = fields.Binary(string="Capa do Livro")
    year = fields.Integer("Ano de Lançamento")
    synopsis = fields.Text("Sinopse")
    rent_id = fields.One2many(comodel_name="rent", inverse_name="book_id", readonly=True, string="Aluguéis")
    quantity = fields.Integer(readonly=True, string="Quantidade")
