
from getpass import getpass
from rich import print as rprint


username  =  getpass("Username: ")
password  =  getpass("Password: ")
secret    =  getpass("secret: ")

while True:
    if username == "Automation" and password == "cisco123" and secret == "cisco123":
        break
    else:
        rprint("[red]Invalid Username or Password[/red]"+"\n")
        username  =  getpass("Username: ")
        password  =  getpass("Password: ")
        secret    =  getpass("secret: ")
