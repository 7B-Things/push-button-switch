# Semblage v0.4.0-alpha
import cadquery as cq
# start_params
switch_diameter=50.0 # {"data_type":"number","comment":"The diameter of the switch."}
switch_holes=[(-3.25,-1.5,0.0),(3.25,-1.5,0.0),] # {"data_type":"tuple","comment":""}
# end_params
def build_switch_bottom():
    # meta {"visible":true}
    switch_bottom=cq
    switch_bottom=switch_bottom.Workplane("XY").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox").tag("switch_bottom")
    switch_bottom=switch_bottom.circle(switch_diameter / 2.0,forConstruction=False)
    switch_bottom=switch_bottom.extrude(5.0,combine=True,clean=True,both=False,taper=0.0)
    switch_bottom=switch_bottom.faces("<Z").workplane(invert=False,centerOption="CenterOfBoundBox")
    switch_bottom=switch_bottom.polarArray(switch_diameter / 2.0 - 4.0,startAngle=30,angle=360.0,count=3,fill=True,rotate=True)
    switch_bottom=switch_bottom.cboreHole(3.4,6.5,3.0,depth=None,clean=True)
    switch_bottom=switch_bottom.faces(">Z").workplane(invert=False,centerOption="CenterOfBoundBox")
    switch_bottom=switch_bottom.polarArray(switch_diameter / 2.0 - 8.0,startAngle=30,angle=360.0,count=3,fill=True,rotate=True)
    switch_bottom=switch_bottom.rect(6,3,centered=True,forConstruction=False)
    switch_bottom=switch_bottom.extrude(2.0,combine=True,clean=True,both=False,taper=0.0)
    switch_bottom=switch_bottom.faces(">Z").workplane(invert=True,centerOption="CenterOfBoundBox")
    switch_bottom=switch_bottom.polarArray(switch_diameter / 2.0 - 4.0,startAngle=30,angle=360.0,count=3,fill=True,rotate=True)
    switch_bottom=switch_bottom.circle(6.7 / 2.0,forConstruction=False)
    switch_bottom=switch_bottom.cutBlind(2.0,clean=True,taper=0.0)
    switch_bottom=switch_bottom.edges("|Z")
    switch_bottom=switch_bottom.fillet(0.5)
    switch_bottom=switch_bottom.faces("<Z[1]").workplane(invert=False,centerOption="CenterOfBoundBox")
    switch_bottom=switch_bottom.moveTo(-5.0,0.0)
    switch_bottom=switch_bottom.rect(4.0,13.0,centered=True,forConstruction=False)
    switch_bottom=switch_bottom.extrude(10,combine=True,clean=True,both=False,taper=0.0)
    switch_bottom=switch_bottom.faces("<X[1]").workplane(invert=True,centerOption="CenterOfBoundBox")
    switch_bottom=switch_bottom.pushPoints(switch_holes)
    switch_bottom=switch_bottom.circle(2.4 / 2.0,forConstruction=False)
    switch_bottom=switch_bottom.cutThruAll(clean=True,taper=0.0)
    switch_bottom=switch_bottom.faces("<Z[2]").workplane(invert=True,centerOption="CenterOfBoundBox")
    switch_bottom=switch_bottom.moveTo(switch_diameter / 4.0,0)
    switch_bottom=switch_bottom.rect(switch_diameter / 2.0 + 5.0,4.5,centered=True,forConstruction=False)
    switch_bottom=switch_bottom.cutBlind(4.5,clean=True,taper=0.0)
    switch_bottom=switch_bottom.faces("<Z[-4]").workplane(invert=True,centerOption="CenterOfBoundBox")
    switch_bottom=switch_bottom.polarArray(switch_diameter / 2.0 - 8.0,startAngle=0,angle=360.0,count=3,fill=True,rotate=True)
    switch_bottom=switch_bottom.polygon(nSides=6,diameter=6.1,forConstruction=False)
    switch_bottom=switch_bottom.cutBlind(2.3,clean=True,taper=0.0)
    switch_bottom=switch_bottom.faces("<Z[-5]").workplane(invert=True,centerOption="CenterOfBoundBox")
    switch_bottom=switch_bottom.polarArray(switch_diameter / 2.0 - 8.0,startAngle=0.0,angle=360.0,count=3,fill=True,rotate=True)
    switch_bottom=switch_bottom.circle(3.4 / 2.0,forConstruction=False)
    switch_bottom=switch_bottom.cutThruAll(clean=True,taper=0.0)
    switch_bottom=switch_bottom.faces("<X[-3]").workplane(invert=True,centerOption="CenterOfBoundBox")
    switch_bottom=switch_bottom.pushPoints(switch_holes)
    switch_bottom=switch_bottom.polygon(nSides=6,diameter=4.4,forConstruction=False)
    switch_bottom=switch_bottom.cutBlind(1.5,clean=True,taper=0.0)
    return switch_bottom
switch_bottom=build_switch_bottom()

