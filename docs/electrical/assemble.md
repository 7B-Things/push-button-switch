# Assemble (Solder)

## Introduction

Once the PCB and electrical components have been obtained, the components can be soldered onto the board. Orientation of these components, especially the microswitch are important. Pay special attention to the position of the plunger when the switch is placed on the board.

## Step 1: Placing Parts

Arrange the components on the PCB in the orientation shown in the following image. Notice that the components are placed on the side of the PCB with the silkscreen (white lines and lettering). This will be considered the top side of the PCB from here out, and it is important to place the components on this side of the PCB.

![Electrical Components with Orientation Callouts]()

## Notes on Audio Connector Placement

Notice that the barrel connector opening on the audio connector faces towards the outside of the board. The audio connector has pegs on the bottom that should fit closely into the non-plated through holes on the PCB. The audio connector should not fit correctly in any other orientation. The collar on the barrel of the connector should just slip past the edge of the PCB so that the connector is flush with the surface of the board. If it looks like the following image, than the connector is interfering with the edge of the PCB.

![Electrical Connector That Is Not Seated Properly]()

It is best if the audio connector body is flush with the surface of the PCB so that the collar can take some of the pressure off of the solder joints when the user is plugging in an audio connector.

## Notes on Microswitch Placement

The plunger of the microswitch, which is the part that gets pressed so that the switch activates, must be oriented as shown in the image above. The is because the microswitch has two modes of operation. The first is normally open (NO), where the microswitch will not activate and let current flow until the plunger is pushed down. The second is normally closed (NC), where the microswitch will be activated (let current flow) until the plunger is pushed. The push button switch needs to operate in the normally open configuration, and so the switch must be oriented as shown above. If the microswitch is turned 180 degrees, it will be in the normally closed (NC) configuration.

With that said, if there is ever a reason for the push button switch to operate in a normally closed configuration, putting the microswitch in the "wrong" orientation could meet the need. That is one of the great things about open hardware. It is easier to adapt it to individual needs and use cases.

## Step 2: Secure the Components to the PCB

The components will likely fall out if the PCB is flipped without securing them first. This can be done using a piece of tape placed over the component (never between it and the circuit board) on the top side of the board. Try to get the components as square (aligned) with the edge of the PCB as possible when securing them.

![Tape On Components to Secure Them]()

A small amount of hot glue can also be used, but caution must be used to keep from overheating and melting the parts. It is also important not to use something permanent like super glue.

If many of these boards need to be assembled over time, it may be worth investing in a PCB assembly frame like [this one](http://www.fortex.co.uk/product/pcb-assembly-jig-pcsa1/) or, better yet, building your own such as [this 3D printed one](https://www.printables.com/model/154975-circuit-board-assembly-holder) or [this aluminum extrusion one](https://www.nutsvolts.com/magazine/article/september2011_Collier).

## Step 3: Flip the PCB and Solder

Once the components have been secured, it is time to flip the board over an solder the terminals to the pads on the circuit board. The following image shows which pins need to be soldered.

![Image of Bottom Side of PCB with Solder Joints Highlighted]()

Be sure to create good solder joints (no cold solder joints) without an excess of solder. If you are new to soldering, there are guides to soldering that can be used as a reference. One example is Adafruit's [guide on making good solder joints](https://learn.adafruit.com/adafruit-guide-excellent-soldering/making-a-good-solder-joint), which is part of a [larger guide](https://learn.adafruit.com/adafruit-guide-excellent-soldering) that covers everything a beginner needs to know about soldering.

## Step 4: Inspect the Assembled Board

Once the board is soldered, the assembly is complete. Take a moment of inspect the solder joints for any problems, and look at the top side of the board to make sure that the plastic housings of components did not get melted at all and were not bumped out of position during soldering.

The finished board should look something like this.

![Fully Assembled PCB]()
