# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014 Camptocamp
#    Author Joel Grand-Guillaume
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import fields, orm


class ProjectTask(orm.Model):
    _inherit = 'project.task'
    _columns = {
        'project_department_id': fields.related(
            'project_id',
            'department_id',
            type='many2one',
            relation='hr.department',
            string='Project Department',
            store=True,
            readonly=True),
    }
