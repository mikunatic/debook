from odoo import fields, models, api


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
    quantity = fields.Integer(string="Quantidade")
    available_quantity = fields.Integer("Quantidade Disponível", compute="calculate_available_books", store=True)

    @api.depends('quantity')
    def calculate_available_books(self):
        for rec in self:
            rents = self.env['rent'].search([('state','!=','returned'),('book_id','=',rec.id)]).ids
            rec.available_quantity = (rec.quantity - len(rents))
