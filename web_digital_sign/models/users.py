# See LICENSE file for full copyright and licensing details.

from odoo import models, fields

class Users(models.Model):
    _name = 'res.users'
    _inherit = 'res.users'

    digital_signature = fields.Binary(string='Firma')
