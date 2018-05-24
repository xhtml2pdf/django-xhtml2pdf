from django.http import HttpResponse

from django.views.generic.detail import DetailView
from django_xhtml2pdf.views import PdfMixin
from django_xhtml2pdf.utils import generate_pdf, render_to_pdf_response, pdf_decorator
from django.contrib.auth.models import User
from django.shortcuts import render

def test_view(request):
    resp = HttpResponse(content_type='application/pdf')
    result = generate_pdf('test_pdf.html', file_object=resp)
    return result



def test_view_fileobject(request):
    # this test file_object as None in py2 and py3
    resp = HttpResponse(content_type='application/pdf')
    result = generate_pdf('test_pdf.html')
    result.seek(0)
    resp.write(result.read())
    return resp


def test_render_response(request):
    return render_to_pdf_response('test_pdf.html')

@pdf_decorator
def render_template_decorated(request):
    return render(request, 'test_pdf.html')

class UserPdfView(PdfMixin, DetailView):
    model = User
    template_name = "user_pdf.html"
