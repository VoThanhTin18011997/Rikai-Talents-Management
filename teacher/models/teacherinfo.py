from . import models, fields, api

class Level(models.Model):
    _name = "teacher.info.level"
    name = fields.Char("Name", required=True)

class Teacher(models.Model):
    _name = "techer.info"
    _decription = "Teacher Information"

    name = fields.Char(string="Teacher Name", requiered = true, track_visibility='onchange')
    email = fields.Char("Email", required = true, track_visibility='onchange')
    phone = fields.Char("Phone", required = true, track_visibility='onchange')
    level_id = fields.Many2one("teacher.info.level", string="Level", required = False, track_visibility='onchange')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender', default='male')
    teacher_image = fields.Binary("Teacher Image", attachment=True, help="Teacher Image")