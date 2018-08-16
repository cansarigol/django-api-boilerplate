import sys

from django.core.management.base import BaseCommand
from django.core.servers.basehttp import (run, get_internal_wsgi_application, WSGIServer)

from django.utils import autoreload

class Command(BaseCommand):
    help = "Run tests before run to server"

    def add_arguments(self, parser):
        parser.add_argument('--just_this_test', 
        nargs='+', 
        type=str,
        help='Tells Django to NOT use the auto-reloader.',)

    def handle(self, *args, **options):
        autoreload.main(self.run, None, options)

    def execute(self, *args, **options):
        super().execute(*args, **options)

    def run(self, **options):
        autoreload.raise_last_exception()
        self.check(display_num_errors=True)
        self.stdout.write(self.style.SUCCESS('Server is running!'))
        
        run(addr="127.0.0.1", port=8000, wsgi_handler=get_internal_wsgi_application(), threading=True, server_cls=WSGIServer)
        