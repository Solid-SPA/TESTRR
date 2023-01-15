# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import Controller, route, request
from odoo.addons.website.controllers.main import Website


class WebsiteCarMaintenance(Website):
    @http.route(auth='public')
    def index(self, data={}, **kw):
        super(WebsiteCarMaintenance, self).index(**kw)
        return http.request.render('website_car_maintenance.THomeServices', False)

  