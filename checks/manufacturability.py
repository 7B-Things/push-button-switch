import cadquery as cq
from ..components.switch_bottom import build_switch_bottom


def run_checks():
    # Check to make sure the component can be build without an error
    try:
        bottom = build_switch_bottom()
    except:
        raise Exception("There was an error building the component")

    if bottom == None:
        raise Exception("There was an error building the component")
