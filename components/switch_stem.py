# Semblage v0.5.0-alpha
import cadquery as cq
# start_params
spring_diameter=25.0 # {"data_type":"number","comment":"The diameter of the main spring."}
# end_params
def build_switch_stem():
    # meta {"visible":true,"color_r":1,"color_g":0.360784,"color_b":0.05098,"color_a":1}
    switch_stem=cq
    switch_stem=switch_stem.Workplane("XY").workplane(offset=5.0,invert=True,centerOption="CenterOfBoundBox").tag("switch_stem")
    switch_stem=switch_stem.circle(10.0,forConstruction=False)
    switch_stem=switch_stem.extrude(4.0,combine=True,clean=True,both=False,taper=-60.0)
    switch_stem=switch_stem.faces(">Z").workplane(invert=False,centerOption="CenterOfBoundBox")
    switch_stem=switch_stem.circle(4.0,forConstruction=False)
    switch_stem=switch_stem.extrude(2.5,combine=True,clean=True,both=False,taper=0.0)
    switch_stem=switch_stem.faces("<Z").workplane(invert=False,centerOption="CenterOfBoundBox")
    switch_stem=switch_stem.cboreHole(3.7,6.5,3.0,depth=None,clean=True)
    switch_stem=switch_stem.faces("|Z").faces("<Z").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox")
    switch_stem=switch_stem.polarArray(spring_diameter / 2.0 - 1.5,startAngle=45,angle=360.0,count=4,fill=True,rotate=True)
    switch_stem=switch_stem.circle(1.5,forConstruction=False)
    switch_stem=switch_stem.extrude(3.0,combine=True,clean=True,both=False,taper=0)
    switch_stem=switch_stem.faces("|Z").faces("<Z[-2]").workplane(offset=0.75,invert=False,centerOption="CenterOfBoundBox")
    switch_stem=switch_stem.rect(spring_diameter - 4.0,spring_diameter - 4.0,centered=True,forConstruction=False)
    switch_stem=switch_stem.rotateAboutCenter(axisEndPoint=((0,0,1)),angleDegrees=45.0)
    switch_stem=switch_stem.cutBlind(1.5,clean=True,taper=0.0)
    return switch_stem
switch_stem=build_switch_stem()

