# Changelog

## 2021-12-22

- Preparing for vacation, so slowing activity.
- Significantly cleaned up wiring in undercarriage area.
- Added Marlin firmware modifications to source tree. Eventually switching to Klipper, but this is functional.
- Slight modification to the SKR2 board mount to improve clearance beneath.
- Created a Raspberry Pi board mount.

## 2021-12-21

**IT PRINTS.**

- Working on firmware for lighting. May need to open an issue with Marlin or push a fix to get two light strips synced with different controllers. First controller (BTT 12864 display) follows the lighting pattern, the second is static.
- Testing a patch to `printer_event_leds.h` and `printer_event_leds.cpp`. It requires adding another preprocessor flag, but it seems to work.
- Printing at 120mm/s and 0.16mm layers okay. Blower needs a higher minimum cutoff.
- Reintroduced Y axis frame bracing to reduce frame vibration during Y axis moves.
- Modified light channel to have deeper siding.

## 2021-12-20

- Finished all crimps but ABL.
- Started mapping headers and began Wiki with corresponding article.
- Tested limit switches, fans, thermistors, bed heat, and finally first hotend heat and filament extrusion.
- Designed mount for programmable LEDs. Design is parametric based on spacing, PCB width, and LED count. Includes a zip tie anchor.
- LED tests. SP901E is finicky with WS2815, leaving it out for now.
- Nearly all connectors are now labeled.
- Resolved display issue.
- Added a modification of an old PTFE tubing coupler design. This part should go away in later revisions.
- First print should be tomorrow.

## 2021-12-19

- Recrimped (properly) all but three of the JST SM connections. Generic crimper for the XH and PH connectors arrived, so went ahead and finished the connectors for all three harnesses above the electrical undercarriage.
- Created an 80mm fan mount for cooling the steppers. Will upload after verifying the second print fits.
- Mounted the Octopus.
- Started work on skirt layout, including IEC (power in) and power switch location.
- Crimped even more wires.

## 2021-12-18

- Fixed emboss on right patch panel
- Revision 2 of XY Joint wire guide. Dealing with some elephant's foot.
- Added a file for extending spare T slot underneath for mounting equipment. The file is parametric for the end-user's modification.
- Designed clamps for board mounting
- Added screw holes to board tray to secure it in place.
- Modified blank tray template and exported STEP file to `/CAD` folder.
- Rebuilt Octopus tray from template file.
- Threw out the last four entries about clamps and boards and went with a simpler design with fewer parts and easier mounting.
- Boards mount at an angle for easier access from the front.
- Made parts for both Octopus and SKR 2 (1.4 if you can find it anymore)
- Started plotting out Octopus fan header usage (cleaner and simpler for now than using SKR 2 + bucks)

## 2021-12-17
- Fixed issue with patch panels.
- Terminated wires, probably terribly, but at least have the lengths and wrap done. Will re-crimp properly later (before using the wires).
- Finished up the `T Slot Wire Anchor` design.
- Tested panel mount--will need to be moved backwards.
- Added a wire guide for the right `XY Joint` to keep the harness elevated.
- Redesigned wire panel mounts to sit further back, leaving more room for exiting wire.
- Added a folder for test GCODE and a basic movement test file, though it needs...testing.
- Modified Z limit switches to lower them 6mm.
- Discovered issue with BLTouch mount after attaching cable ties. Will probably try and move mount position forward a few mm.

## 2021-12-16

- Finished labeling wiring panels.
- Documented part names for consistency and added info to the Readme.
- All parts with wires now have 2-3 letter codes for commonality of labels on connectors and panels.
- Designed panels for left and right side to connect wiring.
- Created `Electronics Master` file for undercarriage area.
- Working on wire anchors/guide channels
- Will start testing lighting channels at some point soon.
- Crimped way, way more wires today. Probably done crimping until the JST-PH connectors arrive.

## 2021-12-15

- Tested XY motion
- Designed and tested replacement for Z bottom bracket that includes rail alignment.
- Tested all endstops
- Added build plate
- Sketched up panel mounts for JST-SM connectors for 2-6 pins and fit-tested
- Began setting up wiring for JST-SM
- Added STL Filename column to `Part Codes`
- Crimped a lot of wires.
- Created file for tracking wire codes and terminal names

## 2021-12-14
- Fixed some issues with the left pulley component.
- Fixed an incorrect peg hole depth on right mid `XY Joint`.
- Added 5mm to the AB stepper mounts.
- Pushed Y limit switch out ~20mm to allow clearance for the X limit switch. This is hacky, but will work and keep the bed area available.
- Adjusted screw holes on right pulley component to account for the new limit switch mount.
- Designed Bowden mount for BMG.
- Designed `Gantry Lock` for servicing hotend and belts.
- Raised the Y limit switch a bit to give clearance for heated inserts in the mount.

## 2021-12-13
- Fixed up some Tony Table issues
- Created a Y rail alignment guide for in front of the tensioners
- Right `XY Joint` now has attachment points for zip ties and a guide for wiring.
- Right `XY Joint` now has additional room (1mm) for cut tolerance on the X axis extrusions/linear rail and heat growth for both the same.
- Adjusted height of XY pulley components to allow for 0.2mm difference in height of the milled Y rail.
- Fixed some issues with the Left `XY Joint`'s bottom piece.
- All `XY Joint` belt guides are now at roofed at 35 degree angles instead of the prior 45 degrees. This shouldn't be an issue with print difficulty and will give additional belt clearance.
- Ditto `Stepper Pulleys`.
- Added `Y Axis Rail Guide` parts for both sides on the `Stepper Pulleys` components. *The Y limit switch mounts on this guide*.
- Spent part of the day learning to crimp JST-SM pins and replacing Blender's heater cartridge (terminated in JST-SM, but also what Clock 3 uses)
- Added `X Limit Switch Mount`
- Published to a public repository.
- Dropped the fan duct about a millimeter to get it to blow under the nozzle (hopefully).

## 2021-12-12

- FPD and second iteration for part cooling duct. The front half is from the EVA project, modified for heated inserts.
- Redid all gantry core fastener locations to make room for other parts.
- Working belt clamp design.
- Created a Tony Table with part codes.

## 2021-12-11
- Assembled second X gantry print--much better clearances around the hotend and fit is good.
- PTFE collar issue resolved with a brace on the mounting bracket
- Added fourth screw hole to extruder mount and relocated to ensure flat connection.
- Added zip tie anchors on front mount plate for wiring.
- Started work on belt tie-offs.
- Updated part color-coding and ran into some Fusion bugs.

## 2021-12-10
- Installed bed frame of correct length. Bed is now a complete unit and finished.
- Installed new lead screws (500mm).
- X axis extrusion and Z crossbar should both arrive today for proper kinematics testing.
- Still having 12864 display issues.
- Modified the hotend mounting bracket to have an install point for ABL.
- Created a BLTouch bracket (what I have on hand).
- There is now a working mount for the BMG + stepper of arbitrary depth. Included cutouts for mounting with wires sideways.
- *Frame is now current to spec*.

## 2021-12-09
- Testing bed height adjustment screw with a locking thumbscrew, similar to the Ender 5's Z endstop trigger.
- Working in earnest on hotend mount and cooling. 
- FPD for V6/BMG mount.
- Testing `PTFE Collar` to allow PTFE tube from extruder to be removable and reattachable easily.
- Started work on paneling.
- Added a few missing joints.
- Added clearance to edges of X axis by rounding the `XY Joint` fronts.

## 2021-12-08
- Tested new limit switch arrangement to raise bed.
- Adjusted limit switch design.
- Reassembled `XY Joint`.
- Some adjustments to `Z Gantry` and `Lead Screw Plates`.
- More limit switch design tweaks to maximize volume.
- Finished bed wire support design.
- Added linear rail stop to raise maximum bed height with identical build volume.
- Working towards shortening filament path for hotend when the `X Gantry` comes together.
- Need to stiffen up new limit switch, but that can wait.
- Pursuing modular panel cutouts for flooring to simplify design and add flexibility for later.
- Modeled full exterior frame and brackets
- Combined frame and internal parts into `Master` file
- Lots of additions to `Parameters` file and fixes

## 2021-12-07
- Organized files, now tracking STLs with a naming scheme in a spreadsheet
- Fixed misnumbered and nonsequential parts
- Lots of work to fix endstop issue and raise Z bed max
- Several iterations to fix small issues with the XY Joint (no longer XY Interface)
- Actively working towards a hotend arrangement design
- Switched to button head screws for most printed parts on the test rig
- Designed cable support piece for the bed wires

## 2021-12-06
- Worked around X axis linear rail
- Adjusted XY interface for linear rail on bottom
- Modeled X gantry and hotend
- Tested cooler ideas, explored EVA as a COTS option (belts incompatible)

## 2021-12-05
- Worked on Z axis all day
- Z limit switch designed, printed, and tested
- Fixed issues with Z steppers after too much troubleshooting
- Added several files for components
- Making switch to button head screws to avoid recesses to socket head.
- Tested bed auto align
- First time with working Z kinematics!

## 2021-12-04
- Finished printing FPD Z axis parts
- Spit and polish to Z stepper mount designs
- Assembled Z axis minus limit switches

## 2021-12-03
- Lots of Z axis fixes and tweaks
- FPD of bed frame bracket
- FPD of printed Z gantry
- Finished `Z Master` file containing full Z motion
- Created XYZ master integrating XY and Z master files, will add frame

## 2021-12-02
- FPD for stepper mounts and bearing holder (prototyped in PETG to get more printers involved)
- First test of heated inserts on tensioner piece with press--went well
- Adjusted all parts to ensure press inserts holes are included where needed
- Added Z frame to `Parameters` file
- Created `Z Frame` file to assemble Z components with
- Folder cleanups, moved old stuff, reorganized `Assemblies` folders
- Finished heat pressing all tensioner parts
- Mounted first AB stepper and bearing holder, printed second
- First XY kinematics test (manually moving tensioned belts)

## 2021-12-01
- Renaming Clock 3 to Snow Angel to avoid confusion with Voron Clockwork extruder. Sigh.
- Completed FPD of right side for XY interface, refined left.
- Calculated first two frame cuts, started labeling frame for machining
- Stole X linear rail for Z axis. Will order a higher quality one for the X.
- Adapted Clock 2 limit switch plate for Y axis and made a template for the other axes.
- Ordered Clock 2 -> Snow Angel frame pieces
- FPD for tensioner (they mirror, so only one design)
- Added belt guide channel for right y gantry
- Continued to refine tensioner
- Added rail stops to X axis, built into the XY interface top pieces.
- Prelimary Z work
- Most of the design done for AB stepper mounts and internal bearing to help align the drive rods.

## 2021-11-30
- Cleaned up stepper pulley plates after assembly
- XY Interface design started
- Completed first printable design (FPD) for left side of XY interface (where X extrusion mates with the Y linear rail carriage)

## 2021-11-29
- Created XY Master file
- Swapped in braces with center threads
- Fit tested stepper pulley plates

## 2021-11-28
- Lots of work on the rear idlers and stepper pulleys
- Disassembled most of test printer
- Pieces will now be numbered and have a L or R designation where applicable.

## 2021-11-27

- Created a `clock-3` branch and started organizing files
- Expanded layout file
- Finished full belt path in layout file and added offset planes for frame and belts
- Still determining exact belt Z offset, as much of the design depends on that

## 2021-11-26

- Created a layout file for inserting derived parametrics and sketches
- Started breaking out parameters
- Sketched 3-point Z layout
- Did a quick pass at designing the stepper pulley bodies to look for issues in the layout file
- Created a hole diameter test block and brass insert practice block, inaugurating the `Tools` folder.

## ~2021-11-25

- Picked it back up again. Time for a redesign.
- Planning 3 point Z, smaller, tighter enclosure
- Switched to F695 idlers from F688 to save ~1/4" of width and depth.
- Working on a switch to brass inserts now that I have a press for them.

## Break

Life got involved.

## 2021-08-19

- Back to printing Linear Bearing Mounts.
- Planning to install wiring harness in center-rear.
- Fit tested new limit switches (Ender 3-style).

## 2021-08-15

- Printed and assembled simple PETG hotend mounting plate. The entire gantry cart for the hotend is now in finished PETG except the backside belt attachment component.
- Proceeding with Mini Fit Jr connectors for (nearly) everything.
- Installed heatsinks on alpha and beta steppers

## 2021-08-12 - 2021-08-14

- Resolved print issues
- Currently one Linear Bearing Mount printed, waiting on filament.
- Printed second Z endstop and updated firmware configuration.

## 2021-08-11

- Reprint of two Linear Bearing Mounts
- Test print for a corner bracket cover
- Reworked hotend carriage's belt fastening a bit. Added guide channels around the backside for working blind to center the belt.

## 2021-08-10

- Installed insulating washers.
- Installed finished feet.
- Installed new 204020 extrusion for above door.
- The hole for the linear bearing has too little clearance with my current print settings. Doing tests to find a balance.

## 2021-08-09

- Worked on aligning Z axis components
- Continued printing PETG bed parts
- Printed TPU feet
- Designed insulating washer for between the underside of the bed and the hex nuts

## 2021-08-08

- Started assembling and mounting print bed & frame
- Glued heatsinks on to alpha and beta steppers
- Attached PETG endstops
- Testing PETG Z limit switch mount
- More minor PETG parts
- Designed bracket cover

## 2021-08-07

- First Tr8 nut mount print
- Designed Linear Bearing Assembly
- Designed Bed Mount Alignment Spacer to properly center and align bed.
- Added limit switch bumper to nut mount
- Added Z limit switch mount
- New Alignment Spacers for Z Axis assembly.
- Minor appearance fixes.
- Continued refining bed components.

## 2021-08-06

- Restarted Z axis work
- Got Tr8 nut mount nearly designed
- Fixed up component tree, added Internal Assembly
- Assembled bed & swapped in more threaded brackets

## 2021-08-05

- Got to a good place on the hotend/belt mount components
- Designed the X Axis Limit Switch Bumper and Endstop (I need a shorter name for this)
- Attached the hotends on a simple mount. There's no way to raise or lower them (nor a print bed yet) but it gives me a moving test object.
- Working on hotend wire management and clamping belts.

## 2021-08-04

- Continued redesinging hotend/belt mount
- Integrated hotend to X gantry
- Replaced X rail stops with Y axis rail stops, need to redesign x limit switch bumper.
- Reorganized a lot of files.
- TPU printed files are now color coded a teal color.
- Started an Internal Assembly file integrating frame and components.

## 2021-08-03

- Printed final tensioners
- Fought with Fusion
- Redesigned hotend mount
- Redid Frame model from scratch.
- Modeled off-brand BCZAMD version of Bondtech's BMG ALU mount.

## 2021-08-02

- Finished reassembling both Y gantry carts and got the X gantry extrusion on.
- Iterated on tensioner design
- Printed stepper caps

## 2021-08-01

- Assembling X gantry at new height
- Designed new tensioners through several iterations. The new design is much narrower and sleeker. Also uses a shorter screw.
- Stepper alignment caps need redesign
- Inserted super thick brackets to the frame. Minor fixes.

## 2021-07-31

- Reassembling piece by piece to check for issues and square frame.
- Need to reassemble again to inset more spring-loaded t nuts and to record for instructions.
- Alignment shims now slide in to the extrusion or some other guide to prevent slippage.
- Moved X axis extrusion up 4mm to simplify logistics for screws and raise the nozzle.
- Redid floor of Y gantry carts for PETG printing

## 2021-07-30

- Finished frame brackets and fasteners, needs review
- Started printing parts in PETG.
- 80mm alignment spacer for base alignment added
- Added more pre-assembled fasteners with screws and tee nuts
- Disassembled test frame for reassembly to new specs

## 2021-07-29

- Designed Y endstop switch mount
- Lots of small polishing
- Added alignment piece for the stepper mounts
- Preformatted brackets added
- Alignment spacer for the Y axis crossbars added
- Completed frame, working on inserting all brackets and fasteners

## 2021-07-28

- Endstop switch work

## 2021-07-27

- Second pass at back piece, adjusted hole sizes for standoffs
- Initial X endstop design. Wrong way; flipped to home to the right.
- Mounted hotend gantry test.

## 2021-07-26

- Fusion is crashing again/still.
- Started hotend gantry design
- Assembles in three main pieces, finished the MGN12H carriage section in the middle.
- First pass at back piece for belt mounting.

## 2021-07-25

- Finished up V1 of the bed, still needs polish
- Now have a mount for leadscrews.
- Redesigning the jigs for the Z axis to be slightly narrower.

## 2021-07-24

- Started designing bed
- Got initial size in place, 510mm x 260mm for frame, re-using Z axis struts that are going to be widened.

## 2021-07-23

- Z Axis needs to be setup *first* or it's going to be difficult.
- Strugged with Z axis all day.

## 2021-07-22

- Fusion crapped itself. Again.
- Looking in to endstop positioning. 
- Will home to the front-right, so considering that aspect.
- Designed jig for Z axis
- Steppers will all have 2mm or 3mm thick covers on the their mounting plates to hold the 35 metal spacers in place and add additional spacing for the 45mm screws.
- 35mm spacer + 3mm plate + 3mm printed spacer = 41mm, leaving 4mm to screw in to the stepperi

## 2021-07-21

- Printed and finished linear rail stops
- Adjusted height of tensioners (off by 5mm)
- Tested XY kinematics
- Started design of Z axis 

## 2021-07-20

- Assembled full belt system
- Designed gantry lock for servicing belts and hotend
- Designed end stops for X and Y axis linear rails

## 2021-07-19

- Worked on belt system
- Printed various tensioner iterations
- Assembled working right tensioner and installed one belt.
- Adjusted wall thicknesses & offsets for tensioner. Fixed a few issues and tested a lot of bad ideas.
- Tensioner now acts as endstop for Y axis linear rails on the front side.

## 2021-07-18

- Moved out extrusions in the X axis. Ideally will resolve spacing and alignment with shorter X axis rail or 60mm wide front extrusions connecting the interior and exterior frames.
- Tweaked and assembled right Y gantry.
- Moved Y axis rails backwards to add more room for hotend.

## 2021-07-17

- Finished stepper pulley/rear idlers component.
- Assembled stepper pulley/idler blocks.
- Continued work on Y gantry.
- Finished printing Mk2 of the Y gantry. No major snags.
- Mk1 belt tensioner designed
- Began tensioner printing