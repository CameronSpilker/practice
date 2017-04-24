import os, os.path, sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'practice.settings'
import django
django.setup()


#imports for our project
from django.core import management
from django.db import connection
from django.contrib.contenttypes.models import ContentType
from homepage import models as cmod



from datetime import datetime
from decimal import Decimal

# ensure the user really wants to do this
areyousure = input('''
  You are about to drop and recreate the entire database.
  All data are about to be deleted.  Use of this script
  may cause itching, vertigo, dizziness, tingling in
  extremities, loss of balance or coordination, slurred
  speech, temporary zoobie syndrome, longer lines at the
  testing center, changed passwords in Learning Suite, or
  uncertainty about whether to call your professor
  'Brother' or 'Doctor'.

  Please type 'yes' to confirm the data destruction: ''')
if areyousure.lower() != 'yes':
    print()
    print('  Wise choice.')
    sys.exit(1)

# initialize the django environment
os.environ['DJANGO_SETTINGS_MODULE'] = 'practice.settings'
import django
django.setup()


# drop and recreate the database tables
print()
print('Living on the edge!  Dropping the current database tables.')
with connection.cursor() as cursor:
    cursor.execute("DROP SCHEMA public CASCADE")
    cursor.execute("CREATE SCHEMA public")
    cursor.execute("GRANT ALL ON SCHEMA public TO postgres")
    cursor.execute("GRANT ALL ON SCHEMA public TO public")

# make the migrations and migrate
management.call_command('makemigrations')
management.call_command('migrate')



#create a Category
cat1 = cmod.Category()
cat1.author = 'Marvin Minsky'
cat1.quote = 'The basic idea in case-based, or CBR, is that the program has stored problems and solutions. Then, when a new problem comes up, the program tries to find a similar problem in its database by finding analogous aspects between the problems.'
cat1.tags = 'Problem Problems Finding'
cat1.save()

cat2 = cmod.Category()
cat2.author = ''' Tim O'Reilly '''
cat2.quote = 'Why did Google, for example, recently decide to offer free 411 service? I havent talked to people at Google, but its pretty clear to me why. Its because of speech recognition. It has nothing to do with 411 service: it has to do with getting a database of voices, so they dont have to license speech technology from Nuance or someone else.'
cat2.tags = 'Technology Service Free'
cat2.save()

cat3 = cmod.Category()
cat3.author = 'Ted Nelson'
cat3.quote = 'So, what you can do in Microsoft Word is what Bill Gates has decided. What you can do in Oracle Database is what Larry Ellison and his crew have decided.'
cat3.tags = 'You Microsoft Crew'
cat3.save()

cat4 = cmod.Category()
cat4.author = 'M. J. Rose'
cat4.quote = 'Dont add people to your subscriber list just because they once wrote you a note. Or once answered a note you wrote to them. Dont put your address book into your newsletter database. Let your readers sign up. '
cat4.tags = 'You'
cat4.save()

cat5 = cmod.Category()
cat5.author = 'Mary Roach'
cat5.quote = 'My books are not really books; theyre endless chains of distraction shoved inside a cover. Many of them begin at the search box of Pub Med, an Internet database of medical journal articles. '
cat5.tags = 'Medical Internet Search'
cat5.save()

cat6 = cmod.Category()
cat6.author = 'David Blunkett'
cat6.quote = 'I said its impossible to have an amnesty without ID cards and a clean database, because you firstly dont have any incentives for people to actually come up front and register, and make themselves available, and secondly you have no means of tracking them. '
cat6.tags = 'Impossible People Cards'
cat6.save()


cat7 = cmod.Category()
cat7.author = 'Micheal Hayden'
cat7.quote = 'Access to the security clearance database would disgorge even more detailed personal information, including the foreign contacts of American officials.'
cat7.tags = 'Information Security'
cat7.save()
