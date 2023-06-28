from odoo import fields, models, api


class HospitalPatient(models.Model):  # this is the way of defining model
    _name = "hospital.appointment"  # way of defining model name from this name we will use this model
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'booking_date'

    # Now we are going to define some fields

    patient_id = fields.Many2one('hospital.patient', string="Name")
    appointment_time = fields.Datetime(string="Appointment Time", default=fields.Datetime.now())
    gender = fields.Selection(string="gender", related="patient_id.gender", readonly=False)
    booking_date = fields.Date(string="Booking Date")
    date_of_birth = fields.Date(string="Date of Birth")
    age = fields.Integer(string='Age', compute='_calculate_age')
    html = fields.Html(string="HTML")
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], string="Priority")

    state = fields.Selection([
        ('drafts', 'Draft'),
        ('in_consultation', 'In Consultation'),
        ('done', 'Done'),
        ('cancel', 'Cancel')], string="Status")

    @api.constrains('date_of_birth')
    def _calculate_age(self):
        current_date = fields.Date.today()
        for record in self:
            dob = record.date_of_birth
            if dob and current_date:
                age = current_date.year - dob.year
            else:
                age = 0
            # if (current_date.month, current_date.day) < (dob.month, dob.day):
            #     age -= 1
            # Assign the calculated age to a field on the model
            record.age = age

    @api.constrains('date_start2', 'sign_date')
    def contract_date_comparison(self):
        for rec in self:
            if rec.date_start2 < rec.sign_date:
                raise ValidationError(_("Contract Start Date Should Not Be Less Than Contract Sign Date"))
