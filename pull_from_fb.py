import facebook
import json
import requests
import urllib3

URL = ""
TOKEN = "EAAlBkubFQxQBANLptT37WKN63V9zj5Cf6zHaHKzVpZC1QTe1hU1Ve4r2cVPCdaRZCZCXskj90wMsnCqqhZBysSZAzuhgC3mkcWdNY2oPkSjC8voAgLpzaVRUJmFc63E3cRF970uMWpW0nhZBDAXV6ZBfTAdDF0zUJbgmskgHPEJ9ZCURfG1iGWySiJjta62dal91wsus2CdSuiA3EuV3GbZAyVLLL7AounT6fpjV6E4AZAswZDZD"
VERSION = "3.1"

graph = facebook.GraphAPI(access_token = TOKEN, version=VERSION)
photo = graph.get_object(id = '591008984407948')
print(photo)
