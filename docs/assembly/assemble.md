[M2x6mm Socket Head Screw]:Parts.yaml#M2x6SocketHeadScrew
[M2x12mm Socket Head Screw]:Parts.yaml#M2x12SocketHeadScrew
[M3x6mm Socket Head Screw]:Parts.yaml#M3x6SocketHeadScrew
[1/4 Inch Heavy Rubber Band]:Parts.yaml#HeavyQuarterInchRubberBand
[1.5mm Hex Wrench]:../mechanical/Tools.yaml#HexWrench_1.5mm
[2.5mm Hex Wrench]:Tools.yaml#HexWrench_2.5mm
# Final Assembly

## Bill of Materials

{{BOM}}

## Introduction

Assuming that all of the previous mechanical and electrical sections have been completed, it is now possible to assemble the switch for use. Please be aware that some of the parts interlock in a specific way, and so the order of the assembly steps matters.

## Step 1: Attach the PCB Assembly to the Bottom

The finished circuit board is installed into the area of the switch bottom that has the relief pocket for the soldered pins. The relief pocket is highlighted in the following image.

![Relief Pocket in Switch Bottom](../images/assembly_pcb_relief_pocket.jpg)

The assembled PCB (circuit board) should be placed so that the 4 mounting holes line up with the 4 holes near the corners of the relief pocket. The PCB should be oriented so that the plunger on the microswitch is near the center of the switch bottom, and the open part of the audio connector faces the outer edge. Then an [M2x6mm Socket Head Screw]{Qty:4} can be placed in each of the 4 holes and tightened with a [1.5mm Hex Wrench]{Qty:1, Cat:Tool}. The result should look like the following image.

![PCB Attached to Switch Bottom with 4 Screws](../images/assembly_pcb_attached_to_bottom.jpg)

## Step 2: Attach the Stem to the Cap

Turn the switch cap over on the table so that the hole with the M3 captive nut is facing up. Place the stem on top of the cap so that the holes align and the counter-bore of the hole in the stem is facing up. An [M3x6mm Socket Head Screw]{Qty:1} can be inserted and tightened with a [2.5mm Hex Wrench]{Qty:1, Cat:Tool} to secure the stem to the cap. When finished, the two parts should look like the following.

![Stem Attached to Cap](../images/assembly_stem_installed_on_cap.jpg)

## Step 3: Place the Body on the Cap

Lay the switch body upside down on top of the cap, centering the hole in the body with the stem on the cap. It does not have to be perfectly centered. That will be addressed in a future step. The stack should now look like the following.

![Body Stacked on Cap](../images/assembly_body_stacked_on_cap.jpg)

## Step 4: Attach the Rubber Band Mounts

The rubber band mounts can now be attached to the stem. This part provides the attachment points for the rubber bands that will be used to suspend the cap for the user to press.

Lay the rubber band mounts on top of the stem, aligning the two holes with the holes in the stem. Place an [M2x6mm Socket Head Screw]{Qty:2} in each of the two holes and tighten with the [1.5mm Hex Wrench]{Qty:1}. The partial assembly should now look like the following.

![Rubber Band Mounts Attached to Stem](../images/assembly_rubber_band_mount_attached_to_stem.jpg)

Notice how the screw heads are aligned with the cutout in the body of the switch. This orientation will be important when the bottom is attached. The following image illustrates the proper alignment.

![Proper Alignment of Screw Heads to Body Cutout](../images/assembly_rubber_band_mount_attached_to_stem_screw_head_orientation.jpg)

## Step 5: Install the Rubber Bands

The rubber bands suspend the cap within the body of the switch, and stand in for something like a metal coil spring. A small size of rubber bands are used here, but there are other sizes of rubber bands or windings that may also work. This is just the configuration that has been found to work the best in testing.

**WARNING:** The rubber bands are typically used in dental applications and may contain latex. If you have a latex allergy, take the proper precautions such as wearing gloves. The rubber bands will be enclosed within the switch after it is fully assembled and should not come in contact with the user during normal operation.

Using a pair of tweezers, loop a [1/4 Inch Heavy Rubber Band]{Qty:4} between one of the pegs on the rubber band mounts and the peg on the switch body. This can take some patience, but the pegs are tapered so that the rubber bands will not slip off during use. The first set of pegs with the (orange) rubber band on it should look like the following.

![First Rubber Band Installed Between a Peg on the Stem and One on the Body](../images/assembly_first_rubber_band_installed.jpg)

Install the rest of the rubber bands in a similar manner, and the end result should look like this.

![All Rubber Bands Installed Between the Pegs on the Stem and the Ones on the Body](../images/assembly_all_rubber_bands_installed.jpg)

Make sure that the screw heads on the rubber band mounts are still oriented as in the image above with the red T. Sometimes that screw orientation can become rotated while working to slip the rubber bands over the pegs.

## Step 6: Install the Bottom

The final assembly step before plugging in and testing the switch is to attach the switch bottom to the rest of the assembly. 

Lay the switch bottom on the rest of the assembly so that the audio connector lines up with the cutout in the body. If these are not aligned properly it will not be possible to plug the mono audio cable into the audio connector. The screw holes that are used to attach the bottom to the body are highlighted in the following image, which also shows the orientation of the captive nuts on the bottom in relation to the cutout in the body. Attaching the bottom this way will ensure the proper orientation as long as all other assembly steps have been done correctly.

![Bottom Placed on Assembled Body with Mounting Holes Highlighted](../images/assembly_bottom_placed_on_assembled_body_with_mounting_holes.jpg)

Place an [M2x12mm Socket Head Screw]{Qty:3} in each of the 3 holes highlighted above and tighten them with a [1.5mm Hex Wrench]{Qty:1, Cat:Tool}.

**Note:** If the head of the screw will not draw down into the counter-bore pocket, either the captive nuts have not been installed in the switch body, or they have not been drawn down far enough into their pockets. Please check the [Captive Nut Installation](../mechanical/captive_nuts.md) section to make sure they were installed properly.

The bottom of the assembly should now look like the following.

![Bottom of Completed Assembly](../images/assembly_bottom_attached.jpg)

The assembly is now complete. A mono audio cable can be plugged into the audio connector on the PCB through the cutout in the cutout in the body. The other end of the audio cable can then be plugged into a switch adapter for testing.

![Mono Audio Cable Plugged In](../images/assembly_mono_audio_cable_plugged_in.jpg)

Once tested, the switch should be ready to use.