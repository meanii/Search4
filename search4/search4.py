#!/usr/bin/env python3
from datetime import datetime

import argparse
import requests
import colorama
from colorama import Style
from colorama import Fore as Color

colorama.init()

def main():
    start_time = datetime.now()
    requests.packages.urllib3.disable_warnings()

    def banner():
        print(
            Style.BRIGHT
            + Color.MAGENTA
            + """
            

          _/_/_/                                          _/        _/  _/
       _/          _/_/      _/_/_/  _/  _/_/    _/_/_/  _/_/_/    _/  _/
        _/_/    _/_/_/_/  _/    _/  _/_/      _/        _/    _/  _/_/_/_/
           _/  _/        _/    _/  _/        _/        _/    _/      _/
    _/_/_/      _/_/_/    _/_/_/  _/          _/_/_/  _/    _/      _/


        > version 1.0
        > Script to find user account on various platforms.
""" + Style.RESET_ALL)

    # os.system("clear")
    banner()

    parser = argparse.ArgumentParser(description="Search user on different sites.")
    parser.add_argument("-u", "--username", help="Search for the given username.")

    args = parser.parse_args()

    if args.username:
        username = args.username
        print(
            Style.BRIGHT
            + Color.BLUE
            + "Given username is {}\n\n".format(
                Color.RED + Color.UNDER + username + Style.RESET_ALL
            )
            + Color.END
        )
    else:
        print(Color.BLUE + "usage : search4 -u username" + Style.RESET_ALL)
        quit()

    def result(url, site, username_):
        address = url + username_
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:62.0) Gecko/20100101 Firefox/62.0"
            }
            r = requests.get(
                address, headers=headers, verify=False, allow_redirects=False
            )
            if r.status_code == 200:
                print(
                    Style.BRIGHT
                    + Color.YELLOW
                    + "> {}: Account found on {}\n".format(site, address)
                    + Style.RESET_ALL
                )
            else:
                print(
                    Style.BRIGHT
                    + Color.GREEN
                    + "[!] {} : Account not found on {}\n".format(site, address)
                    + Style.RESET_ALL
                )
        except requests.RequestException:
            print(
                Style.BRIGHT
                + Color.GREEN
                + "[!] {} : Account not found on {}\n".format(site, address)
                + Style.RESET_ALL
            )

    print(
        Style.BRIGHT
        + Color.RED
        + "___________________________________________________________________________"
        + Style.RESET_ALL
    )

    print(Style.BRIGHT + Color.WHITE + Color.UNDER + "\n\nSocial sites:\n" + Style.RESET_ALL)
    # noinspection PyUnboundLocalVariable
    result("https://www.facebook.com/", "facebook", username)
    result("https://twitter.com/", "Twitter", username)
    result("https://plus.google.com/+", "Google+", username.lower())
    result("https://m.vk.com/", "VK", username)
    result("https://myanimelist.net/profile/", "MyAnimeList", username)

    print(Style.BRIGHT + Color.RED + "\n" + ":" * 75 + "\n\n" + Style.RESET_ALL)

    print(Style.BRIGHT + Color.WHITE + Color.UNDER + "Video platforms:\n" + Style.RESET_ALL)
    result("https://www.youtube.com/c/", "YouTube", username)
    result("https://vimeo.com/", "Vimeo", username)
    result("https://www.dailymotion.com/", "Dailymotion", username)
    result("https://m.twitch.tv/", "Twitch", username)
    result("https://steamcommunity.com/id/", "steam", username)

    print(Style.BRIGHT + Color.RED + "\n" + ":" * 75 + "\n\n" + Style.RESET_ALL)

    print(Style.BRIGHT + Color.WHITE + Color.UNDER + "Photo platforms:\n" + Style.RESET_ALL)
    result("https://www.instagram.com/", "Instagram", username + "/")
    # result("https://www.pinterest.com/", "Pinterest", username)
    result("https://flickr.com/photos/", "Flickr", username.lower())
    result("https://", "Tumblr", username.lower() + ".tumblr.com")
    result("https://imgur.com/user/", "Imgur", username)
    result("https://vsco.co/", "VSCO", username + "/images/1")

    print(Style.BRIGHT + Color.RED + "\n" + ":" * 75 + "\n\n" + Style.RESET_ALL)

    print(Style.BRIGHT + Color.WHITE + Color.UNDER + "Blogs and forums:\n" + Style.RESET_ALL)
    result("https://", "Blogger", username + ".blogspot.com")
    result("https://medium.com/@", "Medium", username)
    result("https://myspace.com/", "Myspace", username.lower())
    result("https://www.reddit.com/user/", "Reddit", username)
    result("https://www.quora.com/profile/", "Quora", username)

    print(Style.BRIGHT + Color.RED + "\n" + ":" * 75 + "\n\n" + Style.RESET_ALL)

    print(
        Style.BRIGHT + Color.WHITE + Color.UNDER + "Professional platform:\n" + Style.RESET_ALL
    )
    result("https://github.com/", "Github", username)
    result("https://sourceforge.net/u/", "Sourceforge", username)
    result("https://repl.it/@", "Repl.it", username)
    result("https://", "Slack", username + ".slack.com")
    result("https://codepen.io/", "CodePen", username)
    result("https://hackerone.com/", "Hackerone", username.lower())
    result("https://BugCrowd.com/", "BugCrowd", username)
    result("https://about.me/", "about me ", username.lower())
    result("https://www.patreon.com/", "Patreon", username)

    print(Style.BRIGHT + Color.RED + "\n" + ":" * 75 + "\n\n" + Style.RESET_ALL)

    print(Style.BRIGHT + Color.WHITE + Color.UNDER + "Others:\n" + Style.RESET_ALL)
    result("https://www.wikipedia.org/wiki/User:", "Wikipedia", username)
    result("https://buzzfeed.com/", "Buzzfeed", username)
    result("https://open.spotify.com/user/", "Spotify", username)
    result("https://soundcloud.com/", "SoundCloud", username)
    result("https://www.crunchyroll.com/user/", "Crunchyroll", username)

    print(Style.BRIGHT + Color.RED + "_" * 75 + Style.RESET_ALL)

    completetime = datetime.now() - start_time
    print(
        Style.BRIGHT
        + Color.BLUE
        + "\n\nExecution Time : {}\n".format(completetime)
        + Color.END
    )
    print(Style.BRIGHT + Color.WHITE + "DONE...! \n" + Style.RESET_ALL)
