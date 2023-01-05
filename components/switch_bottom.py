# Semblage v0.5.0-alpha
import cadquery as cq
# start_params
switch_diameter=75.0 # {"data_type":"number","comment":"The overall diameter of the switch"}
pcb_mount_holes=[(16.0,9.5,0.0),(16.0,-9.5,0.0),(-1,-9.5,0.0),(-1,9.5,0.0),] # {"data_type":"tuple","comment":""}
# end_params
def build_switch_bottom():
    # meta {"visible":true,"color_r":1,"color_g":0.360784,"color_b":0.05098,"color_a":1}
    switch_bottom=cq
    switch_bottom=switch_bottom.Workplane("XY").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox").tag("switch_bottom")
    switch_bottom=switch_bottom.circle(switch_diameter / 2.0,forConstruction=False)
    switch_bottom=switch_bottom.extrude(4.0,combine=True,clean=True,both=False,taper=0.0)
    switch_bottom=switch_bottom.faces("|Z").faces(">Z").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox")
    switch_bottom=switch_bottom.pushPoints(pcb_mount_holes)
    switch_bottom=switch_bottom.hole(2.4,depth=None,clean=True)
    switch_bottom=switch_bottom.faces("|Z").faces("<Z").workplane(offset=0.0,invert=True,centerOption="CenterOfBoundBox")
    switch_bottom=switch_bottom.pushPoints(pcb_mount_holes)
    switch_bottom=switch_bottom.polygon(nSides=5,diameter=4.75,forConstruction=False)
    switch_bottom=switch_bottom.cutBlind(1.75,clean=True,taper=0.0)
    switch_bottom=switch_bottom.faces("|Z").faces(">Z").workplane(offset=0.0,invert=True,centerOption="CenterOfBoundBox")
    switch_bottom=switch_bottom.move(7,0)
    switch_bottom=switch_bottom.rect(24,13.0,centered=True,forConstruction=False)
    switch_bottom=switch_bottom.cutBlind(1.85,clean=True,taper=0.0)
    switch_bottom=switch_bottom.faces("|Z").faces("<Z").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox")
    switch_bottom=switch_bottom.polarArray(switch_diameter / 2.0 - 3.0,startAngle=60.0,angle=360.0,count=3,fill=True,rotate=True)
    switch_bottom=switch_bottom.cboreHole(2.4,4.4,2.0,depth=None,clean=True)
    switch_bottom=switch_bottom.faces("|Z").faces(">Z").workplane(offset=0.0,invert=True,centerOption="CenterOfBoundBox")
    switch_bottom=switch_bottom.polarArray(switch_diameter / 2.0 - 15.0,startAngle=60.0,angle=360.0,count=3,fill=True,rotate=True)
    switch_bottom=switch_bottom.polygon(nSides=5,diameter=4.75,forConstruction=False)
    switch_bottom=switch_bottom.cutBlind(1.75,clean=True,taper=0.0)
    switch_bottom=switch_bottom.faces("|Z").faces(">Z").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox")
    switch_bottom=switch_bottom.polarArray(switch_diameter / 2.0 - 15.0,startAngle=60.0,angle=360.0,count=3,fill=True,rotate=True)
    switch_bottom=switch_bottom.hole(2.4,depth=None,clean=True)
    switch_bottom=switch_bottom.faces("|Z").faces(">Z").workplane(offset=0.0,invert=True,centerOption="CenterOfBoundBox")
    switch_bottom=switch_bottom.move(-7.0,0.0)
    switch_bottom=switch_bottom.circle(1.2,forConstruction=False)
    switch_bottom=switch_bottom.cutThruAll(clean=True,taper=0.0)
    switch_bottom=switch_bottom.faces("|Z").faces("<Z").workplane(offset=0.0,invert=True,centerOption="CenterOfBoundBox")
    switch_bottom=switch_bottom.move(-7.0,0.0)
    switch_bottom=switch_bottom.polygon(nSides=5,diameter=4.75,forConstruction=False)
    switch_bottom=switch_bottom.cutBlind(1.75,clean=True,taper=0.0)
    return switch_bottom
switch_bottom=build_switch_bottom()

