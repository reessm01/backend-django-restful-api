from django.core.management.base import BaseCommand, CommandError
from django_api.Shoe.models import ShoeType, ShoeColor

class Command(BaseCommand):
    help = 'Initializes the ShoeType & ShoeColor model class with predefined values'

    def add_arguments(self, parser):
        parser.add_argument('init')

    def handle(self, *args, **options):
        if not ShoeType.objects.all():
            shoe_types = [
                'sneaker',
                'boot',
                'sandal',
                'dress',
                'other'
            ]

            for _type in shoe_types:
                ShoeType.objects.create(style=_type)
            
            self.stdout.write(self.style.SUCCESS('Shoe types successfully initialized.'))
        else:
            self.stdout.write(self.style.NOTICE('Shoe types already initialized.'))

        if not ShoeColor.objects.all():
            color_choices = [
                'red',
                'orange',
                'yellow',
                'green',
                'blue',
                'indigo',
                'violet',
                'black',
                'white'
            ]

            for color in color_choices:
                ShoeColor.objects.create(color_name=color)

            self.stdout.write(self.style.SUCCESS('Shoe color choices successfully initialized.'))
        else:
            self.stdout.write(self.style.NOTICE('Shoe color choices already initialized.'))            
        
        self.stdout.write(self.style.SUCCESS('Finished initialization sequence.'))