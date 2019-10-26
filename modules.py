# Author: PiereLucas(Julian Huch)


"""
Usage:
    For URL Status:
        object = modules.URLWorker(url)
        _true, status = object.url_online()
"""


import os
import sys
import requests


class URLWorkerException():
    pass


class URLWorker():

    def __init__(self, url, *, wordlist="", wordlist_path=""):
        self.url = url
        self.wordlist = wordlist
        self.wordlist_path = wordlist_path

    def worlist_creator(self):

        try:

            if self.wordlist == "" and self.wordlist_path == "":
                print("Required: wordlist and/or wordlist_path argmument")
                raise Exception

            elif self.wordlist == "":
                with open(self.wordlist_path, 'rt') as f:
                    self.wordlist = f.readlines()

            elif self.wordlist_path == "":
                pass

            else:
                with open(self.wordlist_path, 'rt') as f:
                    wlist = f.readlines()
                    self.wordlist = [*self.wordlist, *wlist]

        except Exception as ex:
            print(ex)
            sys.exit(1)

    def check_domains(self):
        pass

    def url_online(self):
        try:

            url = requests.get(self.url)
            status = url.status_code
            if status < 300: return True, status
            else: return False, status

        except Exception as ex:
            print("Error in function 'url_online' :", ex)

