from odoo import api, fields, models
from odoo.exceptions import ValidationError
from odoo.tools.translate import _

class schoolSubject(models.Model):
    _name = "school.subject"
    _description = "Cursos"

    name = fields.Char(string='Name', required=True)
    credits = fields.Integer(string='Credits', required=True)
    max_students = fields.Integer(string='Maximum Students', required=True)
    active = fields.Boolean(string='Active', default=True)
    student_ids = fields.Many2many('school.student', string="Students")
    teacher_id = fields.Many2one('school.teacher', string="Teacher")

    def write(self, vals):
        if 'student_ids' in vals:
            for subject in self:
                if len(subject.student_ids) - len(
                        [x for x in subject.student_ids.ids if x not in vals['student_ids'][0][2]]) + len(
                        vals['student_ids'][0][2]) > subject.max_students + 1:
                    raise ValidationError(_('The subject %s is full. Cannot add more students.') % subject.name)
        return super(schoolSubject, self).write(vals)
