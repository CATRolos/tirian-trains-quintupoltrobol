from django.urls import path
from .views import pageview, MaintainDetailView

app_name = "train_maintain"

urlpatterns = [
  path('', pageview, name='pageview'),
  path('<int:pk>/details/', MaintainDetailView.as_view(), name="maintenance-detail")
]