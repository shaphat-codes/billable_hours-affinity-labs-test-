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
        return Timetable.objects.create(**validated_data)
    
class InvoiceSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    employee_id = serializers.IntegerField()
    company = serializers.CharField(max_length=255)
    duration = serializers.CharField(source='get_formatted_duration', read_only=True)
    unit_price = serializers.DecimalField(max_digits=10, decimal_places=2)
    cost = serializers.DecimalField(max_digits=10, decimal_places=2)

 
    class Meta:
        model = Invoice
        fields = ('id', 'employee_id', 'company', 'duration', 'unit_price', 'cost')

    def create(self, validated_data):
        return Invoice.objects.create(**validated_data)
