a=40
b=36
c=a-b
d=a-b
e=b-c
if d>e:print("running training makes better improvement")
if d<e:print("the two training makes better improvement")
else:print("only running training's effect equal to the two training")
X=True
Y=False
W=X or Y
# Truth table
# X    Y    W
# True  True  True
# True  False  True
# False True  True
# False False False
