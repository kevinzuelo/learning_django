import os
import django
from faker import Faker
import random

# Fake population script

fake_gen = Faker()
topics = ['Search', 'Social', 'marketplace', 'News', 'Games']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(n=5):
    for entry in range(n):
        top = add_topic()
        fake_url = fake_gen.url()
        fake_date = fake_gen.date()
        fake_name = fake_gen.company()

        page = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        acc_rec = AccessRecord.objects.get_or_create(name=page, date=fake_date)[0]


if __name__ == '__main__':
    print("populating script!")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')
    django.setup()
    from first_app.models import AccessRecord, Webpage, Topic

    populate(20)
    print("populating complete!")