# import urllib2
import urllib.request


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
#        response = urllib2.urlopen(url)
        response = urllib.request.urlopen(url)

        if response.getcode() != 200:
            return None
        return response.read()
