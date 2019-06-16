
import requests
response = requests.get('http://hiscore.runescape.com/index_lite.ws?player=zezima')
print (response.status_code)
print (response.content)