# Semblage v0.4.0-alpha
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

def build_electric_switch_ext():
    # meta {"visible":true,"color_r":1,"color_g":0.05,"color_b":0.05,"color_a":1}
    from vendor.electric_switch import build_electric_switch
    electric_switch=build_electric_switch()
    electric_switch=electric_switch.translate(vec=(0.0,-0.5,4.5))
    electric_switch=electric_switch.rotateAboutCenter(axisEndPoint=((0,0,1)),angleDegrees=180)
    return electric_switch
electric_switch_ext=build_electric_switch_ext()

def build_switch_body_ext():
    # meta {"visible":true,"color_r":1,"color_g":0.360784,"color_b":0.05098,"color_a":0.631373}
    from components.switch_body import build_switch_body
    switch_body=build_switch_body()
    switch_body=switch_body.translate(vec=(0,0,5))
    switch_body=switch_body.rotateAboutCenter(axisEndPoint=((0,0,1)),angleDegrees=90.0)
    return switch_body
switch_body_ext=build_switch_body_ext()

def build_switch_stem_ext():
    # meta {"visible":true,"color_r":0.05,"color_g":0.087109,"color_b":1,"color_a":1}
    from components.switch_stem import build_switch_stem
    switch_stem=build_switch_stem()
    switch_stem=switch_stem.translate(vec=(0,0,28))
    switch_stem=switch_stem.rotateAboutCenter(axisEndPoint=((0,0,1)),angleDegrees=0)
    return switch_stem
switch_stem_ext=build_switch_stem_ext()

