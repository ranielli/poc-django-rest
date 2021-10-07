import csv
from django.core.management.base import BaseCommand
from customers.models import Customer

class Command(BaseCommand):
    help = "Loads Customers from CSV file."

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str)

    def handle(self, *args, **options):
        file_path = options["file_path"]
        with open(file_path) as csv_file:
            csv_data = csv.reader(csv_file, delimiter=",")
            next(csv_data, None)
            customers = []
            for row in csv_data:
                print(row)                
                customer = Customer(
                    pk = int(row[0]),
                    first_name=row[1],
                    last_name=row[2],
                    email=row[3],
                    gender=row[4],
                    company=[4],
                    city=row[5],
                    title=row[6]
                )
                customers.append(customer)
            if customers:
                Customer.objects.bulk_create(customers)
        self.stdout.write(
            self.style.SUCCESS(
                f"Finished"
            )
        )