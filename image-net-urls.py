# Search for images in image-net.org and get the synset id of the image
import json 
import re
import requests
import urllib

class SynsetSearch:
    'search for synset url of images, input the keyword to search for in the api. Returns a list of urls for the keyword'
    
    synset = [] # list of synsets 
    synsetDict = {
        "keyword": {
            "_id": int,
            "_value": str
        },
        "keyword2": {
            "_id": int,
            "_value": str
        }
    } # synset dictionary of id and name
    
    
    def __init__(self, keyword):
        self.synset.append(keyword)

    def addKeyword(self, keyword):
        self.synset.append(keyword)

    def getUrl(self, keyword):
        url = "http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=" + self.synsetDict.keyword._id
        return url

    def searchKeywords(self, keyword):
        wordsFile  = urllib.urlopen("http://image-net.org/archive/words.txt") # search query using keyword
        for line in wordsFile:
            k = line.slit('\t')
            v = 

        return 
        
    
    #def getUrls(self, synsetId):

#initialize images
images = SynsetSearch("dog")

images.addKeyword("cat")

images.getUrl("dog")



#print(Cars.query("car"))
#link = "http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02472987"
#f = urllib.urlopen(link)
#myfile = f.read()
#print myfile