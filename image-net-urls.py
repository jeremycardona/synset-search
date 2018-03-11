# Search for images in image-net.org and get the synset id of the image
import json 
import re
import requests
from bs4 import BeautifulSoup
import urllib.request

class SynsetSearch:
    'search for synset url of images, input the keyword to search for in the api. Returns a list of urls for the keyword'
    synset = []
    synsetDict = {}
    def __init__(self):
        pass

    def addKeyword(self, keyword):
        pass
        
    def getUrl(self, keyword):
        pass
        
    def getKeywordIds(self, keyword):
        wordsFile  = urllib.request.urlopen("http://image-net.org/archive/words.txt")
        for line in wordsFile:
            temp = line.decode("utf-8")
            if keyword + "," in temp:
                self.synset.append(temp)
        return self.synset
        
    def getDict(self):
        rows = ( line.split("\t") for line in self.synset )
        self.synsetDict = { row[0]:row[1:] for row in rows }
        return self.synsetDict
        
                
    def getUrls(self, synsetId):
        urlFile = urllib.request.urlopen("http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=" + synsetId)
        soup = BeautifulSoup(urlFile, "html.parser" ).decode('UTF-8')
        urlList = soup.split()
        return urlList

#initialize images
images = SynsetSearch()

#returns a list of all the ids that has the dog keyword
dogId = images.getKeywordIds("dog")
#returns a dictionary of id, values 
dogDict = images.getDict()

#get list of keys with dogDict.keys()
#print(list(dogDict.keys())[0]) this returns the first key in the dictionary
dogUrls = images.getUrls(list(dogDict.keys())[0])
print(dogUrls)

