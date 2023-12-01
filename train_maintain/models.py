from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_custom_format(value):
  first_char = value[0]
  if first_char not in ['S', 'A']:
    raise ValidationError(_('The first character must be either "S" or "A."'))

  rest_of_value = value[1:]
  if not rest_of_value.isdigit():
    raise ValidationError(_('The remaining characters must be numbers.'))

class Train(models.Model):
  train_id = models.AutoField(primary_key=True)
  train_model = models.CharField(max_length=15, validators=[validate_custom_format])
  max_speed = models.IntegerField()
  no_of_seats = models.IntegerField()
  no_of_toilets = models.IntegerField()
  has_reclining_seats = models.BooleanField()
  has_folding_tables = models.BooleanField()
  has_disability_access = models.BooleanField()
  has_luggage_storage = models.BooleanField()
  has_vending_machine = models.BooleanField()
  has_food_service = models.BooleanField()

class MaintenanceCrew(models.Model):
  crew_id = models.AutoField(primary_key=True)
  crew_leader = models.CharField(max_length=60)
  specialty_skill = models.TextField(max_length=255)

class MaintenanceTask(models.Model):
  maintenance_task_id = models.AutoField(primary_key=True)
  date_maintained = models.DateField()
  condition = models.CharField(max_length=50)
  maintenance_description = models.TextField(max_length=255)
  crew = models.ForeignKey(MaintenanceCrew, on_delete=models.CASCADE)

