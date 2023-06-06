from odoo import fields, models, _
from odoo.exceptions import UserError

class BookRegistry(models.TransientModel):
    _name = 'book.registry'

    book_title = fields.Char(string="Título do Livro", required=True)
    book_author = fields.Many2one('author', string="Autor do Livro", required=True)
    book_publisher = fields.Many2one('publisher', string="Editora do Livro", required=True)
    book_genre = fields.Many2many(comodel_name='genre', relation="registry_genre_rel", string="Gêneros do Livro", required=True)
    book_quantity = fields.Integer(default=1, string="Quantidade", required=True)
    book_cover = fields.Binary("Capa do Livro", required=True)
    book_year = fields.Integer("Ano de Lançamento", required=True)
    book_pages = fields.Integer("Páginas", required=True)
    book_synopsis = fields.Text("Sinopse", required=True)

    def register_book(self):
        if self.book_pages < 0:
            raise UserError(_("Número de páginas inválido"))
        if self.book_year < 0 or self.book_year > (fields.Date.today().year):
            raise UserError(_("Ano inválido"))
        if self.book_quantity < 0:
            raise UserError(_("Quantidade inválida"))
        book_vals_list = {
            'title':self.book_title,
            'author_id':self.book_author.id,
            'publisher_id':self.book_publisher.id,
            'genre_ids':self.book_genre.ids,
            'book_cover':self.book_cover,
            'year':self.book_year,
            'pages':self.book_pages,
            'synopsis':self.book_synopsis,
            'quantity':self.book_quantity,
            'available_quantity':self.book_quantity
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