#imports
import os, requests, json, time, configparser, sys, datetime, getopt, pathlib
from lxml import html
from os import system
from termcolor import colored
from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint 
from pyfiglet import figlet_format
#pre-establish
version = "\".3\""
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
def update():
    configParser = configparser.RawConfigParser()
    configFilePath = r'config.cfg'
    configParser.read(configFilePath)
    print(colored("Current Version Out: "+str(configParser.get('main-config', 'version')), 'magenta'))
    input()
    os.close()
def dependencies_install():
    if str(1) in open(r'temp\cfg\utd.txt', 'r').read():
        prefig()
    else:
        try:
            os.system("pip install -r requirements.txt")
            os.system("cls")
            f = open(r'temp\cfg\utd.txt', "w+")
            f.write("1")
            f.close()
            prefig()
        except TypeError:
            Handler("TypeError on PIP dependencies: "+str(TypeError))
            input("")
            os.close()
        except OSError:
            Handler("ERROR ON PIP INSTALLING: "+str(OSError))
            input("")
            os.close()
        except:
            Handler("ERROR ON PIP DEPENDENCIES - CRITICAL // PLEASE WAIT FOR AN ADMIN TO FIX THIS")
            input("")
            os.close()
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
            print("Error with "+ args + " and " + arg)   
        
if __name__ == "__main__":
    arghandler(sys.argv[1:])
dependencies_install()