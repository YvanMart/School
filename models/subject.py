from odoo import api, fields, models

class schoolSubject(models.Model):
    _name = "school.subject"
    _description = "Cursos"

    name = fields.Char(string='Name', required=True)
    credits = fields.Integer(string='Credits', required=True)
    max_students = fields.Integer(string='Maximum Students', required=True)
    active = fields.Boolean(string='Active', default=True)
    student_ids = fields.Many2many('school.student', string="Students")
    teacher_id = fields.Many2one('school.teacher', string="Teacher")
