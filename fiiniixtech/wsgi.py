"""
WSGI config for fiiniixtech project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys

# place this before(!!) any package import that belongs to virtual env

# replacement for WSGIPythonHome "d:/..../django_project/env_folder"
# choose one:

sys.path.append('f:/py_env/env/Lib/site-packages')   # add individual virt.environment packages at the end of sys.path;  global env packages have prio
#sys.path.insert(0,'F:/py_env/env/Lib/site-packages') # add individual virt.environment packages at the beginning of sys.path;  indiv. virt.env packages have prio over global env

# replacement   WSGIPythonPath "d:/..../django_project/app_name" 
sys.path.append("f:/py_env/fiiniixtech") 


from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fiiniixtech.settings')
#os.environ['DJANGO_SETTINGS_MODULE'] = 'fiiniixtech.settings'

application = get_wsgi_application()
