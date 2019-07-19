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


def run_thread(url, site, user_name):
    temp = Template(url)
    result(temp.render(username=user_name), site)


def main():
    with open(realpath(__file__)[:-10] + 'search4.yml') as yaml_in:
        try:
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
        print(
            Style.BRIGHT
            + Color.BLUE
            + "Given username is {}\n\n".format(
                Color.RED + args.username + Style.RESET_ALL
            )
            + Style.RESET_ALL
        )
    else:
        print(Color.BLUE + "usage : search4 -u username" + Style.RESET_ALL)
        exit(1)
    delim = ''.join(['_' for _ in range(80)])
    print(
        Style.BRIGHT
        + Color.RED
        + delim
        + Style.RESET_ALL)

    for group, data in link_data.items():
        print(
            Style.BRIGHT
            + Color.WHITE
            + "\n\n%s sites:\n" % group
            + Style.RESET_ALL)
        threads = []
        for site, url in data.items():
            t = Thread(target=run_thread, args=[url, site, args.username])
            t.start()
            threads.append(t)
        [th.join() for th in threads]
        print(
            Style.BRIGHT
            + Color.RED
            + "\n" + ":" * 75
            + "\n\n" + Style.RESET_ALL)

    completetime = datetime.now() - start_time
    print(
        Style.BRIGHT
        + Color.BLUE
        + "\n\nExecution Time : {}\n".format(completetime)
        + Style.RESET_ALL
    )
    print(Style.BRIGHT + Color.WHITE + "DONE...! \n" + Style.RESET_ALL)
