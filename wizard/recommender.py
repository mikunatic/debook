from odoo import fields, models, _
from random import choice
from odoo.exceptions import Warning


class Recommender(models.TransientModel):
    _name = 'recommender'

    filter = fields.Selection([('genre','Gênero'),
                               ('author','Autor')],
                              string="Escolher como sortear", required=True)
    genre_id = fields.Many2one('genre', string="Gênero")
    author_id = fields.Many2one('author', string="Autor")
    book_id = fields.Many2one('book', string="Livro Sorteado", readonly=True)
    book_synopsis = fields.Text(related='book_id.synopsis', string="Sinopse")
    book_pages = fields.Integer(related='book_id.pages', string="Páginas")
    book_cover = fields.Binary(related='book_id.book_cover', string="Capa do Livro")
    hide_filter = fields.Boolean(default=False)


    def show_book(self):
        domain = []
        if self.filter == 'genre':
            domain.append(('genre_ids','=',self.genre_id.id))
        else:
            domain.append(('author_id','=',self.author_id.id))
        domain.append(('available_quantity', '>', 0))
        book_ids = self.env['book'].search(domain).ids
        if book_ids:
            choosed_book = choice(book_ids)
            ctx = dict()
            ctx.update({
                'default_book_id': choosed_book,
                'default_hide_filter': True,
                'default_filter': 'genre',
                'default_genre_id': 1,

            })
            return {
                'type': 'ir.actions.act_window',
                'name': 'Recomendador de Livro',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'recommender',
                'views': [[self.env.ref("debook.recommender_form_view").id, 'form']],
                'context': ctx,
                'target': 'new'
            }
        else:
            raise Warning(_("Não há livros disponíveis com esse filtro"))

    def rent(self):
        ctx = dict()
        ctx.update({
            'default_book_id': self.book_id.id
        })
        return {
            'type': 'ir.actions.act_window',
            'name': 'Aluguel de Livros',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'rent',
            'views': [[self.env.ref("debook.rent_form_view").id, 'form']],
            'context': ctx,
            'target': 'current'
        }

    def sort_again(self):
        ctx = dict()
        ctx.update({
            'default_hide_filter': False,
        })
        return {
            'type': 'ir.actions.act_window',
            'name': 'Recomendador de Livro',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'recommender',
            'views': [[self.env.ref("debook.recommender_form_view").id, 'form']],
            'context': ctx,
            'target': 'new'
        }