from odoo import fields, models, api


class HospitalPatient(models.Model):  # this is the way of defining model
    _name = "hospital.patient"        # way of defining model name from this name we will use this model

# Now we are going to define some fields

    name = fields.Char(string="Name")
    ref = fields.Char(string="Reference")  # a unique id for patient
    age = fields.Integer(string="Age")
    gender = fields.Selection([('male','Male'),('female','Female')], string="Gender")
    active = fields.Boolean(string="Active", default=False)
