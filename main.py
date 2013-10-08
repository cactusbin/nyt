import feedparser
import hashlib
import string
import random
import matplotlib.pyplot as plt

PRECISION = 1000000000000

def NYTPoliticalFeed():
    url = "http://rss.nytimes.com/services/xml/rss/nyt/Politics.xml"
    feed = feedparser.parse(url)
    for item in feed["items"]:
        yield item["title"]

def hash(string):
    return (float(int(hashlib.sha512(string.encode('ascii', 'ignore')).hexdigest(), 16))%PRECISION)/PRECISION

def plot_lines(arr):
    plt.xticks([])
    plt.yticks([])
    plt.vlines(arr, 0, 1, linestyle='-.')
    plt.show()

political = []
for headline in NYTPoliticalFeed():
    political.append(hash(headline))
plot_lines(political)
