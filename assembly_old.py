# Semblage v0.5.0-alpha
import cadquery as cq
# start_params
# end_params
def build_switch_bottom_ext():
    # meta {"visible":true}
    from components.switch_bottom import build_switch_bottom
    switch_bottom=build_switch_bottom()
    switch_bottom=switch_bottom.translate(vec=(0,0,0))
    switch_bottom=switch_bottom.rotateAboutCenter(axisEndPoint=((0,0,1)),angleDegrees=0)
    return switch_bottom
switch_bottom_ext=build_switch_bottom_ext()

def build_switch_body_ext():
    # meta {"visible":false}
    from components.switch_body import build_switch_body
    switch_body=build_switch_body()
    switch_body=switch_body.translate(vec=(0,0,6.0))
    switch_body=switch_body.rotateAboutCenter(axisEndPoint=((0,0,1)),angleDegrees=90.0)
    return switch_body
switch_body_ext=build_switch_body_ext()

def build_switch_stem_ext():
    # meta {"visible":false}
    from components.switch_stem import build_switch_stem
    switch_stem=build_switch_stem()
    switch_stem=switch_stem.translate(vec=(0,0,28))
    switch_stem=switch_stem.rotateAboutCenter(axisEndPoint=((0,0,1)),angleDegrees=0)
    return switch_stem
switch_stem_ext=build_switch_stem_ext()

def build_switch_pcb_ext():
    # meta {"visible":true,"color_r":0.207626,"color_g":0.558594,"color_b":0.146448,"color_a":1}
    from components.switch_pcb import build_switch_pcb
    switch_pcb=build_switch_pcb()
    switch_pcb=switch_pcb.translate(vec=(0,0,20.0))
    switch_pcb=switch_pcb.rotateAboutCenter(axisEndPoint=((0,0,1)),angleDegrees=0)
    return switch_pcb
switch_pcb_ext=build_switch_pcb_ext()

