from odoo import api, fields, models

class schoolTeacher(models.Model):
    _name = "school.teacher"
    _description = "Profesor"

    name = fields.Char(string='Name', required=True)
    profile = fields.Text(string='Profile', required=True)
    subject_ids = fields.One2many('school.subject', 'teacher_id', string="Subjects")
