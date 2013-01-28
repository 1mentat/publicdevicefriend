import dns.resolver
from urlparse import urlparse
import fileinput

def getabuseu(url):
    o = urlparse(url)
    answers = dns.resolver.query(o.hostname, 'A')
    for response in answers:
        print getabuse(response.address)

def getabuse(ip):
    emails = []
    parts = ip.split(".")

    hostformat = "{}.{}.{}.{}.abuse-contacts.abusix.org".format(parts[3],parts[2],parts[1],parts[0])

    print "Looking up {}".format(hostformat)

    answers = dns.resolver.query(hostformat, 'TXT')

    for response in answers:
        emails.append(response.strings)

    return emails

if __name__ == "__main__":
    for line in fileinput.input():
        getabuseu(line)
