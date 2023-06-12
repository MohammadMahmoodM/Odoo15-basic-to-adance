from odoo import fields, models, api


class HospitalPatient(models.Model):  # this is the way of defining model
    _name = "hospital.appointment"  # way of defining model name from this name we will use this model
    _inherit = ['mail.thread', 'mail.activity.mixin']

    # Now we are going to define some fields

    patient_id = fields.Many2one('hospital.patient', string="Name")
    appointment_time = fields.Datetime(string="Appointment Time", default=fields.Datetime.now())
    gender = fields.Selection(string="gender", related="patient_id.gender", readonly=False)
    booking_date = fields.Date(string="Booking Date")
