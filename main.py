import feedparser
import hashlib
import string
import random
import matplotlib.pyplot as plt

PRECISION = 1000000000000

def NYTPolitical():
#    url = "http://onlineathens.com/taxonomy/term/4691/2/feed"
    url = "http://rss.nytimes.com/services/xml/rss/nyt/Politics.xml"
    feed = feedparser.parse(url)
    for item in feed["items"]:
        yield item["title"]

def hash(string):
    return (float(int(hashlib.sha512(string.encode('ascii', 'ignore')).hexdigest(), 16))%PRECISION)/PRECISION

def plot_autocorrelate(arr):
    plt.xticks([])
    plt.yticks([])
    plt.acorr(arr, normed=True, color='black', lw=35, linestyle='-.')
    plt.show()

political = []
for headline in NYTPolitical():
    political.append(hash(headline))
plot_autocorrelate(political)
