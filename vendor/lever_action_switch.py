# Semblage v0.5.0-alpha
import cadquery as cq
# start_params
bump_positions=[(3.25,0.0,0.0),(-3.25,0.0,0.0),] # {"data_type":"tuple","comment":""}
hole_positions=[(3.25,-1.8,0.0),(-3.25,-1.8,0.0),] # {"data_type":"tuple","comment":""}
pin_positions=[(0.0,0.0,0.0),(-5.08,0.0,0.0),(5.08,0.0,0.0),] # {"data_type":"tuple","comment":""}
# end_params
def build_leve_action_switch():
    # meta {"visible":true}
    leve_action_switch=cq
    leve_action_switch=leve_action_switch.Workplane("XY").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox").tag("leve_action_switch")
    leve_action_switch=leve_action_switch.rect(12.8,5.8,centered=True,forConstruction=False)
    leve_action_switch=leve_action_switch.extrude(6.2,combine=True,clean=True,both=False,taper=0.0)
    leve_action_switch=leve_action_switch.faces(">Y").workplane(offset=-1.0,invert=False,centerOption="CenterOfBoundBox")
    leve_action_switch=leve_action_switch.moveTo(5.4,3.1)
    leve_action_switch=leve_action_switch.polarLine(13.0,170.0,forConstruction=False)
    leve_action_switch=leve_action_switch.polarLine(0.3,10,forConstruction=False)
    leve_action_switch=leve_action_switch.polarLine(13.0,350,forConstruction=False)
    leve_action_switch=leve_action_switch.close()
    leve_action_switch=leve_action_switch.extrude(-4.10,combine=True,clean=True,both=False,taper=0.0)
    leve_action_switch=leve_action_switch.faces("<Z").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox")
    leve_action_switch=leve_action_switch.pushPoints(bump_positions)
    leve_action_switch=leve_action_switch.rect(2.1,5.8,centered=True,forConstruction=False)
    leve_action_switch=leve_action_switch.extrude(0.4,combine=True,clean=True,both=False,taper=0.0)
    leve_action_switch=leve_action_switch.faces(">Y").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox")
    leve_action_switch=leve_action_switch.pushPoints(hole_positions)
    leve_action_switch=leve_action_switch.hole(2.3,depth=None,clean=True)
    leve_action_switch=leve_action_switch.faces("<Z[-2]").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox")
    leve_action_switch=leve_action_switch.pushPoints(pin_positions)
    leve_action_switch=leve_action_switch.circle(0.4,forConstruction=False)
    leve_action_switch=leve_action_switch.extrude(3.6,combine=True,clean=True,both=False,taper=0.0)
    return leve_action_switch
leve_action_switch=build_leve_action_switch()

