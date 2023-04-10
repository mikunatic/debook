from odoo import fields, models


class UpdateQuantity(models.Model):
    _name = 'update.quantity'

    quantity = fields.Integer(string="Quantidade", required=True)

    def save_updated_quantity(self):
        active_id = self.env.context.get("active_id")
        book_id = self.env['book'].browse(active_id)
        rents = book_id.rent_ids.filtered(lambda rent: rent.state != 'returned')
        available = self.quantity - len(rents)
        book_id.write({'quantity':self.quantity,
                       'available_quantity':available})