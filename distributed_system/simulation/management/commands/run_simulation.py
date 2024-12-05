from django.core.management.base import BaseCommand
from simulation.utils import simulate_insertions

class Command(BaseCommand):
    help = "Run simultaneous insertions"

    def handle(self, *args, **kwargs):
        simulate_insertions()
        self.stdout.write(self.style.SUCCESS("Simultaneous insertions completed!"))
