from odoo import fields, models, api


class HospitalPatient(models.Model):  # this is the way of defining model
    _name = "hospital.patient"        # way of defining model name from this name we will use this model
    _inherit = ['mail.thread', 'mail.activity.mixin']

# Now we are going to define some fields

    name = fields.Char(string="Name", tracking=True)
    ref = fields.Char(string="Reference")  # a unique id for patient
    age = fields.Integer(string="Age", tracking=True)
    gender = fields.Selection([('male','Male'),('female','Female')], string="Gender", default="male")
    active = fields.Boolean(string="Active", default=False)
