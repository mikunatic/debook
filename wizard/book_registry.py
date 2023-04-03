from odoo import fields, models, _


class BookRegistry(models.TransientModel):
    _name = 'book.registry'

    book_title = fields.Char(string="Título do Livro")
    book_author = fields.Many2one('author', string="Autor do Livro")
    book_publisher = fields.Many2one('publisher', string="Editora do Livro")
    book_genre = fields.Many2many(comodel_name='genre', relation="registry_genre_rel", string="Gêneros do Livro")
    book_quantity = fields.Integer(default=1, string="Quantidade")
    book_cover = fields.Binary("Capa do Livro")
    book_year = fields.Integer("Ano de Lançamento")
    book_synopsis = fields.Text("Sinopse")

    def register_book(self):
        book_vals_list = {
            'title':self.book_title,
            'author_id':self.book_author.id,
            'publisher_id':self.book_publisher.id,
            'genre_ids':self.book_genre.ids,
            'book_cover':self.book_cover,
            'year':self.book_year,
            'synopsis':self.book_synopsis,
            'quantity':self.book_quantity
        }
        self.env['book'].create(book_vals_list)

        book_id = self.env['book'].search([], order="id asc")[-1]
        return {
            "type": "ir.actions.act_window",
            "name": _("Livros"),
            "res_model": "book",
            "domain": [("id", "=", book_id.id)],
            "view_mode": "tree,form",
            "context": self.env.context
        }