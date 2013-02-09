import maya.cmds as mc
sel_obj = mc.ls( selection = True )
newname = raw_input()
newname = newname + "1"
for old in sel_obj:
    mc.rename(old, newname) 
