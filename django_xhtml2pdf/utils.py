#-*- coding: utf-8 -*-
from django.conf import settings
from django.http import HttpResponse
from django.template.context import Context
from django.template.loader import get_template
from xhtml2pdf import pisa # TODO: Change this when the lib changes.
import StringIO
import os

#===============================================================================
# HELPERS
#===============================================================================
class UnsupportedMediaPathException(Exception):
    pass

def fetch_resources(uri, rel):
    """
    Callback to allow xhtml2pdf/reportlab to retrieve Images,Stylesheets, etc.
    `uri` is the href attribute from the html link element.
    `rel` gives a relative path, but it's not used here.

    """
    if uri.startswith(settings.MEDIA_URL):
        path = os.path.join(settings.MEDIA_ROOT,
                            uri.replace(settings.MEDIA_URL, ""))
    elif uri.startswith(settings.STATIC_URL):
        path = os.path.join(settings.STATIC_ROOT,
                            uri.replace(settings.STATIC_URL, ""))
        if not os.path.exists(path):
            for d in settings.STATICFILES_DIRS:
                path = os.path.join(d, uri.replace(settings.STATIC_URL, ""))
                if os.path.exists(path):
                    break
    elif uri.startswith("http://") or uri.startswith("https://"):
        path = uri
    else:
        raise UnsupportedMediaPathException(
                                'media urls must start with %s or %s' % (
                                settings.MEDIA_ROOT, settings.STATIC_ROOT))
    return path

def generate_pdf_template_object(template_object, file_object, context):
    """
    Inner function to pass template objects directly instead of passing a filename
    """
    html = template_object.render(Context(context))
    pisa.CreatePDF(html.encode("UTF-8"), file_object , encoding='UTF-8',
                   link_callback=fetch_resources)
    return file_object

#===============================================================================
# Main
#===============================================================================

def generate_pdf(template_name, file_object=None, context=None): # pragma: no cover
    """
    Uses the xhtml2pdf library to render a PDF to the passed file_object, from the
    given template name.

    This returns the passed-in file object, filled with the actual PDF data.
    In case the passed in file object is none, it will return a StringIO instance.

    """
    if not file_object:
        file_object = StringIO.StringIO()
    if not context:
        context = {}
    tmpl = get_template(template_name)
    generate_pdf_template_object(tmpl, file_object, context)
    return file_object

def render_to_pdf_response(template_name, context=None, pdfname=None):
    file_object = HttpResponse(content_type='application/pdf')
    if not pdfname:
        pdfname = '%s.pdf' % os.path.splitext(os.path.basename(template_name))[0]
    file_object['Content-Disposition'] = 'attachment; filename=%s' % pdfname
    return generate_pdf(template_name, file_object, context)
