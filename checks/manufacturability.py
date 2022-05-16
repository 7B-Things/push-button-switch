import cadquery as cq
from components.switch_bottom import build_switch_bottom
from components.switch_body import build_switch_body
from components.switch_stem import build_switch_stem


def run_checks():
    # Check to make sure the component can be build without an error
    try:
        bottom = build_switch_bottom()
        switch_body = build_switch_body()
        switch_stem = build_switch_stem()
    except:
        raise Exception("There was an error building the component")

    if bottom == None:
        raise Exception("There was an error building the component")
