#!/usr/bin/python3
import argparse
import subprocess


if __name__ == '__main__':
    # home = subprocess.os.environ.get('HOME')
    DIR_PATH = '/usr/share/proxyhelper'

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
                        help='Set your own proxy. eg. -C 172.16.24.3:3128') 
    main_args.add_argument('-N',
                        '--clearProxy',
                        action='store_true',
                        help='Reset the system proxy') 
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
    parser.add_argument('--manual',
                        action='store_true',
                        help='Enable manual mode')
    parser.add_argument('--auto',
                        action='store_true',
                        help='Enable automatic mode')
    arg = parser.parse_args()

    if arg.setProxy:
        subprocess.call(['bash',
                        '{}/zetproxy'.format(DIR_PATH)])
    elif arg.torPing:
        subprocess.call(['python3',
                        '{}/torpinger'.format(DIR_PATH)])
    elif arg.customProxy:
        subprocess.call(['bash',
                        '{}/zetproxy'.format(DIR_PATH)
                        ,'Proxy',arg.customProxy[0]])
    elif arg.clearProxy:
        subprocess.call(['bash',
                        '{}/zetproxy'.format(DIR_PATH),
                        'None'])
    elif arg.getProxy:
        subprocess.call(['python3',
                        '{}/surely_parallel.py'.format(DIR_PATH)])
    elif arg.manual:
        subprocess.call('sudo rm /etc/network/if-up.d/zetproxy', shell=True)
        subprocess.call('sudo rm /etc/network/if-up.d/torpinger', shell=True)
    elif arg.auto:
        subprocess.call(
                'sudo cp {}/zetproxy /etc/network/if-up.d/'
                .format(DIR_PATH),shell=True)
        subprocess.call(
                'sudo cp {}/torpinger /etc/network/if-up.d/'
                .format(DIR_PATH),shell=True)
    elif arg.update:
        print('Updating ProxyHelper.')
        subprocess.call(['sh',
                        '{}/update.sh'.format(DIR_PATH)])
    else:
        print('Type "phelp -h" to get description of all features of phelp"')
        subprocess.call(['bash',
                        '{}/zetproxy'.format(DIR_PATH)])

