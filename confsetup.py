from os import system, name, remove
from os.path import exists

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

clear()
system('title -- Server Cloner Configuration Setup --')
print('-- SERVER CLONER CONFIGURATION SETUP --')
print()
inputgid = input('INPUT GUILD ID : ')
outputgid = input('OUTPUT GUILD ID : ')
token = input('DISCORD ACCOUNT TOKEN : ')
cserver = input('CLEAR SERVER? (Y/n) (Optional) : ')
windows = input('RUNNING ON WINDOWS? (Y/n) (Optional) : ')
print()
print('Setting Configuration...')
file_exists = exists('config.py')
if file_exists == True:
    remove('config.py')
if cserver == "Y".lower():
    cserver = True
elif cserver == "N".lower():
    cserver = False
else:
    cserver = True
if windows == "Y".lower():
    windows = True
elif windows == "N".lower():
    windows = False
else:
    windows = True
f = open('config.py', 'w+')
f.write(f"""
################################## Configuration ##################################
input_guild_id = "{inputgid}"  # The ID of the server that you're copying
output_guild_id = "{outputgid}"  # The ID of the server that you're pasting onto
token = "{token}"  # <-- Account token. (user)
clear_server = {cserver} # Whether to clear the server you're pasting to or not (To delete old channels, roles, etc)
windows = {windows} # Whether you're on windows or not (for titling)
###################################################################################
""")
f.close()
print('Successfully Setup The Configuration.')
launch = input('Would you like to launch the Server Cloner? (Y/n) (Optional) : ')
if launch == "Y".lower():
    system('start.bat')
    exit()
elif launch == "N".lower():
    exit()
else:
    system('start.bat')
    exit()