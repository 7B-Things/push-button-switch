# Semblage v0.5.0-alpha
import cadquery as cq
# start_params
# end_params
def build_switch_bottom_ext():
    # meta {"visible":true,"color_r":1,"color_g":0.360784,"color_b":0.05098,"color_a":0.239216}
    from components.switch_bottom import build_switch_bottom
    switch_bottom=build_switch_bottom()
    switch_bottom=switch_bottom.translate(vec=(0,0,0))
    switch_bottom=switch_bottom.rotateAboutCenter(axisEndPoint=((0,0,1)),angleDegrees=0.0)
    return switch_bottom
switch_bottom_ext=build_switch_bottom_ext()

def build_switch_pcb_ext():
    # meta {"visible":true,"color_r":0.129634,"color_g":0.261719,"color_b":0.110765,"color_a":1}
    from components.switch_pcb import build_switch_pcb
    switch_pcb=build_switch_pcb()
    switch_pcb=switch_pcb.translate(vec=(7.5,0.0,4.0))
    switch_pcb=switch_pcb.rotateAboutCenter(axisEndPoint=((0,0,1)),angleDegrees=0.0)
    return switch_pcb
switch_pcb_ext=build_switch_pcb_ext()

def build_audio_connector_ext():
    # meta {"visible":true,"color_r":0.105469,"color_g":0.093494,"color_b":0.087693,"color_a":1}
    from vendor.audio_connector import build_audio_connector
    audio_connector=build_audio_connector()
    audio_connector=audio_connector.translate(vec=(14.5,0,5.75))
    audio_connector=audio_connector.rotateAboutCenter(axisEndPoint=((0,0,1)),angleDegrees=0.0)
    return audio_connector
audio_connector_ext=build_audio_connector_ext()

def build_audio_plug_ext():
    # meta {"visible":true,"color_r":0.132812,"color_g":0.116392,"color_b":0.108439,"color_a":1}
    from vendor.audio_plug import build_audio_plug
    audio_plug=build_audio_plug()
    audio_plug=audio_plug.translate(vec=(50.0,0,-32.5))
    audio_plug=audio_plug.rotateAboutCenter(axisEndPoint=((0,1,0)),angleDegrees=90.0)
    return audio_plug
audio_plug_ext=build_audio_plug_ext()

def build_switch_body_ext():
    # meta {"visible":true,"color_r":1,"color_g":0.36,"color_b":0.05,"color_a":1}
    from components.switch_body import build_switch_body
    switch_body=build_switch_body()
    switch_body=switch_body.translate(vec=(0,0,4.0))
    switch_body=switch_body.rotateAboutCenter(axisEndPoint=((0,0,1)),angleDegrees=90.0)
    return switch_body
switch_body_ext=build_switch_body_ext()

def build_switch_stem_ext():
    # meta {"visible":true,"color_r":1,"color_g":0.360784,"color_b":0.05098,"color_a":0.498039}
    from components.switch_stem import build_switch_stem
    switch_stem=build_switch_stem()
    switch_stem=switch_stem.translate(vec=(0,0,22))
    switch_stem=switch_stem.rotateAboutCenter(axisEndPoint=((0,0,1)),angleDegrees=90.0)
    return switch_stem
switch_stem_ext=build_switch_stem_ext()

def build_switch_cap_ext():
    # meta {"visible":false,"color_r":1,"color_g":0.36,"color_b":0.05,"color_a":1}
    from components.switch_cap import build_switch_cap
    switch_cap=build_switch_cap()
    switch_cap=switch_cap.translate(vec=(0,0,15))
    switch_cap=switch_cap.rotateAboutCenter(axisEndPoint=((0,0,1)),angleDegrees=0.0)
    return switch_cap
switch_cap_ext=build_switch_cap_ext()

def build_weurth_switch_ext():
    # meta {"visible":true,"color_r":0,"color_g":0,"color_b":0,"color_a":1}
    from vendor.weurth_switch import build_weurth_switch
    weurth_switch=build_weurth_switch()
    weurth_switch=weurth_switch.translate(vec=(1.9,0,6.1))
    weurth_switch=weurth_switch.rotateAboutCenter(axisEndPoint=((0,0,1)),angleDegrees=0.0)
    return weurth_switch
weurth_switch_ext=build_weurth_switch_ext()

def build_band_mounts_ext():
    # meta {"visible":true}
    from components.band_mounts import build_band_mounts
    band_mounts=build_band_mounts()
    band_mounts=band_mounts.translate(vec=(0,0,14))
    band_mounts=band_mounts.rotateAboutCenter(axisEndPoint=((0,0,1)),angleDegrees=45.0)
    return band_mounts
band_mounts_ext=build_band_mounts_ext()

