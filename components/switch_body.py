# Semblage v0.5.0-alpha
import cadquery as cq
# start_params
switch_diameter=75.0 # {"data_type":"number","comment":""}
wall_thickness=2.0 # {"data_type":"number","comment":""}
top_height=13.0 # {"data_type":"number","comment":""}
# end_params
def build_switch_body():
    # meta {"visible":true,"color_r":1,"color_g":0.360784,"color_b":0.05098,"color_a":0.745098}
    switch_body=cq
    switch_body=switch_body.Workplane("XY").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox").tag("switch_body")
    switch_body=switch_body.circle(switch_diameter / 2.0,forConstruction=False)
    switch_body=switch_body.extrude(top_height,combine=True,clean=True,both=False,taper=0.0)
    switch_body=switch_body.faces("|Z").faces("<Z").workplane(offset=0.0,invert=True,centerOption="CenterOfBoundBox")
    switch_body=switch_body.circle(switch_diameter / 2.0 - wall_thickness,forConstruction=False)
    switch_body=switch_body.cutBlind(top_height - wall_thickness,clean=True,taper=0.0)
    switch_body=switch_body.workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox",origin=(0,0,0)).transformed(rotate=(90,0,0))
    switch_body=switch_body.move(0,-1.5)
    switch_body=switch_body.circle(5.0,forConstruction=False)
    switch_body=switch_body.cutBlind(switch_diameter,clean=True,taper=0.0)
    switch_body=switch_body.workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox",origin=(0,0,0)).transformed(rotate=(0,0,0))
    switch_body=switch_body.move(0,-5.5)
    switch_body=switch_body.rect(10.0,8.0,centered=True,forConstruction=False)
    switch_body=switch_body.cutBlind(switch_diameter,clean=True,taper=0.0)
    switch_body=switch_body.faces("|Z").faces(">Z").workplane(offset=0.0,invert=True,centerOption="CenterOfBoundBox")
    switch_body=switch_body.circle(10.0,forConstruction=False)
    switch_body=switch_body.cutBlind(10.0,clean=True,taper=0.0)
    switch_body=switch_body.faces("|Z").faces("<Z").workplane(offset=0.0,invert=True,centerOption="CenterOfBoundBox")
    switch_body=switch_body.polarArray(switch_diameter / 2.0 - wall_thickness - 1.5,startAngle=-30.0,angle=360.0,count=3,fill=True,rotate=True)
    switch_body=switch_body.circle(3.0,forConstruction=False)
    switch_body=switch_body.extrude(top_height,combine=True,clean=True,both=False,taper=0.0)
    switch_body=switch_body.faces("|Z").faces("<Z").workplane(offset=0.0,invert=True,centerOption="CenterOfBoundBox")
    switch_body=switch_body.polarArray(switch_diameter / 2.0 - wall_thickness - 1.5,startAngle=-30,angle=360.0,count=3,fill=True,rotate=True)
    switch_body=switch_body.circle(1.2,forConstruction=False)
    switch_body=switch_body.cutBlind(top_height,clean=True,taper=0.0)
    switch_body=switch_body.faces("|Z").faces(">Z").workplane(offset=0.0,invert=True,centerOption="CenterOfBoundBox")
    switch_body=switch_body.polarArray(switch_diameter / 2.0 - wall_thickness - 1.5,startAngle=30.0,angle=360.0,count=3,fill=True,rotate=True)
    switch_body=switch_body.polygon(nSides=5,diameter=4.75,forConstruction=False)
    switch_body=switch_body.cutBlind(5.0,clean=True,taper=0.0)
    switch_body=switch_body.faces("|Z").faces("<Z[-3]").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox")
    switch_body=switch_body.polarArray(switch_diameter / 2.0 - 12.0,startAngle=45,angle=360.0,count=4,fill=True,rotate=True)
    switch_body=switch_body.circle(2.5,forConstruction=False)
    switch_body=switch_body.extrude(3.0,combine=True,clean=True,both=False,taper=-45.0)
    return switch_body
switch_body=build_switch_body()

