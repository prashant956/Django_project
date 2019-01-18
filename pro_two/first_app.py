import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'pro_two.settings'


import django
django.setup()

## FAKE pop scrippt

import random
from first_app.models import AccessRecord, Webpage, Topic
from faker import Faker

fakegen = Faker()
topics =['Search','social','Marketplace','News','Games']

def add_topic():
    t= Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):

    for entry in range(N):

        #get the topic for entry
        top = add_topic()

        #Create the fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #create the new webpage entery
        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_url)[0]

        #create a fake access record for that Webpage

        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("populating complete!")
