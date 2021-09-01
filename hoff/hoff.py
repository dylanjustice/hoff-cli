"""
#    #       ####  #    # ######    ##### #    # ######    #    #  ####  ###### ###### ### 
#    #      #    # #    # #           #   #    # #         #    # #    # #      #      ### 
#    #      #    # #    # #####       #   ###### #####     ###### #    # #####  #####   #  
#    #      #    # #    # #           #   #    # #         #    # #    # #      #          
#    #      #    #  #  #  #           #   #    # #         #    # #    # #      #      ### 
#    ######  ####    ##   ######      #   #    # ######    #    #  ####  #      #      ### 

Usage:    hoff <argument> (--options)

Options:
    -v --version    output the version number
    -h --help       Show this screen

Arguments:
    copy            Copy files and/or directories
    deploy          Deploy various application types
    dotnet          Run various dotnet commands for the project
    dotnet-test     Run various dotnet test runner commands for the project
    github          Commands for interacting with AndcultureCode github resources
    health-check    Send a web request to a given endpoint on an interval to verify the HTTP response code
    install         Collection of commands related to installation and configuration of the and-cli
    list            List all commands/options
    migration       Run commands to manage Entity Framework migrations
    nuget           Manages publishing of nuget dotnet core projects
    restore         Restores application data assets for various application types
    webpack         Run various webpack commands for the project
    webpack-test    Run various webpack test commands for the project
    workspace       Manage AndcultureCode projects workspace
    help [command]  display help for command    

"""
from docopt import docopt
import pkg_resources

def version():
    version = pkg_resources.require("hoff-cli")[0].version
    print(version)

def main():
    arguments = docopt(doc=__doc__, help=True)

    if arguments['--version'] or arguments['-v']:
        version()
        exit(0)

    print(arguments)

if __name__ == '__main__':
    main()

    