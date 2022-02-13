from django.urls import path
from invoiceweb.views import test_response


urlpatterns = [
    path('test/', test_response)
]
