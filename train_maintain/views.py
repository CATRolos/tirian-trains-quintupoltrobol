from .models import Train as train, MaintenanceTask as maintenancetask, MaintenanceCrew as maintenancecrew
from django.shortcuts import render
from django.urls import reverse

def pageview(request):
    # Get the parameter from the URL if any header is clicked
    order_by = request.GET.get('order_by', 'date_maintained')  # Default to sorting by 'date_maintained'
    arrangement = request.GET.get ('arrangement', 'DESC') # Default to descending
    
    # Define the columns that are sortable
    sortable_columns = {
        'maintenance_task_id': 'maintenance_task_id',
        'date_maintained': 'train_maintain_maintenancetask.date_maintained',
        'train_id': 'train_maintain_train.train_id',
        'maintenance_description': 'train_maintain_maintenancetask.maintenance_description',
        'condition': 'train_maintain_maintenancetask.condition',
        'crew_id': 'train_maintain_maintenancecrew.crew_id',
    }
    
    # Check if the column is sortable
    if order_by not in sortable_columns:
        order_by = 'date_maintained'  # Set to default sorting if the column is not in the sortable_columns

    query = f'''
        SELECT maintenance_task_id, train_maintain_maintenancecrew.crew_id AS "Crew No.", 
        train_maintain_maintenancecrew.crew_leader AS "Crew Leader", 
        CONCAT('I.D: ', train_maintain_train.train_id,' (Model: ', train_maintain_train.train_model, ')') AS "Train Maintained", 
        train_maintain_maintenancetask.date_maintained AS "Maintenance Date", 
        train_maintain_maintenancetask.maintenance_description AS "Description of Maintenance", 
        train_maintain_maintenancetask.condition AS "Conditions After Maintenance"
        FROM train_maintain_maintenancecrew, train_maintain_train, train_maintain_maintenancetask
        WHERE train_maintain_maintenancecrew.crew_id = train_maintain_maintenancetask.crew_id
        AND train_maintain_train.train_id = train_maintain_maintenancetask.train_id
        ORDER BY {sortable_columns[order_by]} {arrangement};
    '''

    # Fetch data using the raw SQL query
    model_object = maintenancetask.objects.raw(query)

    return render(request, "train_maintain/maintenance.html", context={"maintenance_list":model_object, "order_by": sortable_columns[order_by], "arrangement": arrangement})