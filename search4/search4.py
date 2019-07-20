#!/usr/bin/env python3
import colorama
from argparse import ArgumentParser
from datetime import datetime
from colorama import Style
from colorama import Fore as Color
from threading import Thread
from yaml import safe_load
from jinja2 import Template
from sys import exit
from os.path import realpath
from search4.utils import banner, result


def print_exec_time(t):
    ft = "\n\nExecution Time : {}\n".format(t)
    print(Style.BRIGHT + Color.BLUE + ft + Style.RESET_ALL)


def print_username(user):
    print(
        Style.BRIGHT
        + Color.BLUE
        + "Given username is {}\n\n".format(
            Color.RED + user + Style.RESET_ALL)
        + Style.RESET_ALL)


def print_usage():
    print(Color.BLUE + "usage : search4 -u username" + Style.RESET_ALL)


def print_finish():
    print(Style.BRIGHT + Color.WHITE + "DONE...! \n" + Style.RESET_ALL)


def print_banner():
    p = "\n" + ":" * 75 + "\n\n"
    print(Style.BRIGHT + Color.RED + p + Style.RESET_ALL)


def print_delimiter():
    delim = ''.join(['_' for _ in range(80)])
    print(Style.BRIGHT + Color.RED + delim + Style.RESET_ALL)


def print_title(grp):
    title = "\n\n%s sites:\n" % grp
    print(Style.BRIGHT + Color.WHITE + title + Style.RESET_ALL)


def run_thread(url, site, user_name):
    temp = Template(url)
    result(temp.render(username=user_name), site)


def main():
    try:
        with open(realpath(__file__)[:-10] + 'search4.yml') as yaml_in:
            link_data = safe_load(yaml_in)
    except Exception as e:
        print(type(e).__name__, e)
        exit(1)
    colorama.init()
    start_time = datetime.now()
    banner()
    parser = ArgumentParser(description="Search user on different sites.")
    parser.add_argument(
        "-u", "--username", help="Search for the given username.")
    args = parser.parse_args()
    if args.username:
        print_username(args.username)
    else:
        print_usage()
        exit(1)
    print_delimiter()

    # read each group of links from YAML and give each
    # link/request its own thread (join threads per each group)
    for group, data in link_data.items():
        print_title(group)
        threads = []
        for site, url in data.items():
            t = Thread(target=run_thread, args=[url, site, args.username])
            t.start()
            threads.append(t)
        [th.join() for th in threads]
        print_banner()

    complete_time = datetime.now() - start_time
    print_exec_time(complete_time)
    print_finish()
