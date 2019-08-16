import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','practise.settings')
import django
django.setup()
from practise_app.models import Users
from faker import Faker

fakegen = Faker()

def populate(N = 5):
    for i in range(N):
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email_id = fakegen.email()
        user_created = Users.objects.get_or_create(first_name = fake_first_name,last_name = fake_last_name,email_id = fake_email_id)[0]

if __name__ == '__main__':
    print("Populating the script!!")
    populate(20)
    print("Populating finished!")
