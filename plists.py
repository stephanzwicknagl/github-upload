import json
import os
import sys
#reload(sys)
#  sys.setdefaultencoding('utf8')
"""Hier den Dateipfad der .json-Datei angeben, die von google heruntergeladen wurde. in your_file.txt wird die Tracklist ausgegeben"""
with open(os.path.join(sys.path[0], "winter19-20.json")   , "r") as read_file:
    data = json.load(read_file)

def extract_values(obj, key):
    """Pull all values of specified key from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    results = extract(obj, arr, key)
    return results

type(data)

songlist=extract_values(data, "title")
print(songlist)
#for item in songlist:
#    item = item.encode('utf8').strip()

with open('/C:/Users/steph/Documents/Programmieren/Python/Youtubeplaylists/your_file.txt', 'w') as f:
    i=1
    for item in songlist:
        f.write("%s %s\n" % (i , item))
        i=i+1
