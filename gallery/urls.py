from django.urls.conf import path
from .views import Home,Details,PostView
app_name='gallery'
urlpatterns=[
    path('',Home.as_view(),name='home'),
    path('detail/<int:pk>',Details.as_view(),name='details'),
    path('post/',PostView.as_view(),name='post')
]