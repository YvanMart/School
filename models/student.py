from odoo import api, fields, models
from datetime import datetime

class schoolStudent(models.Model):
    _name = "school.student"
    _description = "Estudiante"

    name = fields.Char(string='Name', required=True)
    birth_date = fields.Date(string='Birth Date', required=True)
    age = fields.Integer(string='Age', compute='_compute_age', store=True)
    final_exam_grade = fields.Float(string='Final Exam Grade')
    subject_ids = fields.Many2many('school.subject', string="Subjects")

    @api.depends('birth_date')
    def _compute_age(self):
        for student in self:
            if student.birth_date:
                today = datetime.today()
                birth_date = datetime.strptime(str(student.birth_date), '%Y-%m-%d')
                student.age = today.year - birth_date.year - (
                            (today.month, today.day) < (birth_date.month, birth_date.day))