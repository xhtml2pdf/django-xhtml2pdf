#-*- coding: utf-8 -*-

from .utils import PdfResponse


class PdfMixin(object):
    content_type = "application/pdf"
    response_class = PdfResponse
