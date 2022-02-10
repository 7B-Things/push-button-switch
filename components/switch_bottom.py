# Semblage v0.4.0-alpha
import cadquery as cq
# start_params
switch_diameter=40.0 # {"data_type":"number","comment":"The diameter of the switch."}
# end_params
def build_switch_bottom():
    switch_bottom=cq  # {"visible":true}
    switch_bottom=switch_bottom.Workplane("XY").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox").tag("switch_bottom")
    switch_bottom=switch_bottom.circle(switch_diameter / 2.0,forConstruction=False)
    switch_bottom=switch_bottom.extrude(2.0,combine=True,clean=True,both=False,taper=0.0)
    return switch_bottom
switch_bottom=build_switch_bottom()
show_object(switch_bottom)
