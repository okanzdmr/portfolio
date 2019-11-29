from django.urls import path
from . import views



urlpatterns = [
    path("",views.info,  name="main_index.html"),
    # path("<int:pk>/", views.project_detail, name="project_detail"),
]
