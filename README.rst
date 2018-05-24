Django xhtml2pdf
################

Attention
=============================

This project is wrapper code between the django project and the xhtml2pdf
project, both have a few maintaining so maybe are not ideal for your project.

Please get in touch if you would like to take over maintainership.

What it does is simply allow people to create xhtml2pdf templates using all the
cool django things like STATIC_URL etc.. (like one would for a webpage
template), and the utils function makes all the images and ressources appear in
the pdf.

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
