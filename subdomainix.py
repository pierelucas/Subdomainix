# Author: PiereLucas(JUlian Huch)

import os
import sys
from argparse import ArgumentParser
from urlworker import URLWorker


parser = ArgumentParser()
parser.add_argument("-t", "--target", dest="target", required=True, metavar="Target Domain")
parser.add_argument("-w", "--wordlist", dest="wordlist", required=False, metavar="Wordlist")
parser.add_argument("-wp", "--wordlist-path", dest="wordlist_path", required=False, metavar="Wordlist Path")
args = parser.parse_args()


class Parser():

    def __init__(self):

        parser = ArgumentParser(description="Subdomainix - Subdomain Scanner")
        parser.add_argument("-t", "--target", dest="target", required=True, metavar="Target Domain")
        parser.add_argument("-w", "--word", dest="wordlist", required=False, metavar="Single Word")
        parser.add_argument("-wp", "--wordlist-path", dest="wordlist_path", required=False, metavar="Wordlist Path")
        args = parser.parse_args()

        self.target = args.target

        if args.wordlist:
            self.wordlist = args.wordlist
        else:
            self.wordlist = ()

        if args.wordlist_path:
            self.wordlist_path = args.wordlist_path
        else:
            self.wordlist_path = ""


class Controller(Parser, URLWorker):

    def __init__(self):

        Parser.__init__(self)
        URLWorker.__init__(self, url=self.target, wordlist=self.wordlist, wordlist_path=self.wordlist_path)

    def run(self):
        print(f"[+] Scanning: [{self.target}]")
        valid_url_list = self.check_subd()
        if valid_url_list == []:
            print(f"[-] No Subdomains found")
        for url in valid_url_list:
            print(f"[+] Found Subdomain: [{url}]")
        sys.exit(0)


if __name__ == "__main__":
    cc = Controller()
    cc.run()
