"""hoff

#    #       ####  #    # ######    ##### #    # ######    #    #  ####  ###### ###### ### 
#    #      #    # #    # #           #   #    # #         #    # #    # #      #      ### 
#    #      #    # #    # #####       #   ###### #####     ###### #    # #####  #####   #  
#    #      #    # #    # #           #   #    # #         #    # #    # #      #          
#    #      #    #  #  #  #           #   #    # #         #    # #    # #      #      ### 
#    ######  ####    ##   ######      #   #    # ######    #    #  ####  #      #      ### 

Usage:
    ac dotnet (--options)
    ac (-h | --help)

Options:
    -h --help   Show this screen
"""
from dotnet import main
from docopt import docopt

def dotnet():
    main()

if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.0.1')
    if arguments['dotnet']:
        dotnet()
    print(arguments)

    