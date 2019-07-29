from requests import get, RequestException
from re import search
from colorama import Style
from colorama import Fore as Color


def found(name, addr):
    msg = "> {}: Account found on {}\n".format(name, addr)
    print(Style.BRIGHT + Color.YELLOW + msg + Style.RESET_ALL)


def not_found(name, addr):
    msg = "[!] {} : Account not found on {}\n".format(name, addr)
    print(Style.BRIGHT + Color.GREEN + msg + Style.RESET_ALL)


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
        """
        + Style.RESET_ALL
    )


def search_regex(regex, phrase):
    match = search(regex, phrase)
    if match:
        return match.group(1)
    return None


# Scrape more problem pages here to ensure 200 ok.
# Hopefully <title> tag contents can be used on
# any future sites with issues.
def check_200_ok(html, url, site_name):
    if site_name not in ("steam", "pastebin"):
        return True
    regex_out = r"<title>(.*)</title>"
    title_tag = search_regex(regex_out, html)
    # check Steam
    if 'steam' in url and 'Error' in title_tag:
        return False
    # check pastebin
    elif 'pastebin' in url and '#1 paste tool since 2002' in title_tag:
        return False
    return True


def result(address, site):
    try:
        agent = "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:62.0) "
        agent += "Gecko/20100101 Firefox/62.0"
        headers = {"User-Agent": agent}
        r = get(address, headers=headers)
        if r.status_code != 200:
            not_found(site, address)
        else:
            if not check_200_ok(r.text, address, site.lower()):
                not_found(site, address)
            else:
                found(site, address)
    except RequestException:
        not_found(site, address)
