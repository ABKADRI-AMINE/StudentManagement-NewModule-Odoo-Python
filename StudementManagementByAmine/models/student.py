from odoo import api, models, fields

class Student(models.Model):
    _name = 'student.student'
    _description = 'Student Management'

    fileNumber = fields.Char(string="File Number", required=True, default=lambda self: self.env['ir.sequence'].next_by_code('student.student.sequence'))
    lastName = fields.Char(string="Last Name", required=True)
    firstName = fields.Char(string="First Name", required=True)
    dateOfBirth = fields.Date(string="Date Of Birth")
    email = fields.Char(string="Email", required=True)
    phoneNumber = fields.Char(string="Phone Number", required=True)  # Corrected type to Integer
    cin = fields.Char(string="CIN", required=True)
    cne = fields.Char(string="CNE", required=True)
    paid = fields.Selection([('paid', 'Yes'), ('notPaid', 'No')], string="Paid", required=True)