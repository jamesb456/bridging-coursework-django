from django.urls import path
from . import views



urlpatterns = [
    path('',views.cv_view,name="cv_view"),
    path('edit/',views.edit_cv_view,name="edit_cv_view")
]