#imports
import os, requests, json, time, configparser, sys, datetime, getopt
from lxml import html
from os import system
from termcolor import colored
from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint 
from pyfiglet import figlet_format
#pre-establish
version = "\".01\""
system("title "+"DOXter - V"+version+"A")
os.system("cls")
time = datetime.datetime.now()
def Handler(arg):
    loghandler = open(r"temp\logs\log.txt", "a")
    loghandler.write("\n"+arg+" "+str(datetime.datetime.now()))
    loghandler.close()
#restard_handler
def restart():
        print("argv was",sys.argv)
        print("sys.executable was", sys.executable)
        print("restart now")
        os.execv(sys.executable, ['python'] + sys.argv)

def main():
    print(colored("Welcome! This is alpha: "+version, 'red'),colored(" \nLatest Build: "+configParser.get('main-config', 'version'),'magenta'),colored("\nUpdates Frequent. Check back to the github for more updated codes.",'yellow'),colored("https://github.com/StevenHarvey/DOXter", 'green'))
    input("Press Enter To Continue Normally")
    def cog_selects():
        os.system("cls")
        cprint(figlet_format('DOXter', font='smscript'),
        'white', 'on_red', attrs=['bold'])
        try:
            cog_select = input(colored("Drag COG and press \'enter\': ", 'blue'))
        except SyntaxError:
            print(colored("Invalid COG!", "red"))
            input("Press Enter to Reselect")
            os.system('cls')
            cog_selects()
        try:
            if cog_select:
                try:
                    os.system('cls')
                    os.system('python '+cog_select)
                except OSError:
                    print(colored("Invalid COG!", "red"))
                    input("Press Enter to Reselect")
                    os.system('cls')
                    cog_selects()
                except:
                    print("ERROR CHECK LOGS")
                    Handler("UNKNOWN CRASH - MM1A - RESTART")
                    input()
            else:
                print(colored("Invalid COG!", "red"))
                input("Press Enter to Reselect")
                os.system('cls')
                cog_selects()
        except:
            print(colored("Invalid COG!", "red"))
            input("Press Enter to Reselect")
            os.system('cls')
            cog_selects()
    cog_selects()
                                                           
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
        Handler("ERROR - TOS NOT FOUND - https://github.com/StevenHarvey/DOXter/blob/master/TOS.txt")
        print("ERROR - CHECK LOGS")
        input()

def config_handler():
    try:
        if open("config.cfg", "r").read() == open(r"temp\cfg\configtemp.cfg", "r").read():
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
def update():
    configParser = configparser.RawConfigParser()
    configFilePath = r'config.cfg'
    configParser.read(configFilePath)
    print(configParser.get('main-config', 'version')+ " Is the current posted version of DOXter on github!")
def prefig():
    try:
        global configParser
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
def arghandler(argv):
   try:
      opts, args = getopt.getopt(argv, "ur")
   except getopt.GetoptError:
      os.system("python main.py -r")
   for opt, arg in opts:
        if opt in ("-u",):
            update()
        elif opt in ("-r"):
            prefig()
        else:
            os.system("python main.py -r")
if __name__ == "__main__":
    arghandler(sys.argv[1:])
