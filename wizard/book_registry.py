from odoo import fields, models


class BookRegistry(models.TransientModel):
    _name = 'book.registry'

    book_title = fields.Char(string="Book Title")
    book_author = fields.Many2one('author', string="Book Author")
    book_publisher = fields.Many2one('publisher', string="Book Publisher")
    book_genre = fields.Many2many(comodel_name='genre', relation="registry_genre_rel", string="Book Genre")
    book_quantity = fields.Integer()

    def register_book(self):
        register_counter = 0
        register_stopper = self.book_quantity
        while register_counter < register_stopper:
            book_vals_list = {
                'title':self.book_title,
                'author_id':self.book_author.id,
                'publisher_id':self.book_publisher.id,
                'genre_ids':self.book_genre.ids,
            }
            self.env['book'].create(book_vals_list)
            register_counter += 1