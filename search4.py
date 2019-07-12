#!/usr/bin/env python3
from datetime import datetime

import argparse
import os
import requests

startTime = datetime.now()
requests.packages.urllib3.disable_warnings()


class Color:
    BLUE = '\033[94m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    WHITE = '\033[0;37m'
    MAGENTA = '\033[0;35m'
    UNDER = '\033[04m'
    BOLD = '\033[1m'
    END = '\033[0m'


def banner():
    print(Color.BOLD + Color.MAGENTA + """
            

          _/_/_/                                          _/        _/  _/
       _/          _/_/      _/_/_/  _/  _/_/    _/_/_/  _/_/_/    _/  _/
        _/_/    _/_/_/_/  _/    _/  _/_/      _/        _/    _/  _/_/_/_/
           _/  _/        _/    _/  _/        _/        _/    _/      _/
    _/_/_/      _/_/_/    _/_/_/  _/          _/_/_/  _/    _/      _/


        > version 1.0
        > Script to find user account on various platforms.
""" + Color.END)


os.system("clear")
banner()

parser = argparse.ArgumentParser(description='Search user on different sites.')
parser.add_argument('-u', '--username', help='Search for the given username.')

args = parser.parse_args()

if args.username:
    username = args.username
    print(Color.BOLD + Color.BLUE + "Given username is {}\n\n".format(
        Color.RED + Color.UNDER + username + Color.END) + Color.END)
else:
    print(Color.BLUE + "usage : search4 -u username" + Color.END)
    quit()


def result(url, site, username_):
    address = (url + username_)
    try:
        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:62.0) Gecko/20100101 Firefox/62.0"}
        r = requests.get(address, headers=headers, verify=False, allow_redirects=False)
        if r.status_code == 200:
            print(Color.BOLD + Color.YELLOW + "> {}: Account found on {}\n".format(site, address) + Color.END)
        else:
            print(Color.BOLD + Color.GREEN + "[!] {} : Account not found on {}\n".format(site, address) + Color.END)
    except requests.RequestException:
        print(Color.BOLD + Color.GREEN + "[!] {} : Account not found on {}\n".format(site, address) + Color.END)


print(
    Color.BOLD + Color.RED + "___________________________________________________________________________" + Color.END)

print(Color.BOLD + Color.WHITE + Color.UNDER + "\n\nSocial sites:\n" + Color.END)
# noinspection PyUnboundLocalVariable
result("https://www.facebook.com/", "facebook", username)
result("https://twitter.com/", "Twitter", username)
result("https://plus.google.com/+", "Google+", username.lower())
result("https://m.vk.com/", "VK", username)
result("https://myanimelist.net/profile/", "MyAnimeList", username)

print(Color.BOLD + Color.RED + "\n" + ":" * 75 + "\n\n" + Color.END)

print(Color.BOLD + Color.WHITE + Color.UNDER + "Video platforms:\n" + Color.END)
result("https://www.youtube.com/c/", "YouTube", username)
result("https://vimeo.com/", "Vimeo", username)
result("https://www.dailymotion.com/", "Dailymotion", username)
result("https://m.twitch.tv/", "Twitch", username)
result("https://steamcommunity.com/id/", "steam", username)

print(Color.BOLD + Color.RED + "\n" + ":" * 75 + "\n\n" + Color.END)

print(Color.BOLD + Color.WHITE + Color.UNDER + "Photo platforms:\n" + Color.END)
result("https://www.instagram.com/", "Instagram", username + "/")
# result("https://www.pinterest.com/", "Pinterest", username)
result("https://flickr.com/photos/", "Flickr", username.lower())
result("https://", "Tumblr", username.lower() + ".tumblr.com")
result("https://imgur.com/user/", "Imgur", username)
result("https://vsco.co/", "VSCO", username + '/images/1')

print(Color.BOLD + Color.RED + "\n" + ":" * 75 + "\n\n" + Color.END)

print(Color.BOLD + Color.WHITE + Color.UNDER + "Blogs and forums:\n" + Color.END)
result("https://", "Blogger", username + ".blogspot.com")
result("https://medium.com/@", "Medium", username)
result("https://myspace.com/", "Myspace", username.lower())
result("https://www.reddit.com/user/", "Reddit", username)
result("https://www.quora.com/profile/", "Quora", username)

print(Color.BOLD + Color.RED + "\n" + ":" * 75 + "\n\n" + Color.END)

print(Color.BOLD + Color.WHITE + Color.UNDER + "Professional platform:\n" + Color.END)
result("https://github.com/", "Github", username)
result("https://sourceforge.net/u/", "Sourceforge", username)
result("https://repl.it/@", "Repl.it", username)
result("https://", "Slack", username + ".slack.com")
result("https://codepen.io/", "CodePen", username)
result("https://hackerone.com/", "Hackerone", username.lower())
result("https://BugCrowd.com/", "BugCrowd", username)
result("https://about.me/", "about me ", username.lower())
result("https://www.patreon.com/", "Patreon", username)

print(Color.BOLD + Color.RED + "\n" + ":" * 75 + "\n\n" + Color.END)

print(Color.BOLD + Color.WHITE + Color.UNDER + "Others:\n" + Color.END)
result("https://www.wikipedia.org/wiki/User:", "Wikipedia", username)
result("https://buzzfeed.com/", "Buzzfeed", username)
result("https://open.spotify.com/user/", "Spotify", username)
result("https://soundcloud.com/", "SoundCloud", username)
result("https://www.crunchyroll.com/user/", "Crunchyroll", username)

print(
    Color.BOLD + Color.RED + "_" * 75 + Color.END)

completetime = datetime.now() - startTime
print(Color.BOLD + Color.BLUE + "\n\nExecution Time : {}\n".format(completetime) + Color.END)
print(Color.BOLD + Color.WHITE + "DONE...! \n" + Color.END)
