# Author: PiereLucas(Julian Huch)


import sys
from argparse import ArgumentParser
from urlworker import URLWorker


class Parser():
    """
    Parser Class to deal with the given cli args
    """

    def __init__(self):
        parser = ArgumentParser(description="Subdomainix - Subdomain Scanner")
        parser.add_argument("-t", "--target", dest="target", required=True, metavar="Target Domain", help="The Target Domain [google.com]")
        parser.add_argument("-w", "--word", dest="wordlist", required=False, metavar="Single Word", help="Single subdomain search")
        parser.add_argument("-wp", "--wordlist-path", dest="wordlist_path", required=False, metavar="Wordlist Path", help="Give a Wordlist")
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
    """
    Controller Class for run whole program and give arguments to the URLWorker
    """

    def __init__(self):
        Parser.__init__(self)
        URLWorker.__init__(self, url=self.target, wordlist=self.wordlist, wordlist_path=self.wordlist_path)

    def run(self):
        """ Run function """

        print(f"[+] Subdomainix - Subdomain Scanner\n[+] Scanning: [{self.target}]")
        valid_url_list = self.check_subd()
        if valid_url_list == []:
            print(f"[-] No Subdomains found")
        for url in valid_url_list:
            print(f"[+] Found Subdomain: [{url}]")
        sys.exit(0)


if __name__ == "__main__":
    cc = Controller()
    cc.run()
