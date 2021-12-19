# I nearly didn't even try this one, because the 3D
# coordinate system isn't something that works well
# with my brain.  But I gave it a shot, and it works
# for the trivial case, but not the more complex
# cases.  There's an adjustment back to known
# coordinates that isn't working, but I'm really 
# not interested in debugging it.

import sys
from collections import Counter

def align_beacons(known, scanner):
    # try the beacons in scanner with every
    # possible rotation and measure distances
    # between them and known beacons
    # trying to find 12 matching distances
    distances = {}
    
    for x in (0, 1, 2):
        for xsign in (-1, 1):
            for y in (0, 1, 2):
                for ysign in (-1, 1):
                    for z in (0, 1, 2):
                        for zsign in (-1, 1):
                            if x == y or y == z or z == x:
                                continue
                            
                            distances[(x, xsign, y, ysign, z, zsign)] = Counter()
                            for beacon in scanner:
                                for b1 in known:
                                    distance = (beacon[x]*xsign-b1[0], beacon[y]*ysign-b1[1], beacon[z]*zsign-b1[2])
                                
                                    distances[(x, xsign, y, ysign, z, zsign)][distance] += 1
    #print(distances)
    for distance in distances:
        for dist in distances[distance]:
            if distances[distance][dist] >= 12:
                # Adjust the beacon locations to match the known coordinates
                for beacon in scanner:
                    #print('Before', beacon, distance, dist)
                    beacon[0] = beacon[distance[0]]*distance[1]-dist[0]
                    beacon[1] = beacon[distance[2]]*distance[3]-dist[1]
                    beacon[2] = beacon[distance[4]]*distance[5]-dist[2]
                    #print('After', beacon, distance, dist)
                    
                    if beacon not in known:
                        known.append(beacon)
                    
                return True
            
    return False

scanners = []

for line in sys.stdin:
    line = line.rstrip()
    
    if line == '-1':
        scanners.append(scanner)
        break
    
    if 'scanner' in line:
        scanner = []
    elif line:
        scanner.append([int(r) for r in line.split(',')])
    else:
        scanners.append(scanner)
    
known = scanners[0].copy()
unknown = scanners[1:]

while unknown:
    # check the beacons for each scanner
    # to align them with at least 12 known beacons
    # if so, remove them from unknown
    
    for scanner in unknown:
        if align_beacons(known, scanner):
            unknown.remove(scanner)
            break

print(len(known))
