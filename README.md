
A tool to search a particular username on almost every social platform and tell , whether the user with that username exists on that site or not.
<p align="center">
<a href="https://github.com/7rillionaire/Search4">
<img src="https://i.ibb.co/TWvY84p/Pics-Art-12-01-03-29-17-1.png" alt="logo"></a>
</p>


<div align="center">

  [![Status](https://img.shields.io/badge/status-active-success.svg)]()
  <img src="https://img.shields.io/badge/version-1.0-blue.svg">
  <img src="https://img.shields.io/badge/python->=_3.6-green.svg">
  ![GitHub issues](https://img.shields.io/github/issues-raw/7rillionaire/Search4.svg)
  ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/7rillionaire/Search4.svg)
  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> 

   
</p>

## 📝 Table of Contents
- [About](#about)
- [Getting Started](#getting_started)
- [Prerequisites](#prerequisites)
- [Setting-up](#setup)
- [Usage](#usage)
- [TODO](https://github.com/7rillionaire/Search4/blob/master/TODO.md)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

It is a python script using which you can search a username on almost every social media platform. You can see that on how many social media platforms a particular username exists. 

This script works on the response of web servers and searches that username on their web servers on your behalf, in a single execution. It takes it less than a minute to do so.

## 🏁 Getting Started <a name = "getting_started"></a>
These instructions will get you a copy of the project up and running on your local machine for development and usage purposes.

### Prerequisites <a name="prerequisites"></a>
Things needed to run search4.

- python3
- request module

Installing dependencies

- [Install python3 as per your distro.](https://realpython.com/installing-python)

- Now install request module

<code>
pip3 install requests
</code>

### Setting-up <a name="setup"></a>

```
git clone https://github.com/7rillionaire/Search4

cd Search4

chmod +x search4.py

```
We had planned to automate the following & add a feature,  but it seems not possible for now. [See issues#5](https://github.com/7rillionaire/Search4/issues/5)

But then [alias](https://www.geeksforgeeks.org/alias-command-in-linux-with-examples/amp/) can be useful.

```
mv search4.py $HOME

alias search4='python3 search 4.py'

```
[Always make sure while using search4 you are in $HOME](https://github.com/7rillionaire/Search4/issues/5)


#### Installation & Setup done...!


## 🎈 Usage <a name="usage"></a>


Make sure you are in $HOME

```
search4 -u username

# output

         _/_/_/                                          _/        _/  _/
       _/          _/_/      _/_/_/  _/  _/_/    _/_/_/  _/_/_/    _/  _/
        _/_/    _/_/_/_/  _/    _/  _/_/      _/        _/    _/  _/_/_/_/
           _/  _/        _/    _/  _/        _/        _/    _/      _/
    _/_/_/      _/_/_/    _/_/_/  _/          _/_/_/  _/    _/      _/


        > version 1.0
        > Script to find user account on various platforms.

# followed by results

```
 

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

● References :

- [Python requests](https://realpython.com/python-requests/)

- [Writing the Docs](https://github.com/kylelobo/The-Documentation-Compendium)
