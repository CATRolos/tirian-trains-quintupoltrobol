from .models import Train, MaintenanceTask, MaintenanceCrew
from django.views.generic import DetailView
from django.shortcuts import render
from django.urls import reverse

def pageview(request):
    model_object = MaintenanceTask.objects.order_by("-date_maintained")
    return render(request, "train_maintain/maintenance.html", context={"maintenance_list":model_object})

class MaintainDetailView(DetailView):
    model = MaintenanceTask
    template_name = "train_maintain/maintenance-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context