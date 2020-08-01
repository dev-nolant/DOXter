#imports
import os, requests, json, time, configparser, sys
from lxml import html
from os import system
from termcolor import colored
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format
#pre-establish
version = "\".01\""
system("title "+"DOXter - V"+version+"Alpha")
os.system("cls")
#restard cog
def restart():
        print("argv was",sys.argv)
        print("sys.executable was", sys.executable)
        print("restart now")

        os.execv(sys.executable, ['python'] + sys.argv)

def main():
    #Cool into
    print(colored("Welcome! This is alpha version"+version+"- Updates Frequent. Check back to the github for more updated codes.",'green'),colored("https://github.com/StevenHarvey/DOXter", 'yellow'))
    input("Press Enter")
    os.system("cls")
    cprint(figlet_format('DOXter', font='smscript'),
       'white', 'on_red', attrs=['bold'])
    input("Press Enter")
  
 
 
                                                                 
def version_check():
    if version == str(configParser.get('main-config', 'version')):
        main()
    else:
        print(colored("NEW VERSION AVAILABLE! - GO TO https://github.com/StevenHarvey/DOXter", 'red'))
        input("Press Enter to continue regularly (Recommended To Update)")
        os.system("cls")
        main()
def TOS_CHECK():
    try:
        TOSc = open("TOS.txt", encoding="utf8").read()
        if "DO YOU ACCEPT: TRUE" in TOSc or "DO YOU ACCEPT: True" in TOSc or "DO YOU ACCEPT: true" in TOSc:
            version_check()
        else:
            print(colored("ERROR - Please accept the TOS, (Change the \"FALSE\" to \"TRUE\" at the end of the TOS)", 'yellow'))
            print(colored("--------------------------------------------------------------------------------------", 'yellow'))
            input(colored("Press Enter to exit", 'red'))
    except FileNotFoundError:
        Handler = open(r"temp\logs\log.txt", "w")
        Handler.write("TOS Error - A1 - Missing TOS File - (Please Get it from the GitHub = https://raw.githubusercontent.com/StevenHarvey/DOXter/master/TOS.txt)")
        Handler.close()
        print("ERROR - CHECK LOGS")
        input(" ")

def config_handler():
    try:
        if open("config.cfg", "r").read() == open(r"temp\cfg\configtemp.cfg", "r").read():
            #[main-config]
            global pathlog
            pathlog = configParser.get('main-config', 'logdir')
            os.remove(r"temp\cfg\configtemp.cfg")
            TOS_CHECK()
        else:
            try:
                r = requests.get("https://raw.githubusercontent.com/StevenHarvey/DOXter/master/config.cfg")
                foo = open("config.cfg", "w")
                foo.write(r.text)
                foo.close()
                restart()
            except:
                os.system("cls")
                print(colored("ERROR - PLEASE RESTART PROGRAM", 'yellow'))
                input(colored("Press Enter to Restart", 'red'))
                restart()
    except:
        try:
            r = requests.get("https://raw.githubusercontent.com/StevenHarvey/DOXter/master/config.cfg")
            foo = open("config.cfg", "w")
            foo.write(r.text)
            foo.close()
            restart()
        except:
            os.system("cls")
            print(colored("ERROR - PLEASE RESTART PROGRAM", 'yellow'))
            input(colored("Press Enter to Restart", 'red'))
            restart()
#configs
try:
    configParser = configparser.RawConfigParser()
    configFilePath = r'config.cfg'
    configParser.read(configFilePath)
    r = requests.get("https://raw.githubusercontent.com/StevenHarvey/DOXter/master/config.cfg")
    filehandle = open(r"temp\cfg\configtemp.cfg", "w")
    filehandle.write(r.text)
    filehandle.close()
    config_handler()
except:
    config_handler()