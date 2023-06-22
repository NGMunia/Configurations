
from rich import print as rprint
def EEM_config():
    """This funtion will configure EEM applet to the router.
Automatic backup of start-up config to the TFTP server will occur every Monday to Friday at 11:30 PM"""
    rprint(f'[cyan]{EEM_config.__doc__}[/cyan]'+'\n')

#EEM_config()

def ntp_config():
    """This function will configure NTP on the devices"""
    rprint(f'[cyan]{ntp_config.__doc__}[/cyan]'+'\n')
ntp_config()

def netflow_config():
    """This function will configure NetFlow on the Network devices.
This forms part of Data traffic collection and analysis"""
    rprint(f'[cyan]{netflow_config.__doc__}[/cyan]'+'\n')
netflow_config()