# Semblage v0.4.0-alpha
import cadquery as cq
# start_params
switch_diameter=50.0 # {"data_type":"number","comment":"The outside diameter of the switch."}
body_height=18.0 # {"data_type":"number","comment":"The height of the switch body."}
# end_params
def build_switch_body():
    # meta {"visible":true,"color_r":1,"color_g":0.360784,"color_b":0.05098,"color_a":1}
    switch_body=cq
    switch_body=switch_body.Workplane("XY").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox").tag("switch_body")
    switch_body=switch_body.circle(switch_diameter / 2.0,forConstruction=False)
    switch_body=switch_body.extrude(body_height,combine=True,clean=True,both=False,taper=0.0)
    switch_body=switch_body.faces("<Z").workplane(invert=True,centerOption="CenterOfBoundBox")
    switch_body=switch_body.circle(switch_diameter / 2.0 - 4,forConstruction=False)
    switch_body=switch_body.cutBlind(body_height - 2.0,clean=True,taper=0.0)
    switch_body=switch_body.faces(">Z").workplane(invert=True,centerOption="CenterOfBoundBox")
    switch_body=switch_body.circle(10.0,forConstruction=False)
    switch_body=switch_body.cutBlind(5.0,clean=True,taper=-60.0)
    switch_body=switch_body.faces("<Z").workplane(invert=True,centerOption="CenterOfBoundBox")
    switch_body=switch_body.polarArray(switch_diameter / 2.0 -4.0,startAngle=0.0,angle=360.0,count=3,fill=True,rotate=True)
    switch_body=switch_body.circle(6.5 / 2.0,forConstruction=False)
    switch_body=switch_body.extrude(body_height,combine=True,clean=True,both=False,taper=0.0)
    switch_body=switch_body.faces("<Z").workplane(invert=True,centerOption="CenterOfBoundBox")
    switch_body=switch_body.polarArray(switch_diameter / 2.0 - 4.0,startAngle=0.0,angle=360.0,count=3,fill=True,rotate=True)
    switch_body=switch_body.circle(3.4 / 2.0,forConstruction=False)
    switch_body=switch_body.cutBlind(body_height / 2.0,clean=True,taper=0.0)
    switch_body=switch_body.faces(">Z").workplane(offset=0.0,invert=True,centerOption="CenterOfBoundBox")
    switch_body=switch_body.polarArray(switch_diameter / 2.0 - 4.0,startAngle=60,angle=360.0,count=3,fill=True,rotate=True)
    switch_body=switch_body.polygon(nSides=6,diameter=6.1,forConstruction=False)
    switch_body=switch_body.cutBlind(body_height / 2.0,clean=True,taper=0.0)
    return switch_body
switch_body=build_switch_body()

