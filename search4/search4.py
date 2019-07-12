#!/usr/bin/env python3
from datetime import datetime

import argparse
import colorama
from colorama import Style
from colorama import Fore as Color

from search4.utils import banner, result


def main():
    colorama.init()

    start_time = datetime.now()

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
                Color.RED + username + Style.RESET_ALL
            )
            + Style.RESET_ALL
        )
    else:
        print(Color.BLUE + "usage : search4 -u username" + Style.RESET_ALL)
        quit()

    print(
        Style.BRIGHT
        + Color.RED
        + "___________________________________________________________________________"
        + Style.RESET_ALL
    )

    print(Style.BRIGHT + Color.WHITE + "\n\nSocial sites:\n" + Style.RESET_ALL)

    # noinspection PyUnboundLocalVariable
    result("https://www.facebook.com/", "facebook", username)
    result("https://twitter.com/", "Twitter", username)
    result("https://plus.google.com/+", "Google+", username.lower())
    result("https://m.vk.com/", "VK", username)
    result("https://myanimelist.net/profile/", "MyAnimeList", username)

    print(Style.BRIGHT + Color.RED + "\n" + ":" * 75 + "\n\n" + Style.RESET_ALL)

    print(Style.BRIGHT + Color.WHITE + "Video platforms:\n" + Style.RESET_ALL)
    result("https://www.youtube.com/c/", "YouTube", username)
    result("https://vimeo.com/", "Vimeo", username)
    result("https://www.dailymotion.com/", "Dailymotion", username)
    result("https://m.twitch.tv/", "Twitch", username)
    result("https://steamcommunity.com/id/", "steam", username)

    print(Style.BRIGHT + Color.RED + "\n" + ":" * 75 + "\n\n" + Style.RESET_ALL)

    print(Style.BRIGHT + Color.WHITE + "Photo platforms:\n" + Style.RESET_ALL)
    result("https://www.instagram.com/", "Instagram", username + "/")
    # result("https://www.pinterest.com/", "Pinterest", username)
    result("https://flickr.com/photos/", "Flickr", username.lower())
    result("https://", "Tumblr", username.lower() + ".tumblr.com")
    result("https://imgur.com/user/", "Imgur", username)
    result("https://vsco.co/", "VSCO", username + "/images/1")

    print(Style.BRIGHT + Color.RED + "\n" + ":" * 75 + "\n\n" + Style.RESET_ALL)

    print(Style.BRIGHT + Color.WHITE + "Blogs and forums:\n" + Style.RESET_ALL)
    result("https://", "Blogger", username + ".blogspot.com")
    result("https://medium.com/@", "Medium", username)
    result("https://myspace.com/", "Myspace", username.lower())
    result("https://www.reddit.com/user/", "Reddit", username)
    result("https://www.quora.com/profile/", "Quora", username)

    print(Style.BRIGHT + Color.RED + "\n" + ":" * 75 + "\n\n" + Style.RESET_ALL)

    print(
        Style.BRIGHT + Color.WHITE + "Professional platform:\n" + Style.RESET_ALL
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

    print(Style.BRIGHT + Color.WHITE + "Others:\n" + Style.RESET_ALL)
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
        + Style.RESET_ALL
    )
    print(Style.BRIGHT + Color.WHITE + "DONE...! \n" + Style.RESET_ALL)
