### Subdomainix - Python Subdomain Scanner

    Usage:
    
    Subdomainix:
        subdomainix.py [-h] -t Target Domain [-w Single Word]
                       [-wp Wordlist Path]
    
    URLWorker Module:
        Usage:
        For URL Status:
            object = urlworker.URLWorker(url)
            _true = object.url_online()
        For Checking Subdomains:
            object = urlworker.URLWorker(url, worlist=(), wordlist_path="")
            valid_urls = object.check_subd()

+ Author: PiereLucas(Julian Huch)
+ MIT License