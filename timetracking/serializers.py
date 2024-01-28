# serializers.py
from rest_framework import serializers
from .models import Timetable, Invoice

class TimetableCSVSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    employee_id = serializers.IntegerField()
    billable_rate = serializers.DecimalField(max_digits=10, decimal_places=2)
    project = serializers.CharField(max_length=255)
    date = serializers.DateField()
    start_time = serializers.TimeField()
    end_time = serializers.TimeField()

    def create(self, validated_data):
        # Your logic to create and return a Timetable instance using validated_data
        return Timetable.objects.create(**validated_data)
    
class InvoiceSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    employee_id = serializers.IntegerField()
    company = serializers.CharField(max_length=255)
    number_of_hours = serializers.CharField(max_length=255)
    unit_price = serializers.DecimalField(max_digits=10, decimal_places=2)
    cost = serializers.DecimalField(max_digits=10, decimal_places=2)

 
    class Meta:
        model = Invoice
        fields = '__all__'

    def create(self, validated_data):
        # Your logic to create and return a Timetable instance using validated_data
        return Invoice.objects.create(**validated_data)
