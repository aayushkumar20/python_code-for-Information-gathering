import urllib.request 
import io
def GetRobots(url): 
  if url.endswith("/"): 
    path = url
  else: 
    path = url + "/"
    requestingData = urllib.request.urlopen(path + "robots.txt", data=None)
    data = io.TextIOWrapper(requestingData, encoding="utf 8") 
    return data.read()
print(GetRobots("****Enter your URL here***"))
