
import pyodbc
from django.core.management import BaseCommand
from config.settings import DATABASE, USER, DRIVER, HOST, PAD_DATABASE, PASSWORD


class Command(BaseCommand):

    def handle(self, *args, **options):
        connectString = f'''DRIVER={DRIVER};
                              SERVER={HOST};
                              DATABASE={PAD_DATABASE};
                              UID={USER};
                              PWD={PASSWORD};'''
        try:
            conn = pyodbc.connect(connectString)
            conn.autocommit = True
            conn.execute(f"CREATE DATABASE {DATABASE}")
        except pyodbc.ProgrammingError as ex:
            print(ex)
        else:
            print("База данных создана успешно")