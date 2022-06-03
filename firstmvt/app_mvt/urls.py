from django.urls import URLPattern, path 
from . import views
urlpatterns = [
   path("abuela", views.abuela),
   path("tios", views.tios),
   path("primos", views.primos)
]


