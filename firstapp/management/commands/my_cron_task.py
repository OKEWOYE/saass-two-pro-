from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Runs scheduled cron task"

    def handle(self, *args, **kwargs):
        print("Cron job is running successfully")