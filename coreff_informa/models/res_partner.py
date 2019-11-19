# -*- coding: utf-8 -*-
# ©2018-2019 Article714
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models
from odoo.addons.coreff_informa.mixins.informa_data_mixin import (
    InformaDataMixin,
)


class Partner(InformaDataMixin, models.Model):
    """
    Add informa fields from InformaDataMixin
    """

    _inherit = "res.partner"