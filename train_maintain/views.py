from .models import Train as train, MaintenanceTask as maintenancetask, MaintenanceCrew as maintenancecrew
from django.views.generic import DetailView
from django.shortcuts import render
from django.urls import reverse

def pageview(request):
    model_object = maintenancetask.objects.raw(
        '''
        SELECT maintenance_task_id, train_maintain_maintenancecrew.crew_id AS "Crew No.", train_maintain_maintenancecrew.crew_leader AS "Crew Leader", CONCAT('I.D: ', train_maintain_train.train_id,' (Model: ', train_maintain_train.train_model, ')') AS "Train Maintained", train_maintain_maintenancetask.date_maintained AS "Maintenance Date", train_maintain_maintenancetask.maintenance_description AS "Description of Maintenance", train_maintain_maintenancetask.condition AS "Conditions After Maintenance"
        FROM train_maintain_maintenancecrew, train_maintain_train, train_maintain_maintenancetask
        WHERE train_maintain_maintenancecrew.crew_id = train_maintain_maintenancetask.crew_id
        AND train_maintain_train.train_id = train_maintain_maintenancetask.train_id
        AND train_maintain_maintenancetask.date_maintained = '2023-08-14'
        ORDER BY "Maintenance Date" DESC;
        '''
    )
    return render(request, "train_maintain/maintenance.html", context={"maintenance_list":model_object})