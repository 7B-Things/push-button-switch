import cadquery as cq
#import component.leaf_spring

def make_leaf_spring():
    result=cq
    result=result.Workplane("XY").workplane(invert=True,centerOption="CenterOfBoundBox").tag("Change")
    result=result.moveTo(-37.5,0).hLine(75,forConstruction=False).vLine(10,forConstruction=False).threePointArc(point1=(10,20),point2=(5,20),forConstruction=False).hLine(-10,forConstruction=False).threePointArc(point1=(-32.5,13),point2=(-37.5,10),forConstruction=False).close()
    result=result.extrude(10,combine=True,clean=True,both=False,taper=0.0)
    result=result.faces("<Y").workplane(invert=False,centerOption="CenterOfBoundBox")
    result=result.circle(1.0,forConstruction=False)
    result=result.cutThruAll(clean=True,taper=0.0)

    return result


switch = cq.Assembly()
switch.add(make_leaf_spring(), name="leaf spring")

switch = switch.toCompound()

show_object(switch)