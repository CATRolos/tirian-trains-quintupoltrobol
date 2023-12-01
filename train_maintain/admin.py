from django.contrib import admin
from .models import Train, MaintenanceCrew, MaintenanceTask

class TrainAdmin(admin.ModelAdmin):
  model = Train

class MaintenanceCrewAdmin(admin.ModelAdmin):
  model = MaintenanceCrew

class MaintenanceTaskAdmin(admin.ModelAdmin):
  model = MaintenanceTask

admin.site.register(Train, TrainAdmin)
admin.site.register(MaintenanceCrew, MaintenanceCrewAdmin)
admin.site.register(MaintenanceTask, MaintenanceTaskAdmin)

