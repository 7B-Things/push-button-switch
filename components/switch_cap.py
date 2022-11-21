# Semblage v0.5.0-alpha
import cadquery as cq
# start_params
switch_diameter=75 # {"data_type":"number","comment":""}
cap_depth=9.0 # {"data_type":"number","comment":""}
# end_params
def build_switch_cap():
    # meta {"visible":true}
    switch_cap=cq
    switch_cap=switch_cap.Workplane("XY").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox").tag("switch_cap")
    switch_cap=switch_cap.circle(switch_diameter / 2.0 + 6.0,forConstruction=False)
    switch_cap=switch_cap.extrude(cap_depth,combine=True,clean=True,both=False,taper=0.0)
    switch_cap=switch_cap.faces("|Z").faces("<Z").workplane(offset=0.0,invert=True,centerOption="CenterOfBoundBox")
    switch_cap=switch_cap.circle(switch_diameter / 2.0 + 3.0,forConstruction=False)
    switch_cap=switch_cap.cutBlind(cap_depth - 2.0,clean=True,taper=0.0)
    switch_cap=switch_cap.faces("|Z").faces("<Z[-2]").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox")
    switch_cap=switch_cap.circle(8.0,forConstruction=False)
    switch_cap=switch_cap.extrude(5.0,combine=True,clean=True,both=False,taper=0.0)
    switch_cap=switch_cap.faces("|Z").faces("<Z[-3]").workplane(offset=1.0,invert=False,centerOption="CenterOfBoundBox")
    switch_cap=switch_cap.move(0.0,2.75)
    switch_cap=switch_cap.rect(5.5,11,centered=True,forConstruction=False)
    switch_cap=switch_cap.cutBlind(2.5,clean=True,taper=0.0)
    switch_cap=switch_cap.faces("|Z").faces("<Z[-2]").workplane(offset=0.0,invert=True,centerOption="CenterOfBoundBox")
    switch_cap=switch_cap.circle(1.85,forConstruction=False)
    switch_cap=switch_cap.cutBlind(5.0,clean=True,taper=0.0)
    switch_cap=switch_cap.edges(">Z")
    switch_cap=switch_cap.fillet(2.0)
    switch_cap=switch_cap.faces("|Z").faces("<Z[-5]").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox")
    switch_cap=switch_cap.circle(switch_diameter / 2.0 - 2.0,forConstruction=False)
    switch_cap=switch_cap.circle(switch_diameter / 2.0 + 3,forConstruction=False)
    switch_cap=switch_cap.extrude(5.0,combine=True,clean=True,both=False,taper=0.0)
    return switch_cap
switch_cap=build_switch_cap()

