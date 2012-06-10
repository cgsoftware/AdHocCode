# -*- encoding: utf-8 -*-
from osv import fields, osv

import wizard
import decimal_precision as dp
import pooler
import time
from tools.translate import _
from osv import osv, fields
from tools.translate import _
import tools
import base64
from tempfile import TemporaryFile
from osv import osv, fields

class product_product(osv.osv):
        _inherit = 'product.product'
        _columns = {
                    'adhoc_code': fields.char('Cod.Art.Ad-Hoc', size=15),
                    }


product_product()
