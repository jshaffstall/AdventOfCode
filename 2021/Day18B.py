# After how annoying part 1 was, I'm glad
# part 2 was a simple modification

import sys
import math
import copy

class Pair:
    def __init__(self, value=None):
        self.insetup = True
        self.left = 0
        self.right = 0
        self.depth = 0
        self.value = value
        
    def setup(self, item):
        item.depth = self.depth+1
        
        if self.insetup:
            self.left = item
            self.insetup = False
        else:
            self.right = item
    
    @property
    def value(self):
        return self._value
    
    @property
    def left(self):
        return self._left
    
    @property
    def right(self):
        return self._right
    
    @property
    def depth(self):
        return self._depth
    
    @value.setter
    def value(self, item):
        self._value = item
        
    @left.setter
    def left(self, item):
        self._left = item
        
    @right.setter
    def right(self, item):
        self._right = item
        
    @depth.setter
    def depth(self, item):
        self._depth = item
        
    def __str__(self):
        if self.value is not None:
            return f'{self.value}:{self.depth}'
        
        if self.depth > 4:
            return f'[{self.left},{self.right}!{self.depth}]'
        
        if self.depth == 4:
            return f'[{self.left},{self.right}*]'
        
        return f'[{self.left},{self.right}:{self.depth}]'
    
    def __repr__(self):
        return str(self)
    
    def add(self, other):
        pair = Pair()
        pair.left = copy.deepcopy(self)
        pair.left.inc_depth()
        pair.right = copy.deepcopy(other)
        pair.right.inc_depth()
        
        return pair

    def inc_depth(self):
        self.depth += 1
        if self.left:
            self.left.inc_depth()
        if self.right:
            self.right.inc_depth()
            
    def magnitude(self):
        if self.value is not None:
            return self.value
        
        left = 3*self.left.magnitude()
        right = 2*self.right.magnitude()
            
        return left+right

    def split(self):
        if self.value is not None:
            if self.value > 9:
                pair = Pair(self.value//2)
                pair.depth = self.depth+1
                self.left = pair
                pair = Pair(math.ceil(self.value/2))
                pair.depth = self.depth+1
                self.right = pair
                self.value = None
                return True
                
            return False
        
        if self.left.split():
            return True
        
        return self.right.split()

    def explode(self):
        # Saved the most annoying part for last
        # Exploding transmits state information
        # across sibling pairs, so doesn't fit
        # neatly into the data structure, which
        # means ugly code to handle it.
        
        if self.value is not None:
            return False,None,None
        
        if self.depth == 4:
            #print(f'Exploding: {self}')
            self.value = 0
            
            return True,self.left,self.right
        
        result = self.left.explode()
        
        if result[0]:
            if result[2]:
                if self.right.value is not None:
                    self.right.value += result[2].value
                else:
                    self.right.pass_right(result[2].value)
            
            return True,result[1],None
        
        result = self.right.explode()
        
        if result[0]:
            if result[1]:
                if self.left.value is not None:
                    self.left.value += result[1].value
                else:
                    self.left.pass_left(result[1].value)
            
            return True,None,result[2]
        
        return False,None,None
    
    def pass_left(self, value):
        if self.right.value is not None:
            self.right.value += value
            return
        
        self.right.pass_left(value)
    
    def pass_right(self, value):
        if self.left.value is not None:
            self.left.value += value
            return
        
        self.left.pass_right(value)
    
def parse_pair(line):
    pairs = []
    depth = 0
    
    for c in line:
        if c == '[':
            pair = Pair()
            pair.depth = depth
            pairs.append(pair)
            depth += 1
            
        if c.isdigit():
            pair = Pair(int(c))
            pairs[-1].setup(pair)
            
        if c == ']':
            pair = pairs[-1]
            del pairs[-1]
            
            if len(pairs) == 0:
                return pair
            
            pairs[-1].setup(pair)
            depth -= 1

pairs = []

for line in sys.stdin:
    line = line.rstrip()
    
    if line == '-1':
        break
    
    pair = parse_pair(line)
    pairs.append(pair)

highest = 0

for pair1 in pairs:
    for pair2 in pairs:
        if pair1 == pair2:
            continue
        
        result = pair1.add(pair2)
        
        while True:
            temp = result.explode()
                
            if temp[0]:
                #print(f'Exploded: {result}')
                continue
            
            temp = result.split()
            
            if temp:
                #print(f'Split: {result}')
                continue
            
            #print(f'Nothing: {result}')
            break
    
        if result.magnitude() > highest:
            highest = result.magnitude()

print(highest)
