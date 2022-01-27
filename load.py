import os
import json

def load (foldername) :
  jdata = {}
  for filenames in os.listdir(f'{foldername}'):
    with open ( f'{foldername}/{filenames}' , 'r') as jfile:
        print (jfile)
        jdata_unit = json.load(jfile)
        jdata.update(jdata_unit)
  return (jdata)

if __name__ == "__main__":
    print (load(input()))