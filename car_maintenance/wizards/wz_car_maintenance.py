# -*- coding: utf-8 -*-

import xlwt
import base64
from io import BytesIO
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError, Warning
from datetime import date

try:
    from odoo.tools.misc import xlsxwriter
except ImportError:
    import xlsxwriter


class WzCarMaintenanceReport(models.TransientModel):
    _name = 'wz.car.maintenance.report'
    _description = 'Report Car Maintenance Most Services'

    date_start = fields.Date('Date Start')
    date_end = fields.Date('Date End')

    name_filename = fields.Char('Name', size=256)
    file_name = fields.Binary('Filename', readonly=True)


    def print_report(self):
        if self.date_start > self.date_end:
            raise ValidationError(_('Start Date must be less than End Date'))

        file_name = 'ReportMasServicios.xls'
        workbook = xlwt.Workbook(encoding="UTF-8")
        formatTitulo = xlwt.easyxf('font:height 300,bold True;')
        formathead2 = xlwt.easyxf(
            'font:height 250,bold True;pattern: pattern solid, fore_colour gray25;align: horiz center; borders: top_color black, bottom_color black, right_color black, left_color black,\
                                left thin, right thin, top thin, bottom thin;')
        format1 = xlwt.easyxf('font:bold True;')
        format2 = xlwt.easyxf('font:bold True;align: horiz left')
        format3 = xlwt.easyxf('align: horiz left; borders: top_color black, bottom_color black, right_color black, left_color black,\
                                left thin, right thin, top thin, bottom thin;')
        sheet = workbook.add_sheet("Datos")
        sheet.col(0).width = int(40 * 260)
        sheet.col(1).width = int(10 * 260)
        sheet.col(2).width = int(10 * 260)
        sheet.row(0).height_mismatch = True
        sheet.row(0).height = 150 * 4
        sheet.row(1).height_mismatch = True
        sheet.row(1).height = 150 * 2
        sheet.row(2).height_mismatch = True
        sheet.row(2).height = 150 * 3
        sheet.write_merge(0, 0, 0, 3, 'Servicios mas solicitados', formatTitulo)
        sheet.write_merge(1, 1, 0, 3, 'Fecha Desde :' + str(self.date_start)+" Hasta :"+ str(self.date_end), formathead2)
        sheet.write(3, 0, 'Servicio', format1)
        sheet.write(3, 1, 'Cantidad', format1)
        sheet.write(3, 2, 'Monto Total', format1)
        rowList = 3
        #Get data
        listServices = []
        listServicesFilter = []
        final_list_data_department = []
        Total = []

        resSearch = self.env['car.maintenance.services'].search(['&',('car_maintenance_id.date_service','>=',str(self.date_start)),('car_maintenance_id.date_service','<=',str(self.date_end))])
        for rec_d in resSearch:
            listServices.append(rec_d.product_id.id)

        listServicesFilter = list(dict.fromkeys(listServices))

        for serv in listServicesFilter :
            res1 = self.env['car.maintenance.services'].search([('product_id','=',serv)])
            if (res1):
                rowList = rowList+1           
                qty = len(res1)
                Total = [x.car_maintenance_id.amount_service for x in res1 if res1.product_id.id == serv]
                sheet.write(rowList, 0, res1.product_id.name or '',format1)           
                sheet.write(rowList, 1, qty,format1)           
                sheet.write(rowList, 2, Total[0],format1)  
            
            Total = []

        fp = BytesIO()
        workbook.save(fp)
        self.write({'file_name': base64.encodestring(fp.getvalue()), 'name_filename': file_name})
        fp.close()
        
        return {
           'type': 'ir.actions.act_window',
           'res_model': 'wz.car.maintenance.report',
           'view_mode': 'form',
           'view_type': 'form',
           'res_id': self.id,
           'target': 'new',
       }

class WzCarMaintenanceReportList(models.TransientModel):
    _name = 'wz.car.maintenance.report.list'
    _description = 'More Services'

    date_start = fields.Date('Date Start')
    date_end = fields.Date('Date End')

    name_filename = fields.Char('Name', size=256)
    file_name = fields.Binary('Filename', readonly=True)



    def print_report(self):
        if self.date_start > self.date_end:
            raise ValidationError(_('Start Date must be less than End Date'))

        file_name = 'ReportServicios.xls'
        workbook = xlwt.Workbook(encoding="UTF-8")
        formatTitulo = xlwt.easyxf('font:height 300,bold True;')
        formathead2 = xlwt.easyxf(
            'font:height 250,bold True;pattern: pattern solid, fore_colour gray25;align: horiz center; borders: top_color black, bottom_color black, right_color black, left_color black,\
                                left thin, right thin, top thin, bottom thin;')
        format1 = xlwt.easyxf('font:bold True;')
        format2 = xlwt.easyxf('font:bold True;align: horiz left')
        format3 = xlwt.easyxf('align: horiz left; borders: top_color black, bottom_color black, right_color black, left_color black,\
                                left thin, right thin, top thin, bottom thin;')
        sheet = workbook.add_sheet("Datos")
        sheet.col(0).width = int(20 * 260)
        sheet.col(1).width = int(30 * 260)
        sheet.col(2).width = int(10 * 260)
        sheet.col(3).width = int(10 * 260)
        sheet.row(0).height_mismatch = True
        sheet.row(0).height = 150 * 4
        sheet.row(1).height_mismatch = True
        sheet.row(1).height = 150 * 2
        sheet.row(2).height_mismatch = True
        sheet.row(2).height = 150 * 3
        sheet.write_merge(0, 0, 0, 3, 'Servicios', formatTitulo)
        sheet.write_merge(1, 1, 0, 3, 'Fecha Desde :' + str(self.date_start)+" Hasta :"+ str(self.date_end), formathead2)
        sheet.write(3, 0, 'Matrícula', format1)
        sheet.write(3, 1, 'Cliente', format1)
        sheet.write(3, 2, 'Monto Servicio	', format1)
        sheet.write(3, 3, 'Fecha Servicio', format1)
        rowList = 3
        #Get data
        listServices = []
        listServicesFilter = []

        resSearch = self.env['car.maintenance'].search(['&',('date_service','>=',str(self.date_start)),('date_service','<=',str(self.date_end))])
        for rec_d in resSearch:
            listServices.append(rec_d.id)

        listServicesFilter = list(dict.fromkeys(listServices))

        for serv in listServicesFilter :
            res1 = self.env['car.maintenance'].search([('id','=',serv)])
            if (res1):
                rowList = rowList+1           
                sheet.write(rowList, 0, res1.car_plate or '',format1)           
                sheet.write(rowList, 1, res1.partner_id.name,format1)           
                sheet.write(rowList, 2, res1.amount_service,format1)  
                sheet.write(rowList, 3, res1.date_service,format1)  

        fp = BytesIO()
        workbook.save(fp)
        self.write({'file_name': base64.encodestring(fp.getvalue()), 'name_filename': file_name})
        fp.close()
        
        return {
           'type': 'ir.actions.act_window',
           'res_model': 'wz.car.maintenance.report.list',
           'view_mode': 'form',
           'view_type': 'form',
           'res_id': self.id,
           'target': 'new',
       }

