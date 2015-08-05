import sys
from contextlib import closing
import requests


def main():
    
    chan = sys.argv[1]
    url = "https://streamboat.tv/sub/{}".format(chan)
    print "Subscribing to {} ..".format(chan)
    with closing(requests.get(url, stream=True)) as r:
        for msg in r.iter_lines():
            print msg


if __name__ == '__main__':
    main()