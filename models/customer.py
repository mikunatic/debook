from odoo import fields, models
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Customer(models.Model):
    _name = 'customer'

    name = fields.Char("Name", required=True)
    cpf = fields.Char("CPF", required=True)
    email = fields.Char("E-mail", required=True)
    city = fields.Char("City", required=True)
    cep = fields.Char("CEP", required=True)
    state = fields.Many2one('res.country.state', required=True)
    country = fields.Many2one('res.country', default=31, readonly=True)
    rent_ids = fields.One2many(comodel_name="rent", inverse_name="customer_id", readonly=True)

    def create(self):
        for rec in self:
            remetente = 'seu_email@gmail.com'  # Substitua com o seu endereço de email
            senha = 'sua_senha'  # Substitua com a sua senha de email

            # Cria o objeto MIME para o email
            msg = MIMEMultipart()
            msg['From'] = remetente
            msg['To'] = rec.email
            msg['Subject'] = "Bem-vindo"
            msg.attach(MIMEText("Você se cadastrou no deBook!", 'plain'))

            # Conecta ao servidor SMTP do Gmail
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(remetente, senha)

            # Envia o email
            texto_do_email = msg.as_string()
            server.sendmail(remetente, rec.email, texto_do_email)
            server.quit()