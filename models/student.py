from odoo import api, fields, models
from datetime import datetime
from odoo.exceptions import ValidationError

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

    def write(self, vals):
        if 'subject_ids' in vals:
            for subject in self.env['school.subject'].browse(vals['subject_ids'][0][2]):
                if len(subject.student_ids) >= subject.max_students:
                    raise ValidationError("Maximum number of students reached for this subject")
        return super(schoolStudent, self).write(vals)
