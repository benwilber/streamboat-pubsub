import sys
import requests


def main():

    chan, msg = sys.argv[1], sys.argv[2]
    url = "https://streamboat.tv/pub/{}".format(chan)
    r = requests.post(url, data=msg, headers={'Authorization': "Token 12345"})
    r.raise_for_status()
    print r.json()


if __name__ == '__main__':
    main()