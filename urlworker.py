# Author: PiereLucas(Julian Huch)


"""
URLWorker Module:
    Usage:
        For URL Status:
            object = urlworker.URLWorker(url)
            _true = object.url_online()
        For Checking Subdomains:
            object = urlworker.URLWorker(url, worlist=(), wordlist_path="")
            valid_urls = object.check_subd()
"""


import sys
import requests
from collections import deque


class URLWorkerException():
    pass


class URLWorker():

    def __init__(self, url, *, wordlist=(), wordlist_path=""):
        self.url = url
        self.valid_urls = []
        self.wordlist = wordlist
        self.wordlist_path = wordlist_path

    def check_subd(self):

        self.worlist_creator()
        self.check_domains()
        return self.valid_urls

    def url_online(self):

        try:

            url = requests.get(self.url)
            status = url.status_code
            if status < 300: return True
            else: return False

        except Exception as ex:
            print("Error in function 'url_online' :", ex)

    def worlist_creator(self):

        try:

            if self.wordlist == () and self.wordlist_path == "":
                print("Required: wordlist and/or wordlist_path argmument")
                raise Exception

            elif self.wordlist == ():
                with open(self.wordlist_path, 'rt') as f:
                    self.wordlist = deque(f.readlines())

            elif self.wordlist_path == "":
                self.wordlist = deque(self.wordlist)

            else:
                with open(self.wordlist_path, 'rt') as f:
                    wlist = f.readlines()
                    self.wordlist = deque([*self.wordlist, *wlist])

            return

        except Exception as ex:
            print(ex)
            sys.exit(1)

    def check_domains(self):

        while self.wordlist != deque([]):
            word = self.wordlist[0]
            self.url = word + self.url
            _true = self.url_online()
            if _true:
                self.valid_urls.append(self.url)
            self.wordlist.popleft()
            continue
        return
