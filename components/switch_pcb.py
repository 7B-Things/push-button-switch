# Semblage v0.5.0-alpha
import cadquery as cq
# start_params
mounting_holes=[(8.5,10.5,0.0),(8.5,-10.5,0.0),(-8.5,-10.5,0.0),(-8.5,10.5,0.0),] # {"data_type":"tuple","comment":""}
audio_conn_mounting_holes=[(9.45,5.0,0.0),(11.95,5.0,0.0),(9.45,-5.0,0.0),(11.95,-5.0,0.0),(4.45,0.0,0.0),] # {"data_type":"tuple","comment":""}
switch_holes=[(-0.5,0,0.0),(-5.58,0.0,0.0),(-10.66,0,0.0),] # {"data_type":"tuple","comment":""}
# end_params
def build_switch_pcb():
    # meta {"visible":true}
    switch_pcb=cq
    switch_pcb=switch_pcb.Workplane("XY").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox").tag("switch_pcb")
    switch_pcb=switch_pcb.rect(27.0,25.0,centered=True,forConstruction=False)
    switch_pcb=switch_pcb.extrude(1.65,combine=True,clean=True,both=False,taper=0.0)
    switch_pcb=switch_pcb.faces(">Z").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox")
    switch_pcb=switch_pcb.pushPoints(mounting_holes)
    switch_pcb=switch_pcb.hole(2.4,depth=None,clean=True)
    switch_pcb=switch_pcb.faces(">Z").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox")
    switch_pcb=switch_pcb.pushPoints(audio_conn_mounting_holes)
    switch_pcb=switch_pcb.hole(1.2,depth=None,clean=True)
    switch_pcb=switch_pcb.faces(">Z").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox")
    switch_pcb=switch_pcb.pushPoints(switch_holes)
    switch_pcb=switch_pcb.hole(1.0,depth=None,clean=True)
    return switch_pcb
switch_pcb=build_switch_pcb()

