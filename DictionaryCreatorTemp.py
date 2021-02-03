import xml.etree.ElementTree as ET
import re

regex_str = [
    r'<[^>]+>',  # HTML tags
    r'(?:@[\w_]+)',  # @-mentions
    r"(?:\#+[\w_]+[\w\'\-]*[\w]+)",  # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',  # URLs
    r'\".+?\"',  # string in double quotes
    r'\$\d+(?:\.\d+)?',  # dollar amount
    r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers
    r"(?:[\u0590-\u05fe][\u0590-\u05fe'\-_]+[\u0590-\u05fe])",  # words with - and '
    r'(?:[\w_]+)',  # other words
    r'(?:\S)',  # anything else
]

tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)


def tokenize(s):
    s = re.sub(r'[^\x00-\x7f]*',r'',s)
    s = re.sub(r'<[^>]+>',r'',s)   #removed HTML tags
    return tokens_re.findall(s)


def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens


lawPath = 'main.xml'

lawTree = ET.parse(lawPath)
lawRoot = lawTree.getroot()

lawContent = lawRoot.findall('.//{http://docs.oasis-open.org/legaldocml/ns/akn/3.0}p')
lawContent = [content.text for content in lawContent]
for content in lawContent:
    print(content)
