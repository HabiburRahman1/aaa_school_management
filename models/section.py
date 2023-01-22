from odoo import fields, models


class School(models.Model):
    _name = 'school.section'
    _description = 'school'

    name = fields.Char('Section')
    code = fields.Char('Section Code')
    student_ids = fields.One2many('school.student','section_id','Student List')



class School(models.Model):
    _name = 'school.student'
    _description = 'school'

    name = fields.Char('Name', required= True)
    email = fields.Char('Email')
    phone = fields.Char('Contact')
    birth_date = fields.Date('Birth of Date: ')
    gender = fields.Selection([('M','Male'),('F','Female')], 'Gender')
    image = fields.Image('Image')
    section_id = fields.Many2one('school.section','Section')