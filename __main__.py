import os

# Import configuration loader:
from loader import ConfigLoader

# Load configuration file:
loader = ConfigLoader(os.path.dirname(os.path.realpath(__file__)) + '/config.ini')

# Print database configuration:
database = loader.get('database')
print(' [ Database ] ')
print(' ==> %s' % database)
print(' ==> %s' % database['host'])

# Print mail configuration:
print(' [ Mail ] ')
mail = loader.get('mail')
print(' ==> %s' % mail)
print(' ==> %s' % mail['global'])