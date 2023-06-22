from odoo import fields, models, api
import requests


class Customer(models.Model):
    _name = 'customer'

    name = fields.Char("Nome", required=True)
    cpf = fields.Char("CPF", required=True)
    email = fields.Char("E-mail", required=True)
    city = fields.Many2one('city', string="Cidade", required=True)
    cep = fields.Char("CEP", required=True)
    rent_ids = fields.One2many(comodel_name="rent", inverse_name="customer_id", readonly=True)

    # @api.onchange('cep')
    # def onchange_cep(self):
    #     if self.cep:
    #         url = f'https://viacep.com.br/ws/{self.cep}/json/'
    #         response = requests.get(url)
    #         if response.status_code == 200:
    #             data = response.json()
    #             self.city = data.get('localidade', '')
    #             self.cep = data.get('cep', '')

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