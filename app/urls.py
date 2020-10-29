from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('', views.dashboard,name="dashboard"),

    path('pages/buttons', views.buttons,name="buttons"),
    path('pages/elements', views.elements,name="elements"),
    path('pages/table', views.table,name="table"),
    path('pages/chart', views.chart,name="chart"),
    path('pages/icons', views.icons,name="icons"),
    path('pages/typography', views.typography,name="typography"),

]
