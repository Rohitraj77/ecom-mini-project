from django.urls import path
from django.http import HttpResponse

def home(_request):
    return HttpResponse("<h2>Ecom Admin Panel (placeholder)</h2><p>API is running ✅</p>")

urlpatterns = [
    path("", home, name="admin-home"),
]
