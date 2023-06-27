
from getpass import getpass
from rich import print as rprint


username =   input("Username: ")
password = getpass("password: ")
secret   = getpass("enable password: ")

while True:
    if username == "Automation" and password == "cisco123" and secret == "cisco123":
        break
    else:
        rprint("[red]Incorrect Username or Password![/red]")
        username =   input("Username: ")
        password = getpass("password: ")
        secret   = getpass("enable password: ")
      