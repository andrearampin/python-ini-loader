# Python config files loader
This is a simple script for loading configuration settings from an ini file.

## Set up virtual environment
The following steps are required only if you want to execute the config loader within a virtual environment.

```
$ virtualenv configloader
$ source configloader/bin/activate
```

you should now have a new folder called *configloader* which will contain everything that your python interpreter needs to run this script.

## Loader

### Config file

In the repository there is already a sample *config.ini* file; you can use it for your own project.
The config file contains section that are defined by its title
```
[database]
...
```
Within the section there is the list of configurations:
```
name = test
user = root
password = root
host = localhost
```
Therefore, within the database section the following settings will be accessible:
- database.name
- database.user
- database.password
- database.host

### Python script
In order to access the config file as a disctionary simply import the configuration loader:
```
import os
from loader import ConfigLoader
```
And pass the configuration path to the loader:
```
loader = ConfigLoader(os.path.dirname(os.path.realpath(__file__)) + '/config.ini')
```
Now, if you want to access the database host config simply:
```
database = loader.get('database')
print(database['host'])
```
To run the script just run python
```
$ python .
```