#!/usr/bin/python3
import argparse
import subprocess


if __name__ == '__main__':
    home = subprocess.os.environ.get('HOME')

    parser = argparse.ArgumentParser(description='A simple command-line tool to manage proxy settings')
    main_args = parser.add_argument_group()

    main_args.add_argument('-S','--setProxy',action='store_true', 
                        help='Set best proxy automatically')
    main_args.add_argument('-T',
                        '--torPing',
                        help='Perform ping via tor'\
                        +', Helps to keep connection alive',
                        action='store_true')
    main_args.add_argument('-C',
                        '--customProxy',
                        nargs=1,
                        help='Set your own proxy') 
    parser.add_argument('-U',
                        '--update',
                        action='store_true', 
                        help='Update ProxyHelper package')
    main_args.add_argument('-G',
                        '--getProxy',
                        action='store_true', 
                        help='Print the best proxy, but don\'t set it.')
    parser.add_argument('--configure',
                        action='store_true', 
                        help='Configure defaults in proxyhelper')
    arg = parser.parse_args()

    if arg.setProxy:
        subprocess.call(['bash',
                        '{}/.proxyhelper/zetproxy'.format(home)])
    elif arg.torPing:
        subprocess.call(['python3',
                        '{}/.proxyhelper/torpinger'.format(home)])
    elif arg.customProxy:
        subprocess.call(['bash',
                        '{}/.proxyhelper/zetproxy'.format(home)
                        ,'Proxy',arg.customProxy[0]])
         
    elif arg.getProxy:
        subprocess.call(['python3',
                        '{}/.proxyhelper/surely_parallel.py'.format(home)])
        
    elif arg.update:
        print('Updating ProxyHelper.')
    else:
        parser.print_help()

