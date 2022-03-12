# Semblage v0.4.0-alpha
import cadquery as cq
# start_params
switch_holes=[(-3.25,-1.5,0.0),(3.25,-1.5,0.0),] # {"data_type":"tuple","comment":""}
leg_leads=[(0.0,0.0,0.0),(0.0,-4.08,0.0),(0.0,4.08,0.0),] # {"data_type":"tuple","comment":""}
leg_angles=[(0,-1.4,0.0),(-4.08,-1.4,0.0),(4.08,-1.4,0.0),] # {"data_type":"tuple","comment":""}
lever_height=5.0 # {"data_type":"number","comment":"1.8 is operating position, 5.0 is free position"}
# end_params
def build_electric_switch():
    # meta {"visible":true}
    electric_switch=cq
    electric_switch=electric_switch.Workplane("XY").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox").tag("electric_switch")
    electric_switch=electric_switch.translate(vec=(0,0,7))
    electric_switch=electric_switch.rect(5.8,12.8,centered=True,forConstruction=False)
    electric_switch=electric_switch.extrude(6.5,combine=True,clean=True,both=False,taper=0.0)
    electric_switch=electric_switch.faces(">X").workplane(invert=False,centerOption="CenterOfBoundBox")
    electric_switch=electric_switch.pushPoints(switch_holes)
    electric_switch=electric_switch.circle(1.1,forConstruction=False)
    electric_switch=electric_switch.cutThruAll(clean=True,taper=0.0)
    electric_switch=electric_switch.faces("<Z").workplane(invert=False,centerOption="CenterOfBoundBox")
    electric_switch=electric_switch.pushPoints(leg_leads)
    electric_switch=electric_switch.rect(0.4,1.0,centered=True,forConstruction=False)
    electric_switch=electric_switch.extrude(2.8,combine=True,clean=True,both=False,taper=0.0)
    electric_switch=electric_switch.faces(">X[1]").workplane(invert=False,centerOption="CenterOfBoundBox")
    electric_switch=electric_switch.pushPoints(leg_angles)
    electric_switch=electric_switch.rect(1.0,0.4,centered=True,forConstruction=False)
    electric_switch=electric_switch.extrude(6.16,combine=True,clean=True,both=False,taper=0.0)
    electric_switch=electric_switch.faces(">Z").workplane(invert=False,centerOption="CenterOfBoundBox")
    electric_switch=electric_switch.center(0.0,1.0)
    electric_switch=electric_switch.rect(3.0,12.8,centered=True,forConstruction=False)
    electric_switch=electric_switch.extrude(lever_height,combine=True,clean=True,both=False,taper=0.0)
    electric_switch=electric_switch.translate(vec=(0,0,5.2))
    return electric_switch
electric_switch=build_electric_switch()
