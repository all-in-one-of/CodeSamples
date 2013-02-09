import hou
import random

#Generate 5 random spheres and merge them

n = hou.node("/obj").createNode("geo")
n.node("file1").destroy()
mn = n.createNode('merge')
s = []
for x in range(5):
    s.append(mn.createInputNode(x, "sphere"))
    rv = (random.random() * 2) + 0.5
    s[x].parm('radx').set(str(rv))
    s[x].parm('rady').set(str(rv))
    s[x].parm('radz').set(str(rv))

mn.setDisplayFlag(True)

#Determine the order of the spheres by radius

rad = []
for y in s:
    rad.append(y.parm('radx').eval())

sorted_s = []
sorted_rad = sorted(rad, reverse=True)

for r in sorted_rad:
    for z in s:
        if z.parm('radx').eval() == r:
            sorted_s.append(z)

#Stack Spheres by size

move = 0
for m in sorted_s:
    move = move + m.parm('radx').eval()
    m.parm('ty').set(move)
    move = move + m.parm('radx').eval()

