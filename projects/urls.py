from django.urls import path
from . import views



urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("<slug:slug>/", views.project_detail, name="project_detail"),
    path(""+"categories/<category>/", views.project_category, name="project_category"),
]
