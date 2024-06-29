from django.urls import path
from . import views
urlpatterns=[
    path("",views.index,name='index'),
    path("city_aqi",views.city_aqi,name='city_aqi'),
    path("prediction/<city>",views.prediction,name='prediction'),
    path("state_page/<status>",views.state_page,name="state_page")


]