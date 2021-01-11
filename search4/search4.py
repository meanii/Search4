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
    ft = "Execution Time : {}\n".format(t)
    print(Color.BLUE + ft + Style.RESET_ALL)


def print_username(user):
    print(
        Color.RED
        + "> {}\n".format(
            Color.BLUE + user + Style.RESET_ALL)
        + Style.RESET_ALL)


def print_usage():
    print(Color.BLUE + "usage : search4 -u username\n" + Style.RESET_ALL)


def print_title(grp):
    title = "\n%s sites:\n" % grp
    print(Color.WHITE + title + Style.RESET_ALL)


def run_thread(url, site, user_name):
    temp = Template(url)
    result(temp.render(username=user_name), site)


def parse_yaml():
    try:
        with open(realpath(__file__)[:-10] + 'search4.yml') as yaml_in:
            link_data = safe_load(yaml_in)
    except Exception as e:
        print(type(e).__name__, e)
        exit(1)
    else:
        return link_data


def parse_args():
    parser = ArgumentParser(description="Search user on different sites.")
    parser.add_argument(
        "-u", "--username", help="Search for the given username.")
    args = parser.parse_args()
    if args.username:
        return args.username
    return None


def main():
    link_data = parse_yaml()
    colorama.init()
    start_time = datetime.now()
    banner()
    user_name = parse_args()
    if not user_name:
        print_usage()
        exit(1)
    print_username(user_name)

    for group, data in link_data.items():
        threads = []
        for site, url in data.items():
            t = Thread(target=run_thread, args=[url, site, user_name])
            t.start()
            threads.append(t)
        [th.join() for th in threads]

    complete_time = datetime.now() - start_time
    print_exec_time(complete_time)
