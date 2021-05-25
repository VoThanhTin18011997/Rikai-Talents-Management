from odoo import  http, fields
from odoo.http import request

class MyTeacherAPI(http.Controller):
    @http.route(['/foo'],type='http', website=True, stemap = False ,auth='public')
    def foo_handler(self):
        return "Hello Tin, Welcome to foo API !"