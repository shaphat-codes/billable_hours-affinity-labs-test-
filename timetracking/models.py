from django.db import models
import logging

logger = logging.getLogger(__name__)

class Timetable(models.Model):
    employee_id = models.IntegerField()
    billable_rate = models.DecimalField(max_digits=10, decimal_places=2)
    project = models.CharField(max_length=255)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def save(self, *args, **kwargs):
        # Check if the object already has an ID
        if not self.id:
            self.id = None  # Set to None to let the database generate the ID
        super().save(*args, **kwargs)


class Invoice(models.Model):
    employee_id = models.PositiveIntegerField(null=True, blank=True)
    company = models.CharField(max_length=255)
    number_of_hours = models.DurationField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    # total = models.DecimalField(max_digits=20, decimal_places=2)

    def get_formatted_duration(self):
        total_seconds = self.number_of_hours.total_seconds()
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours)} hours and {int(minutes)} minutes"

