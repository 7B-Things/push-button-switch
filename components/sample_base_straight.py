# Semblage v0.5.0-alpha
import cadquery as cq
# start_params
switch_diameter=75.0 # {"data_type":"number","comment":"The diameter of the switch that this base will attach to."}
base_thickness=5.0 # {"data_type":"number","comment":""}
# end_params
def build_straight_base():
    # meta {"visible":true}
    straight_base=cq
    straight_base=straight_base.Workplane("XY").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox").tag("straight_base")
    straight_base=straight_base.circle(switch_diameter / 2.0,forConstruction=False)
    straight_base=straight_base.extrude(5.0,combine=True,clean=True,both=False,taper=0.0)
    straight_base=straight_base.faces("|Z").faces(">Z").workplane(offset=0.0,invert=True,centerOption="CenterOfBoundBox")
    straight_base=straight_base.circle(switch_diameter / 2.0 - 5.0,forConstruction=False)
    straight_base=straight_base.cutBlind(base_thickness - 3.0,clean=True,taper=0.0)
    straight_base=straight_base.faces("|Z").faces("<Z[-2]").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox")
    straight_base=straight_base.polarArray(switch_diameter / 2.0 - 15.0,startAngle=60.0,angle=360.0,count=3,fill=True,rotate=True)
    straight_base=straight_base.circle(5.0,forConstruction=False)
    straight_base=straight_base.extrude(2.0,combine=True,clean=True,both=False,taper=0.0)
    straight_base=straight_base.faces("|Z").faces("<Z").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox")
    straight_base=straight_base.polarArray(switch_diameter / 2.0 - 15.0,startAngle=60.0,angle=360.0,count=3,fill=True,rotate=True)
    straight_base=straight_base.cboreHole(2.4,4.4,2.4,depth=None,clean=True)
    return straight_base
straight_base=build_straight_base()

