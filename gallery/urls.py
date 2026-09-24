from django.urls.conf import path
from .views import Home
app_name='gallery'
url_patterns=[
    path('',Home.as_view(),name='home'),
]