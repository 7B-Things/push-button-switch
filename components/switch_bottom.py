import cadquery as cq
from cadquery import exporters

DA = 25.4*13
A = 25.4*3
DB = 25.4*11
B = 25.4*2.75
DC = 25.4*9
L = 25.4*11.75
bore = 25.4*2

ra = 20
rb = 10
r = 2

result = (cq.Workplane('XY').circle(DA/2).extrude(A)
          .faces('>Z').workplane().circle(DC/2).tag('fa').extrude(L-A-B)
        # add fillet to the lower flange (A),
        #.edges().item(3).fillet(ra)
        .faces('>Z').workplane().circle(DB/2).extrude(B)
        # add fillet to the upper flange (B)
        #.edges().item(3).fillet(rb)
        .faces(">Z").workplane().hole(bore)#.fillet(r)
        .faces(">Z[-2]").edges(cq.RadiusNthSelector()).fillet(ra)

        )

show_object(result)