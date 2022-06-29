# Semblage v0.5.0-alpha
import cadquery as cq
# start_params
# end_params
def build_audio_plug():
    # meta {"visible":true}
    audio_plug=cq
    audio_plug=audio_plug.Workplane("XY").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox").tag("audio_plug")
    audio_plug=audio_plug.circle(1.5,forConstruction=False)
    audio_plug=audio_plug.extrude(4.0,combine=True,clean=True,both=False,taper=0.0)
    audio_plug=audio_plug.faces("|Z").faces(">Z").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox")
    audio_plug=audio_plug.circle(1.75,forConstruction=False)
    audio_plug=audio_plug.extrude(9.5,combine=True,clean=True,both=False,taper=0.0)
    audio_plug=audio_plug.faces("|Z").faces(">Z").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox")
    audio_plug=audio_plug.circle(2.25,forConstruction=False)
    audio_plug=audio_plug.extrude(1.0,combine=True,clean=True,both=False,taper=0.0)
    audio_plug=audio_plug.faces("|Z").faces(">Z").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox")
    audio_plug=audio_plug.circle(2.875,forConstruction=False)
    audio_plug=audio_plug.extrude(3.5,combine=True,clean=True,both=False,taper=0.0)
    audio_plug=audio_plug.faces("|Z").faces(">Z").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox")
    audio_plug=audio_plug.circle(3.5,forConstruction=False)
    audio_plug=audio_plug.extrude(30.25,combine=True,clean=True,both=False,taper=0.0)
    audio_plug=audio_plug.faces("|Z").faces(">Z").workplane(offset=0.0,invert=False,centerOption="CenterOfBoundBox")
    audio_plug=audio_plug.circle(1.75,forConstruction=False)
    audio_plug=audio_plug.extrude(50.0,combine=True,clean=True,both=False,taper=0.0)
    audio_plug=audio_plug.edges("<Z")
    audio_plug=audio_plug.chamfer(0.5,length2=None)
    return audio_plug
audio_plug=build_audio_plug()

