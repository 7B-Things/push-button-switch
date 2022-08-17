# Semblage v0.5.0-alpha
import cadquery as cq
# start_params
bump_positions=[(3.25,0.0,0.0),(-3.25,0.0,0.0),] # {"data_type":"tuple","comment":""}
hole_positions=[(3.25,-1.8,0.0),(-3.25,-1.8,0.0),] # {"data_type":"tuple","comment":""}
pin_positions=[(0.0,0.0,0.0),(-5.08,0.0,0.0),(5.08,0.0,0.0),] # {"data_type":"tuple","comment":""}
# end_params
def build_weurth_switch():
    # meta {"visible":true}
    weurth_switch=cq
    weurth_switch=weurth_switch.Workplane("XY").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox").tag("weurth_switch")
    weurth_switch=weurth_switch.rect(12.8,5.8,centered=True,forConstruction=False)
    weurth_switch=weurth_switch.extrude(6.2,combine=True,clean=True,both=False,taper=0.0)
    weurth_switch=weurth_switch.faces("|Y").faces(">Y").workplane(offset=-2.9,invert=False,centerOption="CenterOfBoundBox")
    weurth_switch=weurth_switch.moveTo(1.9,3.1)
    weurth_switch=weurth_switch.circle(0.6,forConstruction=False)
    weurth_switch=weurth_switch.extrude(1.0,combine=True,clean=True,both=True,taper=0.0)
    weurth_switch=weurth_switch.faces("<Z").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox")
    weurth_switch=weurth_switch.pushPoints(bump_positions)
    weurth_switch=weurth_switch.rect(2.1,5.8,centered=True,forConstruction=False)
    weurth_switch=weurth_switch.extrude(0.4,combine=True,clean=True,both=False,taper=0.0)
    weurth_switch=weurth_switch.faces(">Y").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox")
    weurth_switch=weurth_switch.pushPoints(hole_positions)
    weurth_switch=weurth_switch.hole(2.0,depth=None,clean=True)
    weurth_switch=weurth_switch.faces("<Z[-2]").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox")
    weurth_switch=weurth_switch.pushPoints(pin_positions)
    weurth_switch=weurth_switch.rect(1.0,0.4,centered=True,forConstruction=False)
    weurth_switch=weurth_switch.extrude(3.6,combine=True,clean=True,both=False,taper=0.0)
    return weurth_switch
weurth_switch=build_weurth_switch()

