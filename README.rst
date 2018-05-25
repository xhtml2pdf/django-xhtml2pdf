Django xhtml2pdf
################

Attention
=============================

This project is wrapper code between the django project and the xhtml2pdf
project, both have a few maintaining so maybe are not ideal for your project.

What it does is simply allow people to create xhtml2pdf templates using all the
cool django things like STATIC_URL etc.. (like one would for a webpage
template), and the utils function makes all the images and resources appear in
the pdf.

This release (0.0.5) supports Django 2.0, and Python 3.6.

NOTE:

While this project is being maintained on a limited basis for legacy projects,
we recommend strongly that new projects consider using
`WeasyPrint <https://weasyprint.org>`.

Usage
=====

Simply do the following::

    from django_xhtml2pdf.utils import generate_pdf

    def myview(response):
        resp = HttpResponse(content_type='application/pdf')
        result = generate_pdf('my_template.html', file_object=resp)
        return result

Class-based views
=================

You can use the provided PdfMixin with any view that subclasses TemplateView,
example::

    from django.views.generic.detail import DetailView
    from django_xhtml2pdf.views import PdfMixin
    from .models import Product

    class ProductPdfView(PdfMixin, DetailView):
        model = Product
        template_name = "product_pdf.html"

It will output the rendered content of the view in pdf.

Decorator
============

Simply do the following::

    from django_xhtml2pdf.utils import pdf_decorator

    @pdf_decorator
    def myview(request):
        return render(request, 'mytemplate.html')

Change the pdf file name::

    from django_xhtml2pdf.utils import pdf_decorator

    @pdf_decorator(pdfname='new_filename.pdf')
    def myview(request):
        return render(request, 'mytemplate.html')
