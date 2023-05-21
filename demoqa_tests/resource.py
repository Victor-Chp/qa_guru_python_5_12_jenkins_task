import os

def path(file_name):
    return str(os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.path.pardir, f'tests/resources/{file_name}')
        ))
