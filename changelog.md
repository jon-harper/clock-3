# Changelog

## 2022-02-10

- Continuing fresh reprints. May have discovered an issue with the tensioner.
- Adding reference links to the BOM.
- Most parts are now in the BOM--looking to address issues like zip ties and other oddments
- Considering using placeholder (empty) bodies with part numbers to trigger the script when scraping for BOM.

## 2022-02-09

- Moving through components to add part numbers and locate model inconsistencies.
- Resolved some very old model components that didn't get updated against the prototype.
- `Printer Pard Codes.xlsx` has a significant update with tabs for each BOM category.
- Fusion model now is largely updated with internal part codes for auto-generating a BOM.
- Python script for scraping part numbers and instances is initially done.
- Removed a lot of unused and outdated files from the Fusion project.
- Removed PN080 and PN081, the freestanding 80mm fan mount and grille, along with some other stale entries.
- Exported XY Pulleys and XY Joints again for final reprint before disassembly.

## 2022-02-08

- Lots of progress auto-generating a BOM, though I will need to individually tag each part that needs to be included.
- Each part is tagged with a part number starting in "PN". These match up with the printed IDs, but are extended to any BOM part.
- This should massively speed up generating the BOM, as there are fewer parts added to the list (the script doesn't add anything without a "PN" part number).

## 2022-02-07

- Visual display of chamber temperatures is critical, so I'm quickly adjusting the default display for Klipper.
- I also plan to change the menu layout, so I'm laying the groundwork for that, as well.
- Created a repository for [Clock Face](https://github.com/jon-harper/clock-face), as I'm calling the display screen.
- Removed the OctoPrint menu and changed "SD Card" to read "Virtual SD"
- It works and I've sketched up a new menu layout, so stopping on that for now.

## 2022-02-06

- Updating issues.
- Going with a very simple, conservative, notched-edged panel approach for the floor.
- Working on auto-generating a BOM

## 2022-02-05

- Closed #11 regarding air filtration, as a working vertical prototype is completed.
- Will proceed with 0.2" plywood for panels due to cost.
- FPD of a new gantry lock bar.
- All project files now up to date with parametric heated insert holes.
- Enclosure maintaining at 45C with 48C target

## 2022-02-04

- Enclosure maintains 3C above target at 45C.
- A 2/3 full 75mm tank is currently doing the job. Printed off two 50mm tanks.

## 2022-02-03

- Working on testing Klipper, lights, and the exhaust in an enclosure.

## 2022-02-02

- Modified exhaust adapter for ~20mm OD hose.
- Continuing to work on enclosure/Klipper/filtration integration
- Widened HEPA filter latch for vertical filter.
- Added a render of the finished filter assembly.
- Added pinout diagram for the SKR 2.

## 2022-01-25 - 2022-02-01

Focused at the moment on finding a plastics fabricator to answer some basic questions about material and panels.

Meanwhile, since I can't enclose the prototype yet, I've setup Klipper on the ABS printer and am getting that ironed out. This way I can test the chamber exhaust in an real-world environment.

## 2022-01-24*

- Tested filtration with 75mm fans; much improved.
- Fit tested model with shroud--may need some minor adjustments to maintain tension around the HEPA filter.
- Current cold temperatures are making it diffiult to maintain chamber temps, so having more warp than usual and therefore more reprints.

## 2022-01-23

- Tested the filtration; seems to work slowly but efficiently. Likely will rely on 75mm fan solution.
- Iterated through some changes to the base and fan intake for the vertical stand.
- Added a shroud to help keep the HEPA cartridge in place
- Modified the TPU latch to print on its back.
- Found two Raspberry Pis.

## 2022-01-22

Filtration

- Added a small hole to the center of the 75mm tank to add more perimeters for sturdiness. The center pillar is pretty weak.
- AC -> HEPA duct is done for the vertical filtration assembly.
- Testing dual 50mm fan setup in an enclosure today.

GitHub

- Added a number of issues to GitHub and pinned an issue containing a list of what needs closing before disassembly.
- Removed Marlin firmware folder. It's not maintained or even finished, nor do I intend to move away from Klipper now.
- Reworded some of the readme.md and slimmed it down. Moved the TODO entirely to Issues.
- Moved orientation-specific STLs for filtration to subfolders.

## 2022-01-21

Clock 3

- Renaming a lot of the components to group them by function.
- Added a new #95: a panel mount piece. A 50 pack of M5 heated inserts is $14 and will cover any panel subdivisions I need to make, as well as possibly being useful elsewhere.

Filtration

- Made shims/TPU gaskets for both 75mm and 50mm fans. They push the fans out 1.6mm to make room for a hose adapter (and dampen noise).
- Both the 50mm and 75mm fan intakes work, though the right 50mm profile is incorrect.
- Working on 75mm fan exhaust to tighten fit. Modeling is difficult as there is some variation between brands in wall thicknesses, etc.
- Ordered 1" ID hose instead of 1/4". The 75mm fan is having difficulty providing pressure, so I'm going to try avoiding necking down. The 1/4" hosing may still be useful for 50mm fans.
- 1/4" hose is ideal for 50mm fan.
- 50mm fan intake is now front heavy with hose on, added hole for an insert and foot.
- Started work on a fully vertical filter tower.

## 2022-01-20

- Will need TPU shims to leave room for tubing connectors.
- Fixed fan holes to fit regardless of orientation.
- Added foot to 75mm fan intake.
- Added small front foot to use with 75mm fan intake
- Modeled 75mm radial fan

## 2022-01-19

- Dual 50mm seem like they would work for a small chamber, particularly with one 50mm running continuously as exhaust.
- Modeled and started a FPD for dual 75mm blowers.
- Looking into flexible hosing, ordered 1/4" ID, 1/2" OD silicone tubing and push connectors.
- Dual 75mm is front-heavy.

## 2022-01-18

- Created a hole diameter test for heat pressing with variable tapers.
- Big change in standard heated inserts after testing. All inserts (both vertically and horizontally) will default to 4.5mm with a -4 degree taper.
- Re-exported all affected STL files.
- Created `heated_insert_test_block.md` in the `/Docs` folder to explain heated insert testing.
- Air filter prototype is finished; waiting on new fans to test.

## 2022-01-17

- Filtration: Finished the latch, hinge, and carbon tank gasket.
- Added in all fasteners to the filtration model.
- Started printing FPD of components.
- Added renders to GitHub.
- Hinges work, latches align.
- Remodeled backside of activated carbon duct to reduce weight by 50 grams, down from over 200 (2mm perimeters, 20% infill).
- Generic ABS not happy with such a large solid volume (delaminating). Printing in PETG for now, will switch to modified ABS later.

## 2022-01-16

- Took a break yesterday; came up with some good ideas.
- ~~Working on a relatively straightforward, 3-fan filtration setup, but need to dissect a fan first to get the diameter of the inner bearings.~~
- Destroyed a fan; starting over.
- Almost done with a different setup using just two 5015 or 7530 fans.

## 2022-01-15

- Activated carbon appears to be a good supplier. No sign of rust on any of the test items.
- Updated the FAQ a bit.

## 2022-01-14

- Waiting on HEPA filters so working on polishing XY components for milestone print.
- Added surface chamfers to XY Pulleys, XY Joint components.
- Fixed #1 and #2 ID text to specify that they are Left side components.
- Redid #8, R Top XY Joint. Center rib now stretches to the wire anchor, the anchor is slightly deeper, and there is now a lip around the rear edge.
- Found a screw hole that somehow got lost on #10.

## 2022-01-13

- Had some initial success using a French press filter to hold the activated carbon.
- Testing a lid with another French press filter to act as a sealed container for activated carbon.
- AC will either need to be pre-sieved or thoroughly shaken in the container to sieve the finer particles out.
- Last export of bed corner bracket didn't have part code. This is fixed.
- Modest edits to the readme.

## 2022-01-12

- Working on some concepts for filtration.

## 2022-01-11

- Fixed mounting hole size for part cooling fan.
- Created a skeleton FAQ.
- Added a note in the `/Firmware/Klipper` folder where to find the `.cfg` files for Klipper.
- Testing virgin coconut shell activated carbon for oxidation. Hopefully this is a good supplier.
- Raised A/B steppers a few mm. Now use M5x45mm screws.
- Lots of issues resolved on the X Gantry and hotend.
- Changed mointing direction for part cooling fan. Heated insert no longer enters at an angle, which should help alignment issues.
- BLTouch mount works.
- Pretty much every component touched to update `Parameters` file. No changes due to new parameters yet.
- Went through a number of iterations on the camera mount. Have settled on a location near the front left on top of the tensioner.
- Steadily adding issues to the issue tracker. Working on setting some initial milestones.

## 2022-01-10

- Hotend now locks in place with two screws into the mount itself, rather than passing through to the front plate. This allows preassembly of the hotend and fewer screws to remove the mount plate for belt access (4->2).
- Between the above and changing the fan screws, the hotend cage, fan and all, can be removed with 4 total screws instead of 8.
- Fixed an issue with the front mount plate's vent not passing all the way through.
- Steadily adding 0.4mm chamfers to narrow holes (mostly screw holes) that touch the build surface in case of elephant's foot. Completed hotend and stepper mount modification so far.
- Also moving ID # off the build surface if an alternate location is available, e.g. under the stepper on the BMG mount. This keeps the # from fusing closed.
- Added Octopus pinout diagram to docs.
- Belt clamps now have a 'U' shape with much more grip.
- Display works on prototype now. Note: Klipper docs use a reversed orientation for their board aliases from Marlin, so I skipped using aliases and directly inserted pins.

## 2022-01-09

- Created a Klipper config repository.
- Working on an Raspberry Pi camera mount.

## 2022-01-08

- Added #110 (a different #110), which is a panel mount for an SD card extension PCB. Crack the extension case, slip the cable through the back and the PCB into the slot. Mounts with 2 brass inserts.
- Finished prototype wiring, labeling, and front panel. Now working on Klipper.
- Need to flip RPi mount to lay flat for cooling.
- Started adding issues to Github.
- Working on initial Klipper config.

## 2022-01-07

- Printing was delayed by layer shifting on the 92mm fan mount. 
- Did a relayout on the left panel mount. The Fusion timeline is more manageable and the layout of the connectors more logical.
- Front panel mounts all fit save for Ethernet and SD Card--expect those to arrive today.
- Added zip tie anchors to the forward-facing side of the panel mount.
- RJ-45 cutout is off by a bit, but it fit after some effort. Going on the TODO list.

## 2022-01-06

- More wire anchors, more wire routing.
- Finishing front panel component printing.
- Added through hole for a screw to the display slot so that the front panel will have two vertical fasteners.
- Added a cutout for full size SD card slot with the rest of the panel mounts in front. Waiting on extension PCB to arrive in the mail, so no corresponding mount yet.
- Moved USB, HDMI, and Ethernet panel mounts to left panel to avoid crowding the display area.
- Modified left interior panel mount for chamber thermistor and chamber fan ports.
- Shortened and recrimped much of the undercarriage.
- Feeling more comfortable with the general state and layout of the undercarriage wiring.
- Shortened tops of wiring panel mounts to leave space for flooring panel to inset.

## 2022-01-05

- Working on wiring in general:
- Raspberry Pi now has a dedicated power/IO cable that I've hot-glued in place. I can't figure another way to properly secure Dupont connectors, as they don't latch. Hot glue it is.
- Created a harness to properly wire the SP901E and mounted it.
- Checked light wiring connections and recrimped a few.
- Added wire anchors in numerous locations.

## 2022-01-04

- Added JST SM connectors for the alpha and beta steppers. They now plug in to the back skirt end panels instead of being wired to the board directly. This modified #106 and #107.
- Designed skirt slot for display and USB, HDMI, and Ethernet ports.
- Started initial Raspberry Pi and Klipper setup.
- Reorganized fan headers, added Supply Voltage column to `Connectors.xlsx`.
- Finished the back skirt assembly, including today's modifications.

## 2022-01-03

- Added tab with a screw hole for the skirt grille. It's a little flimsy in the center currently.
- Modified power switch port to accept 15mm hex nut cutout. Should stabilize the power switch.
- Skirt ends: moved M5 hole down to give easier access with plugs and switches and such installed.

## 2022-01-02

- Tweaked frame caps so the screw holes are more printable
- Re-exported X gantry's front plate.

## 2022-01-01

- Back in office. 31 parts to print until I'm caught up.
- Strengthened PSU bracket
- Switched to M4 screws for PSU bracket (oops)
- Modified fan exhaust and intakes to print properly. Fan mount had impossible overhangs; this is fixed.
- Tweaked tolerance for IEC plug

## 2021-12-30

- Added some bracing to the electrical panel mounts to reduce flex and moved them further back.
- Introduced the wiring panels to the master model.
- Added lighting into the model for 3 x 12 pixel strips at 60px/m (16.6mm spacing).
- Made a few fixes to the lighting strip so the zip tie does not cross over an LED.
- Plenty of new renders.

## 2021-12-29

- Fixed ABL mount issues with belt attachment screws.
- Also simplified mounting the hotend fan. Two screws mount into the fan shroud and two pass through to mount both. The fan shroud and fan then can come off with two screws instead of four.
- Added motion joints.
- Reviewed assemblies and added any missing fasteners.
- Updated wiring anchors on the x gantry. BMG mount now has a groove and zip tie channels for wiring on the right side.
- `Electrical T Slot Extension` now has a slot for inserting new roll-in tee nuts (or taking them out) without having to dismount the extrusion.

## 2021-12-28

- Fairly significant number of changes today.
- Added a number of missing brackets in the model. I *believe* they are all present now, but will check WBIO (when back in office).
- Fixed a few naming issues in the part codes list. Working on consistency and logical grouping. Re-numbering will come WBIO.
- Iterating through the models and making sure all fasteners are present.
- Added a TPU vibration damper between the AB stepper mounts and the frame. I will test TPU washers WBIO.
- Fixed minor issues with tensioner assembly/disassembly.
- Inset M3s on the tensioner top and added chamfers for screw head insertion/removal.
- Removed #97 after integrating wire guide into the right top `XY Joint` piece (#8).
- Entire XY axis assembly has fasteners but the hotend and X gantry.
- Z axis now has all fasteners; fixed Z2 stepper mislocation.
- Deleted #95 `Wire Guide` part ID entry, as the anchors are doing just fine.
- Trying to modify the side panels for the new crossbars but running into Fusion issues.

## 2021-12-27

- Finished rear exhaust and tagging pieces with IDs for the skirt.
- Publishing 104-111 and reserving 112 and 113 for the display (to be done when back in office).
- Fixed up the electronics undercarriage file with parts already designed.
- Added PSU to the model and desgined a power supply mount, as well.

## 2021-12-26

- Significant work done on skirts:
- Designed frame and section system. Front panels are modular and replaceable but fit together with screws.
- Finished 92mm fan intake, right switch panel, two identical center grille pieces.
- Work for screen and front communications ports can be done once back in office.
- Rear panel has two grilles and two fan cutouts, plus an IEC panel mount spot.
- Not entirely satisfied with fan cutouts, will work on them in the morning and push everything tomorrow.
- Added #s 100-103, the caps to cover the exterior frame edges at the base and top.

## 2021-12-23

- I needed to bring a buck converter with me, so added #85 for a 5A DROK mount.

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