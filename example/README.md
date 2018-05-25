How to run test
=================

Create a Virtual Environment and activate it

```
virtualenv xhtml2pdf-test
source xhtml2pdf-test/bin/activate
```

Install dependencies:

```
  pip install -r example/requirements.txt
```

Install django-xhtml2pdf in 'develop' mode

```
  python setup.py develop
```

Make migrations and one user (need for test):

```
   cd example/demo
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
- http://localhost:8000/render_template_decorated
- http://localhost:8000/test_view_fileobject
