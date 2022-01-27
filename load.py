import os
import json

def load () :
  jdata = {}
  for filenames in os.listdir('text'):
    with open ( f'text/{filenames}' , 'r') as jfile:
        print (jfile)
        jdata_unit = json.load(jfile)
        jdata.update(jdata_unit)
  return (jdata)

if __name__ == "__main__":
    print (load())