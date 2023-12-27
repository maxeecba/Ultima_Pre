from django.urls import path
from .views import index
app_name = "clientess"
urlpatterns = [
    path ('clientes/',index, name = "index")
    ]
