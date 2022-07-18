from django.urls import path
from .views import BallotsView

urlpatterns = [path("", BallotsView.as_view())]
