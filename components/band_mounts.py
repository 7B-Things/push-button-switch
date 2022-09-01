# Semblage v0.5.0-alpha
import cadquery as cq
# start_params
hole_points=[(3.89,3.89,0.0),(-3.89,-3.89,0.0),] # {"data_type":"tuple","comment":""}
# end_params
def build_band_mounts():
    # meta {"visible":true}
    band_mounts=cq
    band_mounts=band_mounts.Workplane("XY").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox").tag("band_mounts")
    band_mounts=band_mounts.circle(15.0,forConstruction=False)
    band_mounts=band_mounts.extrude(1.0,combine=True,clean=True,both=False,taper=0.0)
    band_mounts=band_mounts.faces("|Z").faces("<Z").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox")
    band_mounts=band_mounts.pushPoints(hole_points)
    band_mounts=band_mounts.hole(2.4,depth=None,clean=True)
    band_mounts=band_mounts.faces("|Z").faces("<Z").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox")
    band_mounts=band_mounts.polarArray(13.0,startAngle=0.0,angle=360.0,count=4,fill=True,rotate=True)
    band_mounts=band_mounts.circle(2.0,forConstruction=False)
    band_mounts=band_mounts.extrude(1.5,combine=True,clean=True,both=False,taper=45.0)
    band_mounts=band_mounts.faces("|Z").faces("<Z[-2]").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox")
    band_mounts=band_mounts.circle(3.0,forConstruction=False)
    band_mounts=band_mounts.extrude(1.2,combine=True,clean=True,both=False,taper=0.0)
    band_mounts=band_mounts.faces("|Z").faces("<Z[-2]").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox")
    band_mounts=band_mounts.polarArray(13.0,startAngle=0.0,angle=360.0,count=4,fill=True,rotate=True)
    band_mounts=band_mounts.circle(1.0,forConstruction=False)
    band_mounts=band_mounts.extrude(1.5,combine=True,clean=True,both=False,taper=-45.0)
    band_mounts=band_mounts.faces("|Z").faces("<Z[-2]").workplane(offset=0.0,invert=True,centerOption="CenterOfBoundBox")
    band_mounts=band_mounts.circle(3.0,forConstruction=False)
    band_mounts=band_mounts.cutBlind(2.0,clean=True,taper=80)
    return band_mounts
band_mounts=build_band_mounts()

