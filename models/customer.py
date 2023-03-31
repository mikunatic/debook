from odoo import fields, models, api


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

    # @api.model
    # def create(self, vals_list):
    #
    #     target = vals_list.get('email')
    #     smtp_server = "smtp.gmail.com"
    #     smtp_port = 587
    #     usuario = "sys4seek@gmail.com"
    #     senha = "agerjumi@123"
    #     to = vals_list.get('email')
    #     subject = "Bem-vindo"
    #     message = "Você se cadastrou no deBook"
    #     creds = Credentials.from_authorized_user_file('token.json', ['https://www.googleapis.com/auth/gmail.send'])
    #
    #     # corpo da mensagem
    #     message = f'To: {to}\nSubject: {subject}\n\n{message}'
    #     message_bytes = message.encode('utf-8')
    #     message_b64 = base64.urlsafe_b64encode(message_bytes).decode('utf-8')
    #     body = {'raw': message_b64}
    #
    #     try:
    #         # cria a conexão com a API do Gmail
    #         service = build('gmail', 'v1', credentials=creds)
    #
    #         # envia o e-mail
    #         message = service.users().messages().send(userId='me', body=body).execute()
    #         print(f'Successfully sent message to {to}, Message Id: {message["id"]}')
    #
    #     except Exception as error:
    #         print(f'An error occurred: {error}')