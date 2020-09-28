from django.core.management.base import BaseCommand
from datetime import datetime, timedelta
from time import sleep

from proj.reservationapp import tasks
from config import celery_app


class Command(BaseCommand):
    help = 'Example command adding and cancelling task'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        celery_app.control.purge()
        result = tasks.example_task.apply_async(
            (3, 5),
            eta=datetime.now() + timedelta(seconds=10),
            expires=datetime.now() + timedelta(seconds=20)
        )
        sleep(3)

        tasks.revoke_celery_task(result.id)
