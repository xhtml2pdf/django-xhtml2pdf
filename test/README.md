How to run test
=================

Install dependencies:

```
  pip install django
  pip install xhtml2pdf
```

Make migrations and one user (need for test):

```
   cd d1_11
   python manage.py migrate
   python manage.py createsuperuser
```

Run server:

``
python manage.py runserver
``

Go to this urls 

- http://localhost:8000/test_view
- http://localhost:8000/test_render_response
- http://localhost:8000/test_user/1
- http://localhost:8100/render_template_decorated
