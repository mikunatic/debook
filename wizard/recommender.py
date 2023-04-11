from odoo import fields, models
import random

class Recommender(models.TransientModel):
    _name = 'recommender'

    filter = fields.Selection([('genre','Gênero'),
                               ('author','Autor')],
                              string="Escolher como sortear")
    genre_id = fields.Many2one('genre', string="Gênero")
    author_id = fields.Many2one('author', string="Autor")
    book_id = fields.Many2one('book', string="Livro Sorteado", readonly=True)
    book_synopsis = fields.Text(related='book_id.synopsis', string="Sinopse")
    hide_filter = fields.Boolean(default=False)


    def show_book(self):
        domain = []
        if self.filter == 'genre':
            domain.append(('genre_ids','=',self.genre_id.id))
            domain.append(('available_quantity','>',0))
        else:
            domain.append(('author_id','=',self.author_id.id))
            domain.append(('available_quantity', '>', 0))
        book_ids = self.env['book'].search(domain).ids
        choosed_book = random.choice(book_ids)
        ctx = dict()
        ctx.update({
            'default_book_id': choosed_book,
            'default_hide_filter': True
        })
        return {
            'type': 'ir.actions.act_window',
            'name': 'Recomendador de Livro',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'recommender',
            'views': [[self.env.ref("deBook.recommender_form_view").id, 'form']],
            'context': ctx,
            'target': 'new'
        }