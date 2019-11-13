from django.core.management.base import BaseCommand
from rooms.models import HouseRule


class Command(BaseCommand):

    help = "This command creates house rules!"

    def handle(self, *args, **options):
        house_rules = [
            "You can keep a suitcase",
            "long-term accommodation",
            "Check in & out",
            "Close the door",
            "Lock the door",
            "Quiet",
        ]
        for rule in house_rules:
            HouseRule.objects.create(name=rule)
        self.stdout.write(self.style.SUCCESS(f"{len(house_rules)} Rules created!"))
