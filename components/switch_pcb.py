# Semblage v0.5.0-alpha
import cadquery as cq
# start_params
mounting_holes=[(7.5,9.5,0.0),(7.5,-9.5,0.0),(-7.5,-9.5,0.0),] # {"data_type":"tuple","comment":""}
audio_conn_mounting_holes=[(8.45,5.0,0.0),(10.95,5.0,0.0),(8.45,-5.0,0.0),(10.95,-5.0,0.0),(3.45,0.0,0.0),] # {"data_type":"tuple","comment":""}
switch_holes=[(-6.75,5.15,0.0),(-6.75,0.0,0.0),(-6.75,-5.15,0.0),] # {"data_type":"tuple","comment":""}
# end_params
def build_switch_pcb():
    # meta {"visible":true}
    switch_pcb=cq
    switch_pcb=switch_pcb.Workplane("XY").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox").tag("switch_pcb")
    switch_pcb=switch_pcb.rect(25.0,25.0,centered=True,forConstruction=False)
    switch_pcb=switch_pcb.extrude(1.65,combine=True,clean=True,both=False,taper=0.0)
    switch_pcb=switch_pcb.faces(">Z").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox")
    switch_pcb=switch_pcb.pushPoints(mounting_holes)
    switch_pcb=switch_pcb.hole(2.4,depth=None,clean=True)
    switch_pcb=switch_pcb.faces(">Z").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox")
    switch_pcb=switch_pcb.pushPoints(audio_conn_mounting_holes)
    switch_pcb=switch_pcb.hole(1.2,depth=None,clean=True)
    switch_pcb=switch_pcb.faces(">Z").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox")
    switch_pcb=switch_pcb.pushPoints(switch_holes)
    switch_pcb=switch_pcb.hole(0.8,depth=None,clean=True)
    return switch_pcb
switch_pcb=build_switch_pcb()

