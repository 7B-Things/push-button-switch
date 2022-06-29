# Semblage v0.5.0-alpha
import cadquery as cq
# start_params
peg_points=[(4.5,5.0,0.0),(4.5,-5.0,0.0),(2.0,5.0,0.0),(2.0,-5.0,0.0),(-3,0.0,0.0),] # {"data_type":"tuple","comment":"Mounting peg positions"}
pin_points=[(-2.0,2.5,0.0),(-2.0,5.0,0.0),] # {"data_type":"tuple","comment":"Locations of the rest of the leads"}
# end_params
def build_audio_connector():
    # meta {"visible":true}
    audio_connector=cq
    audio_connector=audio_connector.Workplane("XY").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox").tag("audio_connector")
    audio_connector=audio_connector.rect(11.8,12.0,centered=True,forConstruction=False)
    audio_connector=audio_connector.extrude(5.0,combine=True,clean=True,both=False,taper=0.0)
    audio_connector=audio_connector.faces(">X").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox")
    audio_connector=audio_connector.circle(3.0,forConstruction=False)
    audio_connector=audio_connector.extrude(3.2,combine=True,clean=True,both=False,taper=0.0)
    audio_connector=audio_connector.faces("<X[-2]").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox")
    audio_connector=audio_connector.rect(9.0,5.0,centered=True,forConstruction=False)
    audio_connector=audio_connector.extrude(1.0,combine=True,clean=True,both=False,taper=0.0)
    audio_connector=audio_connector.faces("|Z and <Z[-1]").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox")
    audio_connector=audio_connector.pushPoints(peg_points)
    audio_connector=audio_connector.circle(0.6,forConstruction=False)
    audio_connector=audio_connector.extrude(1.0,combine=True,clean=True,both=False,taper=0.0)
    audio_connector=audio_connector.faces("|Z and <Z[-2]").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox")
    audio_connector=audio_connector.moveTo(2.0,0.0)
    audio_connector=audio_connector.rect(0.6,1.5,centered=True,forConstruction=False)
    audio_connector=audio_connector.extrude(2.5,combine=True,clean=True,both=False,taper=0.0)
    audio_connector=audio_connector.faces("|Z").faces("<Z[-3]").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox")
    audio_connector=audio_connector.pushPoints(pin_points)
    audio_connector=audio_connector.rect(1.5,0.6,centered=True,forConstruction=False)
    audio_connector=audio_connector.extrude(2.5,combine=True,clean=True,both=False,taper=0.0)
    audio_connector=audio_connector.faces("|X").faces(">X").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox")
    audio_connector=audio_connector.hole(3.6,depth=13.0,clean=True)
    return audio_connector
audio_connector=build_audio_connector()

