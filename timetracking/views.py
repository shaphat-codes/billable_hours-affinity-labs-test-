# timetracker/timetracking/views.py
from io import TextIOWrapper, BytesIO
import csv
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Timetable, Invoice
from .serializers import *
from rest_framework import status, parsers
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

@api_view(['GET'])
def list_timetables(request):
    if request.method == 'GET':
        timetables = Timetable.objects.all()
        serializer = TimetableCSVSerializer(timetables, many=True)
        return Response(serializer.data)

class TimetableProcessor:

    def __init__(self, request):
        self.request = request
        self.csv_file = self.request.data.get('file')
        self.csv_data = None

    def process_timetables(self):
        if not self.csv_file:
            return Response({"error": "File not provided."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            csv_content = self.csv_file.read().decode('utf-8')
            self.csv_data = list(csv.reader(csv_content.splitlines()))

            header = self.csv_data[0] if self.csv_data else []
            self.csv_data = self.csv_data[1:] if self.csv_data else []

            csv_dicts = [dict(zip(header, row)) for row in self.csv_data]

            file_serializer = TimetableCSVSerializer(data=csv_dicts, many=True)

            if file_serializer.is_valid():
                self._save_timetable_data(file_serializer.validated_data)
                invoice = self._save_invoice_data(file_serializer.validated_data)
                return invoice

            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def _save_timetable_data(self, data):
        for row in data:
            try:
                Timetable.objects.create(
                    employee_id=row['employee_id'],
                    billable_rate=row['billable_rate'],
                    project=row['project'],
                    date=row['date'],
                    start_time=row['start_time'],
                    end_time=row['end_time']
                )
            except Exception as e:
                logger.error(f"Error creating the entry: {e}")

    def _save_invoice_data(self, data):
        total_cost = 0
        invoices = []

        for row in data:
            start_time = datetime.combine(datetime.today(), row['start_time'])
            end_time = datetime.combine(datetime.today(), row['end_time'])

            time_difference = end_time - start_time
            hours, remainder = divmod(time_difference.seconds, 3600)
            minutes = remainder // 60

            cost = row['billable_rate'] * hours
            total_cost += cost

            try:
                invoice = Invoice.objects.create(
                    company=row['project'],
                    employee_id=row['employee_id'],
                    number_of_hours=f"{hours} hours and {minutes} minutes",
                    unit_price=row['billable_rate'],
                    cost=cost,
                )
                invoices.append(invoice)
            except Exception as e:
                return Response({"error": "Invoice was not created"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = InvoiceSerializer(invoices, many=True)
        serialized_response = [{"total": total_cost}, serializer.data]
        return Response(serialized_response, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@parser_classes([parsers.MultiPartParser])
def create_timetable(request):
    timetable_processor = TimetableProcessor(request)
    return timetable_processor.process_timetables()