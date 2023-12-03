from django.urls import path
from .views import pageview

app_name = "train_maintain"

urlpatterns = [
  path('', pageview, name='pageview'),
]