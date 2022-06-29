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
    switch_stem=switch_stem.circle(13.5,forConstruction=False)
    switch_stem=switch_stem.extrude(1.5,combine=True,clean=True,both=False,taper=45.0)
    switch_stem=switch_stem.faces("|Z").faces("<Z").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox")
    switch_stem=switch_stem.circle(12.5,forConstruction=False)
    switch_stem=switch_stem.extrude(1.5,combine=True,clean=True,both=False,taper=-45.0)
    switch_stem=switch_stem.faces("|Z").faces("<Z").workplane(offset=0.0,invert=True,centerOption="CenterOfBoundBox")
    switch_stem=switch_stem.circle(10.0,forConstruction=False)
    switch_stem=switch_stem.cutBlind(3.0,clean=True,taper=0.0)
    switch_stem=switch_stem.faces("|Z").faces("<Z").workplane(offset=0.0,invert=True,centerOption="CenterOfBoundBox")
    switch_stem=switch_stem.rect(30.0,2.0,centered=True,forConstruction=False)
    switch_stem=switch_stem.cutBlind(3.0,clean=True,taper=0.0)
    switch_stem=switch_stem.faces("|Z").faces("<Z").workplane(offset=0.0,invert=True,centerOption="CenterOfBoundBox")
    switch_stem=switch_stem.rect(2.0,30.0,centered=True,forConstruction=False)
    switch_stem=switch_stem.cutBlind(3.0,clean=True,taper=0.0)
    return switch_stem
switch_stem=build_switch_stem()

