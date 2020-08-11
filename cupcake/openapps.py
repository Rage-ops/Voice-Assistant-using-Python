import os
from response import cupcakeResponse


def open_app(app_name):
    name = ''
    for letter in app_name:
        if letter == ' ':
            name += '\ '
        else:
            name += letter
    print(name)
    path = f"/Applications/{name}.app"
    os.system(f"open {path}")
    cupcakeResponse(f"Opening {app_name}")
