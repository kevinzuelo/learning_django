import os
import django
from faker import Faker

generator = Faker()

def populate(n=5):
    for entry in range(n):
        fake_first = generator.first_name()
        fake_last = generator.last_name()
        fake_email = generator.ascii_free_email()
        
        user = User.objects.get_or_create(first_name = fake_first, last_name = fake_last, email = fake_email)[0]

if __name__ == '__main__':
    print("populating script!")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_Two.settings')
    django.setup()
    from app_Two.models import User
    
    populate(20)
    print("populating complete!")