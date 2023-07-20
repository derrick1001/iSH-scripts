#!/usr/bin/python3.8

from netmiko import ConnectHandler
from time import sleep
from rich.progress import track
import colorama

# Auto reset color back to white after color call
colorama.init(autoreset=True)

# Colors we use
c_BLUE = f"{colorama.Style.BRIGHT}{colorama.Fore.BLUE}"
c_GREEN = f"{colorama.Style.BRIGHT}{colorama.Fore.GREEN}"
c_MAGENTA = f"{colorama.Style.BRIGHT}{colorama.Fore.MAGENTA}"
c_CYAN = f"{colorama.Style.BRIGHT}{colorama.Fore.CYAN}"
c_RED = f"{colorama.Style.BRIGHT}{colorama.Fore.RED}"

ip = input(f'{c_BLUE}IP-address: ')
user = input(f'{c_BLUE}User: ')
password = input(f'{c_BLUE}Password: ')
radio = input(f'{c_BLUE}HI or LO: ').upper()


def connect_to_radio(ip, user, password):
    device = {'device_type': 'generic',
              'host': ip,
              'username': user,
              'password': password,
              'fast_cli': False
              }
    conn = ConnectHandler(**device)
    return conn


def countdown(second):
    for n in track(range(second), description=f'{c_GREEN}Rebooting...'):
        sleep(1)


countdown(10)
countdown(20)


# def refresh(cmd):
#     while True:
#         output = con.send_command(cmd)
#         print(output)
#         if 'all components exist' in output:
#             print(f'{c_CYAN}Software is up to date.', end='\r')
#             break
#         elif 'Nothing to Update' in output:
#             print(f'{c_CYAN}Already up to date', end='\r')
#             break
#         elif '100' in output:
#             break
#         elif 'download in progress' in output:
#             parse_string = output.split()
#             print(f"{c_CYAN}{parse_string[8].capitalize()} {c_CYAN}{parse_string[9].capitalize()} {c_MAGENTA}{parse_string[10].capitalize()}", end='\r')
#             sleep(10)
#         elif 'install started' or 'installation in progress' in output:
#             parse_string = output.split()
#             print(f"{c_CYAN}{parse_string[8].capitalize()} {c_CYAN}{parse_string[9].capitalize()} {c_MAGENTA}{parse_string[10].capitalize()}", end='\r')
#             sleep(10)
#         else:
#             continue
# 
# 
# def software_dl():
#     dl_software = 'platform software download version protocol ftp'
#     set_software_param = 'platform software download channel server set server-ip 192.168.1.30 directory sd1/820S-Builds/820S-11-9/ username RSI-Admin password can0py_BAM'
#     status = 'platform software download status show'
# 
#     con.send_command(set_software_param)
#     con.send_command(dl_software,
#                      expect_string='Software Version to Download')
#     con.send_command('yes\n',
#                      expect_string='root>',
#                      delay_factor=2
#                      )
#     print(f'{c_GREEN}Downloading software..')
#     sleep(2)
#     refresh(status)
#     sleep(3)
#     print(f'{c_GREEN}Software successfully uploaded.')
#     sleep(2)
#     print(f'{c_GREEN}Upgrading firmware..')
#     install_func()
# 
# 
# def install_func():
#     install_software = 'platform software install version'
#     status = 'platform software install status show'
#     con.send_command(install_software,
#                      expect_string=r'Software version to be installed:')
#     con.send_command('yes\n',
#                      expect_string='root>',
#                      delay_factor=2
#                      )
#     refresh(status)
#     sleep(3)
#     print(f'{c_GREEN}Installation complete.')
#     sleep(2)
#     # countdown(250)
#     # import_func(radio)
# 
# 
# def import_func(radio_type):
#     set_template_params = f'platform configuration channel server set ip-address 192.168.1.30 directory sd1/820S-Builds/ filename 820S-12-0-{radio_type}-template.zip username RSI-Admin password can0py_BAM'
#     import_template = 'platform configuration configuration-file import restore-point-1'
#     restore_template = 'platform configuration configuration-file restore restore-point-1'
#     con = connect_to_radio(ip='192.168.1.1', user='admin', password='admin')
# 
#     con.send_command(set_template_params)
#     con.send_command(import_template,
#                      expect_string='WARNING: This will replace the existing configuration file.',)
#     con.send_command('yes\n',
#                      expect_string='root>',)
#     print(f'{c_GREEN}Importing template..')
#     sleep(2)
#     while True:
#         output = con.send_command('platform configuration channel show status')
#         if 'succeeded' in output:
#             print(f'{c_GREEN}File transfer complete..')
#             break
#         elif 'failure' in output:
#             print(f'{c_RED}Something went wrong..')
#             break
#         else:
#             print(f'{c_CYAN}Validating..', end='\r')
#     sleep(2)
#     print(f'{c_GREEN}Restoring configuration..')
#     sleep(2)
#     con.send_command(restore_template,
#                      expect_string='WARNING: This will replace the working configuration. System will reboot.')
#     output = con.send_command('yes\n',
#                      expect_string='The system is going down for reboot NOW!')
#     if 'NOW!' in output:
#         print(f'{c_GREEN}Done..')
#     else:
#         print(f'{c_RED}Something went wrong')
#     sleep(1)
#     countdown(250)
# 
# 
# con = connect_to_radio(ip='192.168.1.1', user='admin', password='admin')
# print("\n")
# print(f'{c_GREEN}Gathering info..')
# software_dl()
# countdown(20)
