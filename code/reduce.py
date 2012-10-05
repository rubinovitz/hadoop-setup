import sys
counts={}
for lineIn in sys.stdin:
#       Note: We separate the key here
    try:
       key, line = lineIn.rsplit('\t',1)
       aLine = line.split(',')
       counts[key] = counts.get(key,0) + int(aLine[3])
    except:
        pass
for k , v in counts.items():
      print k + ',' +str(v)
