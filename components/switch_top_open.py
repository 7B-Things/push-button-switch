# Semblage v0.5.0-alpha
import cadquery as cq
# start_params
switch_diameter=75.0 # {"data_type":"number","comment":""}
wall_thickness=2.0 # {"data_type":"number","comment":""}
top_height=13.0 # {"data_type":"number","comment":""}
# end_params
def build_switch_top():
    # meta {"visible":true,"color_r":1,"color_g":0.360784,"color_b":0.05098,"color_a":0.745098}
    switch_top=cq
    switch_top=switch_top.Workplane("XY").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox").tag("switch_top")
    switch_top=switch_top.circle(switch_diameter / 2.0,forConstruction=False)
    switch_top=switch_top.extrude(top_height,combine=True,clean=True,both=False,taper=0.0)
    switch_top=switch_top.faces("|Z").faces("<Z").workplane(offset=0.0,invert=True,centerOption="CenterOfBoundBox")
    switch_top=switch_top.circle(switch_diameter / 2.0 - wall_thickness,forConstruction=False)
    switch_top=switch_top.cutBlind(top_height - wall_thickness,clean=True,taper=0.0)
    switch_top=switch_top.workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox",origin=(0,0,0)).transformed(rotate=(90,0,0))
    switch_top=switch_top.move(0,-1.5)
    switch_top=switch_top.circle(4.0,forConstruction=False)
    switch_top=switch_top.cutBlind(switch_diameter,clean=True,taper=0.0)
    switch_top=switch_top.workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox",origin=(0,0,0)).transformed(rotate=(0,0,0))
    switch_top=switch_top.move(0,-5.5)
    switch_top=switch_top.rect(8.0,8.0,centered=True,forConstruction=False)
    switch_top=switch_top.cutBlind(switch_diameter,clean=True,taper=0.0)
    switch_top=switch_top.faces("|Z").faces(">Z").workplane(offset=0.0,invert=True,centerOption="CenterOfBoundBox")
    switch_top=switch_top.circle(10.0,forConstruction=False)
    switch_top=switch_top.cutBlind(10.0,clean=True,taper=0.0)
    switch_top=switch_top.faces("|Z").faces("<Z").workplane(offset=0.0,invert=True,centerOption="CenterOfBoundBox")
    switch_top=switch_top.polarArray(switch_diameter / 2.0 - wall_thickness - 1.5,startAngle=-30.0,angle=360.0,count=3,fill=True,rotate=True)
    switch_top=switch_top.circle(3.0,forConstruction=False)
    switch_top=switch_top.extrude(top_height,combine=True,clean=True,both=False,taper=0.0)
    switch_top=switch_top.faces("|Z").faces("<Z").workplane(offset=0.0,invert=True,centerOption="CenterOfBoundBox")
    switch_top=switch_top.polarArray(switch_diameter / 2.0 - wall_thickness - 1.5,startAngle=-30,angle=360.0,count=3,fill=True,rotate=True)
    switch_top=switch_top.circle(1.2,forConstruction=False)
    switch_top=switch_top.cutBlind(top_height,clean=True,taper=0.0)
    switch_top=switch_top.faces("|Z").faces(">Z").workplane(offset=0.0,invert=True,centerOption="CenterOfBoundBox")
    switch_top=switch_top.polarArray(switch_diameter / 2.0 - wall_thickness - 1.5,startAngle=30.0,angle=360.0,count=3,fill=True,rotate=True)
    switch_top=switch_top.polygon(nSides=5,diameter=4.5,forConstruction=False)
    switch_top=switch_top.cutBlind(5.0,clean=True,taper=0.0)
    switch_top=switch_top.faces("|Z").faces("<Z[-3]").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox")
    switch_top=switch_top.polarArray(switch_diameter / 2.0 - 12.0,startAngle=45,angle=360.0,count=4,fill=True,rotate=True)
    switch_top=switch_top.circle(2.5,forConstruction=False)
    switch_top=switch_top.extrude(3.0,combine=True,clean=True,both=False,taper=-45.0)
    switch_top=switch_top.faces("|Z").faces("<Z").workplane(offset=0.0,invert=True,centerOption="CenterOfBoundBox")
    switch_top=switch_top.polarArray(switch_diameter / 2.0,startAngle=35,angle=360.0,count=3,fill=True,rotate=True)
    switch_top=switch_top.rect(25,50,centered=True,forConstruction=False)
    switch_top=switch_top.cutBlind(8.5,clean=True,taper=0.0)
    return switch_top
switch_top=build_switch_top()

