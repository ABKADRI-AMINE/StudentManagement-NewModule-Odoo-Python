# -*- coding: utf-8 -*-

from odoo import models, fields, api

class UniversityDepatment(models.Model):
    _name = 'university.depatment'

    name = fields.Char("Nom de filiere")
    code = fields.Char("Chef de filiere")
    student_associated = fields.Many2one('student.student', string="Associated Student", help="Select the associated student.")
    associated_student_full_name = fields.Char(string="Etudiant associee", compute='_compute_associated_student_file_numbers', store=True)

    @api.depends('student_associated')
    def _compute_associated_student_file_numbers(self):
        for record in self:
            if record.student_associated:
                firstName = record.student_associated.mapped('firstName')
                lastName = record.student_associated.mapped('lastName')
                record.associated_student_full_name = ', '.join([str(x) for x in firstName]) + ' ' + ', '.join([str(x) for x in lastName])
            else:
                record.associated_student_full_name = ''