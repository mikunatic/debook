from odoo import fields, models


class UpdateQuantity(models.Model):
    _name = 'update.quantity'

    quantity = fields.Integer(string="Quantidade", required=True)

    def save_updated_quantity(self):
        active_id = self.env.context.get("active_id")
        book_id = self.env['book'].browse(active_id)
        book_id.write({'quantity':book_id.quantity + self.quantity,
                       'available_quantity':book_id.available_quantity + self.quantity})