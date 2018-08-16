from fabric.api import local, warn, env
from fabric.colors import green, red

def run_with_venv(command, capture=True, warn_only=True):
    env.warn_only = warn_only
    result = local('source venv/bin/activate && {}'.format(command), capture=capture)
    if result.stderr:
        print(result.stderr)
        print(red("--------- ERROR ---------"))
    else:
        print(green("--------- successfully completed ---------"))

def debug(var=""):
    run_with_venv("./manage.py runserver {0}".format(var), capture=False)

def test(app_name="", method_name=""):
    """
    For pytest execute with params. 
    e.g. -> 
        app: fab test:test_api.py
        def: fab test:test_api.py,test_method
    """
    if app_name:
        covStr = " && coverage report | grep {0}".format(app_name.replace('test_','').replace('.py', ''))
        app_name = "mobile_api/tests/{0}".format(app_name)
        if method_name:
            app_name = "{0}::TestClass::{1}".format(app_name, method_name)
        app_name += covStr
    run_with_venv("pytest --cov-fail-under=0 {0}".format(app_name), capture=False, warn_only=False)
    

def manage(var):
    run_with_venv("./manage.py {0}".format(var), capture=False)

def celery():
    run_with_venv("DJANGO_SETTINGS_MODULE='_project.settings.local' celery -A _project worker -l info")