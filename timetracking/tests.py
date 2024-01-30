from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from io import BytesIO
import csv

class TimetableTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_create_timetable_valid_csv(self):
        csv_content = "employee_id,billable_rate,project,date,start_time,end_time\n1,50,ProjectA,2024-01-28,09:00,17:00"
        csv_file = BytesIO(csv_content.encode('utf-8'))
        csv_file.name = 'test.csv'

        response = self.client.post('/api/v1/timetable', {'file': csv_file}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_timetable_invalid_csv(self):
        invalid_csv_content = "invalid_header,invalid_data\n1,2"
        invalid_csv_file = BytesIO(invalid_csv_content.encode('utf-8'))
        invalid_csv_file.name = 'invalid_test.csv'

        response = self.client.post('/api/v1/timetable', {'file': invalid_csv_file}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_timetable_missing_file(self):
        response = self.client.post('/api/v1/timetable')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

