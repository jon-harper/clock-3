---
title: Changelog
summary: Regular changelog of project changes.
authors: Jon Harper
date: 2022-06-05
---

This is a (mostly) daily changelog for Clock 3, beginning August 2021 during the end of testing the previous version.

## Q2 2022

### 2022-06-06

- Tweaked latch designs somewhat for cleaner appearance and open/close action (PN129-PN131).
- Tweaked initial floor tab design (PN132). Smaller and actually fits!
- Continuing to evolve ideas for hotend/extruder/part fan mount.
- Relocated a number of doc files for better access to info from the landing page.

### 2022-06-04

- Added feet resolved stability issues, though a more stable surface would still help.
- *Printing both ABS and PLA today*.
- Started work on a new hotend/gantry carriage format. Still deciding best directions, however:
    - Footprint is narrower
    - Ducting is much tigher to the heatsink on the X axis to help with directed cooling;
    - Hotend cage is 6mm shorter on Y axis, as well
- Still early on designing this, so it'll be awhile before I find a good combination of component mounting methods and arrangement.

### 2022-06-03

- Added PN131, a lower door latch.
- Also working on PN132, a spinning latch for the floor panels.
- Gasketing went in perfectly. Clock 3 is sealed.

### 2022-06-01

- Fixed Z axis issue—the anti-backlash nut wasn't secured properly on Z2.
- Printing successfully today.

### 2022-05-31

- Modified the door latch for wider opening arc.
- Testing TPU door seals and gaskets. Currently testing TPU with E6000 glue and have Loctite 406 on order.

### 2022-05-30

- Fixed numerous kinematic values for steppers. XYZE are all calibrated now.
- Made a custom temp map for the thermistor I'm using.
- Stability issues. Not sure if bed or gantry.
- Added PN129 and PN130 for a front door latch.

### 2022-05-29

- RGB lights do not work, possibly because of the SP901E. I have replaced these with 12V white LEDs for now.
- Chamber is sealed except for the around the flooring edges. May another gasketing material.
- Hotend thermistor is inaccurate. Going to create a resistance table.
- Door and all panels are back on.
- Kinematics work.
- Fans for both chamber and electronics are configured and working.

### 2022-05-28

- Undercarriage wiring is in with no issue.
- Chamber is now sealed except for:
    - Door gasketing
    - Side panel weatherseal
    - Wiring tunnels (left and right)
- New panel mount works nicely.

### 2022-05-27

- Finishing up the first electronics section and wiring details.
- Steppers mount on the panels with no issue.
- Side panels work, although initial mounting of the couplers is tough.
- Switching to final color scheme; looking good.

### 2022-05-21/22

- Panel mount can be adapted and will be.
- Have already pushed changes to hotend for BLTouch mount points; will add BLTouch adapter later after testing.
- Z Axis assembly largely finished; outline done for Z Axis section of the documentation.
- Mostly done with XY axes outline.

### 2022-05-12

- Had some catastrophic issues with multiple SKR 2s. Had to switch over to Octopus 1.1s, which required a new control case. That took a week.
- I have two printers up and expect to have a third printing ABS by tomorrow.
- Testing with Clock 3 hotend cooling assembly and BMG on an Ender 5 is going extremely well.
- Also testing a hotend panel mount on an Ender 5.
- BLTouch will need some work, so opened issue #50.

### 2022-04-27

- Still working on documentation. I took a week off to solve some long-term issues and test out a few things.
- Documentation is now merged into the clock-3 repo instead of being its own repo. This will simplify a lot of things.

### 2022-04-17

- Doing a lot of experimentation and testing right now, as well as catching up on maintenance.
- Focus ATM is testing the hotend & related assemblies on an Ender 5, including a new wiring panel mount. Will adapt for Clock 3 afteward.

### 2022-04-14

- Making heavy progress documenting assembly.
- Panels are finished, insulation is 80% done.
- Made a number of model fixes based on assembly experience, all related to fasteners.

### 2022-04-11

- Finished testing Micro Fit 3 profile, updated PN070
- Fixed #45
### 2022-04-08

- Made some milestone changes. See below.
- Adjusted due date for 0.4.5 (pre-assembly testing).
  - Although the Micro Fit 3 profile is done, it's not tested.
  - The BOM needs to be broken out into the Sales BOM and the Manufacturing/Assembly BOM. This (kinda) exists with the Materials/Parts sections, but they are different things and need to be broken out.
- Documentation is progressing steadily in parallel, but can't progress while the BOM is changing (i.e. reference points might change).

### 2022-04-07

- Today is yesterday on repeat, but with more progress.
- [jon-harper.github.io/clock3-docs/](https://jon-harper.github.io/clock3-docs/) is live, if incomplete.

### 2022-04-06
- Continuing to flesh out the documentation basics
- Started sealing the panels with polyurethane.

### 2022-04-05

- Filling out docs in earnest now.
- Rigid coupler link in the part list/BOM is now correct
- Documentation changes are now tracked in the documentation repository.
### 2022-04-04

- BomDialog now exports both CSV and Markdown formats.
- Panels are sanded and ready for better weather to apply PUR.
- Pushed first working BOM exporter with Markdown support.
- Documentation framework is progressing steadily.
- Created a panel mount profile for the MicroFit 3.0 dual row, two pin connector.
- Earth wire is now 16awg.
- Lots of added links and corrections in the part list.
- Updated `/Scripts` readme text.

### 2022-04-03

- Apparently never exported PN127 and 128, the TPU wire conduits. This is fixed.
- Continued prepping panels for sanding and sealing
- Significant progress on BOM export as a Markdown file.

### 2022-04-02

- Setup `clock3-docs` repository and MkDocs.
- Started work on a new script to re-format the `BomDialog` output CSV file into Markdown. This will possibly make its way directly into Clock3Scripts, but it's useful enough to leave it in the `/Scripts` folder.
- Spent much of the morning setting up to seal the panels in polyurethane. 

### 2022-04-01

- Assembled exterior frame, planned assembly order.
- Checked panels for fit.
- Removed extrusion channel guide from frame feet. This should greatly speed up the print time and reduce supports.
- Re-ordered Micro-Fit 3.0 panel mount connectors. USPS mis-delivered my package.
- Will likely use Jekyll for docs.
- Found the missing tee nut. BOM and model are now fully in sync and verified.
- Relabeled all extrusions with cleaner labeling

## Q1 2022

### 2022-03-30

- Added more layout files for exporting STLs
- Exploring documentation formats
- Picked up completed panels (YES!)
- Began "pre-assembly" of frame

### 2022-03-29

- Export BOM dialog works (mostly). Pushed an update to Clock3Scripts.
- Exported a working, auto-exported bill of materials.
- Removed old scripts folder and put in placeholder.
- Firmware folder is now just a `readme.md` with information on where to find the Klipper config and such.

### 2022-03-28

- Added a new repository for the Fusion scripts: Clock3Scripts.
- Migrated old scripting issues to Clock3Scripts.
- Added new linear rail alignment tools for during assembly.

### 2022-03-27

- Added a printed number to PN033, the front mount plate.
- Two new renders of the model with final panels.
- Verified all printed part counts and heat set inserts against BOM.
- Tested LED mount length.
- I believe the BOM is correct with respect to Micro Fit 3.0 connectors, although the panel mount parts are not here yet.

### 2022-03-26

- There is a literal, phantom tee nut in the model. I have counted component by component three different ways. The's an extra tee nut hidden in the model. =(
- In the process of counting, `Connectors.xlsx` is taking on new responsibilities, i.e. it's now named `ID Lists.xlsx` and contains information on parts that require fabrication or assembly: frame + tee nuts, printed parts + heat set inserts, and all of the cables.

### 2022-03-25

- `Frame Identification.pdf` now has handy arrows to the front, top left corner of each piece and an explanation of the labeling system.
- Switched hotend wiring to 20awg and connector to Micro Fit 3.
- Fixed #42 (A/B steppers have pigtailed connectors now)
- Chasing a phantom tee nut.

### 2022-03-24

- Created a set of drawings to identify and label frame components
- Spent most of the day locating and counting M5 roll in tee nuts.

### 2022-03-23
- Fixed #39 in the model.
- Fixed #35. Reprinting.
- Added more wire anchors to the model.
- Added a subfolder in `/CAD` called `Font`. Inside is Hack, the monospace font used for labeling part numbers. A readme and links to the project page are included.
- Fixed #41 by modeling the USB C buck converter.
- Started a Fusion plugin to collect scripts.
- Fixed #38.

### 2022-03-22

- Opened a lot of issues and a new milestone.
- New render.
- Nearly all components are counted from the BOM.
- Set side panel depth to 6mm to fit all panels on 1x 4'x5'x12mm sheet and 1x 4'x5'x6mm sheet.
- Will need to rework acrylic to 3mm. 6mm total with an air gap is sufficient. This was pointed out by the fabricator (thank you, Michael).
- Finalized laser cut layout and submitted for fabrication.
- Started modeling PTFE filament guide.

### 2022-03-21

- Integrating printed parts to general part list.
- Parts have new, simpler name scheme and .stl filenames are auto-generated. Now to update the model...
- New PN070-073 (electrical panel mounts).
- Removed panel mount frames, PN074 and PN075.
- Renamed STL files to match new naming scheme.
- Inserted panel mounts into the model.
- Added PIR foam cutouts for panel mounts, which were previously missing. Have not updated drawings yet.
- Updated each component in the model with new Description fields and checked for issues.
- Fixed #31. PSU now uses M4x8mm BHCS.
- Uploading an initial, mostly verified, bill of materials.
- Fixed depth of external couplers on the side panels.

### 2022-03-20

- Working on issue #28 fairly steadily.
- All wire runs will now have an ID to aid tracking and assembly.
- Wire IDs are based on component IDs
- IDs not involving the PSU are tailed with a letter code indicating distance from MCU, e.g. HE-A is MCU->chamber panel mount, HE-B is from the right chamber panel to the tooldhead panel.
- There are a few third level connectors with a -C. The modified BLTouch wire is ABL-C and connects to ABL-B. Likewise, I included a -C for LED strips. Even though they are soldered on, they still have to be made by the builder. 
- Added initial drawings for foam insulation to the `/BOM` folder
- Tallied and labeled all wires, connectors, and pins.
- Updated ExtractBOM_PN. File location is currently hardcoded and it lacks a UI, but those are already on the radar.

### 2022-03-19

- Adjusted dimensions to be uniform 6 or 12mm for panels due to material availability.
- Updated model and laser cut sketches.
- Working on a new panel mount design.

### 2022-03-18

- Laid out panels for laser cutting on 4'x5' sheets.
- Now have both engineering sketches and laser cut paths in the `BOM` folder; closing #33

### 2022-03-17

- Finished draft of engineering sketches.
- Several more renders of the panels for the fabricator to see.
- Re-export PN016, the stepper mounts, as I forgot on the 16th.

### 2022-03-16

- Completely remodeled the outside frame and panels, as the timeline was already in bad shape. It finally got corrupted and I threw it out and started over. The results are much cleaner.
- AB stepper mounts are 5mm shorter (again).
- Restarting engineering sketches again due to frame and panel problems. Should go much more quickly.

### 2022-03-15

- Modeled piano hinge
- Attempted to update the the `Outside Frame` file and on to finish the drawings, but Fusion is crashing constantly.
- Will need to merge printed part list in to `General Part List.xlsx` for proper export as a CSV.
- Exported first completed set of panel sketches.

### 2022-03-14

- Cleanup and tweaking to the readme file.
- Lots of issue and milestone cleanups.
- Preparing `General Part List.xlsx` to be exported as a `.csv` file instead of tab-delimited.
- Will need to merge printed part list into the general file.
- Added a value column and merged the default values.
- The Fusion Python script now reads in the CSV file and optionally includes default values, then scrapes the model for part numbers, and exports to a specified file.
- The UI does not work correctly. It appears, but events do not fire properly.

### 2022-03-12

- Added printed part numbers to PN123 and PN124
- Minor edits and updates to the `General Parts List`.

### 2022-03-11

- Picked up on learning Fusion's UI API. It's built on Qt, so very familiar.

### 2022-03-10

- Learned a few lessons and laid out the panels as derived objects in a separate file, then created the drawings from that.
- Waiting on a piano hinge to draw up the top panel and hatch.
- All other fabricated pieces have drawings now.
- Exported the initial sketches (minus the top) to the `/BOM` folder.

### 2022-03-09

- Top hatch is now 300mm deep instead of 390. This leaves room for a spool holder on top of the printer.
- Continuing to work on drawings.
- Multiple new renders to illustrate paneling.

### 2022-03-08

- Exported initial designs for panels and a mockup of panels/frame to discuss with fabricator.
- Began engineering drawings for panels.

### 2022-03-06

- Finished disassembling frame.
- Modified base foot design to accomodate roll-in tee nuts.
- Now verifying total on hand count against the model.
- Aside from count verification, BOM just needs connector count and cable lengths.
- Closed disassembly milestone.

### 2022-03-05

- Re-exported PN099. File somehow got lost without being replaced.
- More fastener length fixes.

### 2022-03-04

- Continuing model and BOM verification. Working on kinematic components today.
- Restored PN088, the camera base.
- Added a linear rail plug that can be printed in TPU in case they are lost (I need them right now; figured they can't hurt).
- Lot of corrections to fastener sizes.

### 2022-03-03

- Continued model/BOM verification.
- Lots of fastener adjustments, but no major surprises
- The electrical panel mount will definitely need redesign, and the PSU mount is dubious.
- Also need a mount for the new RPi buck converter.

### 2022-03-02

- Began verification of BOM and model.
- Replaced M5x12 SHCS for the doors with M5x16.
- Shortened air filter base stand top 2mm.

### 2022-03-01

- Moved exhaust hose and PTFE coupler exits. Panels are no longer identical but this is much simpler to work around.
- FPD of wire conduit for the paneling. Since there is no physical paneling yet, the conduit will definitely need revision later. This is mostly to ensure it's doable, counted in the BOM, and have *something* to test when the paneling is fabricated.
- Model is now missing only lock collars for the F688 alignment bearings.
- Only remaining design necessary for a complete prototype are TPU gaskets for the front door. Changes definitely need to be made around the hotend and (later) the Z axis, but an enclosed prototype is almost here.
- BOM is accurately generated for all **printed** parts but lock collars and some extra zip tie anchors.
- Added the aluminum facing for PIR foam, fixed numerous issues.
- Several new renders.
- Added quite a few zip tie anchors to the model, as well.
- Added foam weather stripping to the sides of the floor panels.

### 2022-02-28

- Massive number of small edits to filenames, `Printed Part List.xlsx` and model to ensure consistency.
- Updated Raspberry Pi in the model, adding heatsink, HDMI adapter, and SD card.
- Removed even more stale STL files.
- Added PN111, a fan finger guard with about the right amount of spacing for a M3x35mm screw.
- Added SD cards, thumb screws, and other small details to the models.
- Updated the Readme file with my spare time while Fusion saves.
- Designed two styles of pull handles: one is narrow to fit the V-slot door, the other is 25mm wide for everywhere else. PN125 and 126
- Started work on wire pass-thrus for the flooring.

### 2022-02-27

- Removing PN095 and 097, as the panels are done and no M5 inserts were needed.
- Renumbered PN089 to PN095. It's now circular and is used on all A/B and Z steppers for a near-airtight seal.
- Added PN123 and PN124, the bearing slider mounts for the Z axis (left and right).
- All printed part file names have three-digit numbers now, e.g. `090 - Misc - Frame - Corner Bracket Cover.stl`. This will help sorting on every platform other than Windows.
- `Printed Part List.xlsx` is updated to reflect three-digit file names, as well.
- Added PN122, a PTFE tube guide for between the pneumatic connectors for PN120
- Fixed outside panel coupler dimensions for new panel widths.
- Moved some brackets slightly to work with thicker floor panel.
- Modeled all remaining insulation and added relevant parts.
- Finished adding fasteners to the floor panels.
- Working on ensuring the air filtration both fits and can exhaust easily. This may require work, but is doable.

### 2022-02-26

- Set panel thickness to 7/32" or ~5.56mm for front panel.
- Side panels and top are now 5/16".
- Rear panel and flooring is 7/16".
Updating model positions and sketches.
- Deleted STL files for SKR board mount, as the board itself is currently unsupported.
- Running hard against physical memory limits with Fusion when loading the master model. Pagefiles are still on spinning disks on my machine, not flash, so pagefile thrashing hurts and is possibly causing crashes.
- Fixed the alignment of a few brackets.
- Floor panel dimensions are in. Still finishing adding insulation and fasteners.

### 2022-02-25

- Lots of part corrections in the model.
- Modeled and added the 3mm spring steel build plate.
- Finished the front door and related components in the model. Added M5x14 FHCS to the BOM.
- Cleaned up the frame components to be external references instead of internal. Will fix the XY and rest of Z axis tomorrow.
- PTFE coupler and hose exhaust work well--will need TPU guide between the pneumatic couplers to align the PTFE tubes.
- Readme edits.
- Two new renders added.

### 2022-02-24

- Assembled and measured door. Approximate clearance with MISUMI hinges is 4-5mm on the handle side.
- FPD of hose exhaust and PTFE coupler for side panels. Adding PN120 and PN121.
- Testing stability of door. I've mocked up spacers that are as thick as the paneling, but I believe they are allowing the door to sag.
- Modified PN092, the frame base foot, to work with BHCS.
- Corrected a few file names against the master log.

### 2022-02-23

- Modified AB stepper mounts and TPU shim to sit on top panel.
- Extended AB stepper mount height, now uses M5 x 60mm BHCS.
- Added PN089, a stepper alignment slider. It's a TPU plug for where the linear rods from the AB steppers enter the top panel. A ball bearing sits in it and plugs the bottom to keep it airtight, but the top has room for the bearing to slide sideways to get it precisely positioned.
- Added some lateral clearance for the stepper mounting holes, as well.
- Removed `AB Stepper Modules` from the `XY Master` and pulled it into the `Master` file because it mounts above the enclosure.
- BOM tweaks.

### 2022-02-22

- Adjusted PN083/PN084 clearances around the extrusion.
- Tweaking master part list entries a bit, adding "Supplies" category that includes items of indeterminate quantity (e.g. lubricant) or that may be on hand as a tool (e.g. screwdrivers) and generally don't go on a BOM but will be needed.
- Removed old PN082 file.
- Rebalanced screws on the Z Gantries. There are now three M5 on top, three under.
- Finished insulation and fasteners for all of the panels but the flooring.
- Updated the master model and removed old paneling.
- Added in feet to the `Outer Frame` model.

### 2022-02-21

- PN100 is finished. PTFE tube stays neatly out of the way and has a shorter feed path.
- Adding new milestones and issues to help sort short- and long-term goals.
- Turns out PN083 and PN084's issues are not thickness underneath the insert but severe ringing by the printer. Removed the issue. Will fix belt tension on printer later.
- Adding insulation and joints to the new panel models in the Outer Frame file.
- Finishing out the connector list based on the wire harnesses.

### 2022-02-20

- Iterating through PN100 to get a satisfactory design.
- Nearly all internal connector wires have a prespecified length now. I will leave the undercarriage unspecified as it's short enough it can be left to the end user. Plus no two people are going to want to arrange it the same way.
- Not a lot of model progress today; focused on wiring.
- Now using a PTFE tube to stiffen the hotend wiring loom. No filament is in it--it just adds rigidity.

### 2022-02-19

- Focusing on wiring today.
- `Connectors.xlsx` has a new tab for "Upper Level Wiring". This is wiring from the lower level patch panel up, e.g. to the hotend fans. Every connector has a pin count, recommended wire gauge, and approximate length needed. More will be filled in during disassembly.
- Added PN100, a PTFE tube guide to keep it from snagging the belts. The tube will now exit out of the back right, passing near the rear belts on the way. This will keep it out of the way and anchor it while the hotend moves.
- Top panel and hatch are modeled with a piano hinge.

### 2022-02-18

- Added twin cutouts to the side panels. Right side cutout is for PTFE conduit, the left side is for exhaust.
- Still considering approachs to wiring for the hotend.

### 2022-02-17

- One year since this all really started in earnest.
- Uploaded parametric t-slot extension for the electrical undercarriage, closing #14.
- Installed thermistor for the electronics (`TE`).
- Updated `Connectors.xlsx` to reflect minor changes.
- PN013, Tensioner Cap: fixed issue with impossible to print features. M5x25 instead of M5x16 screws are needed. They're already needed for the tensioner bolt iself, so no new fasteners are introduced.

### 2022-02-16

- Raspberry Pi board mounts (PN083, PN084) are now horizontal to allow better airflow, fixing #15
- Part numbers are now broken out into "General Part List" and "Printed Part List"
- All part numbers are now three digit.
- Created wire anchor assembly.
- Door frame assembly is modeled, minus the hinges.
- Concerned hinge gap is too small for door frame, or may leave too large a gap on the handle side. May need to design printable hinges to properly align.

### 2022-02-15

- Fixed a ton of minor issues with brackets in the model.
- All brackets are now properly positioned and should be propogated.
- Removed brackets from the bed frame; will rely solely on printed parts.
- Bracket assemblies still used SHCS instead of button head; fixed and propagated.
- Filtration is in the model.
- Finished renaming printed part numbers.
- SP901E has a placeholder body with fasteners in the model, temporarily addressing #21.

### 2022-02-14

- Fixed outer frame for part ID purposes.
- Added invisible SP901E assembly to the model to get it and the appropriate fasteners inventoried.
- Updated base foot and LED strips for part numbers.
- Too many minor changes to count.
- Lots of work on the prototype to reassemble the fixed skirt panels.

### 2022-02-13

- Temporarily removed the part codes Markdown file, as it is not current. Too many changes are taking place with the BOM to keep up.
- Renamed `Printer Part Codes.xlsx` to `Part Codes.xlsx` and shifted it to the `/BOM` folder.
- Replaced stock nuts with anti-backlash in the model, fixed some missing screws in the `Z Master`
- Adjusted RPi panel mount connector profiles. The skirt is now fully modeled and should be correct in the BOM. Also tested and working.
- Made exhaust adapter fully parametric and exported to `/CAD/Templates` folder.
- Ditto LED Guide Channel.
- Exhaust adapter now has a larger fan exhaust duct coverage area to help keep it in place.
- Mass renamed filtration parts with appropriate names and updated `Part Codes`.
- Finalized Vertical Filter model.

### 2022-02-12

- Exported parametric tools for heated inserts.
- Changed a few part categories and added a "Type" column for parts.
- Modified the 80mm fan grill for better printing.
- I believe all but some very odds-and-ends parts have numbers, so closing issue #20.

### 2022-02-11

- Tensioner definitely needs rework.
- Removed PN100-PN103, the frame caps. With wood paneling, they are unnecessary.
- Pushing the `ExtractBOM_PN` Fusion script.
- Re-exporting files and continuing reprints before disassembly.
- Added a lot of entries that are not modeled, like heat shrink and zip ties.
- Most entries in the parts list now have links to reference suppliers
- New 80mm fan mounts for front and rear panels, with PNs 102 and 103

### 2022-02-10

- Continuing fresh reprints. May have discovered an issue with the tensioner.
- Adding reference links to the BOM.
- Most parts are now in the BOM--looking to address issues like zip ties and other oddments
- Considering using placeholder (empty) bodies with part numbers to trigger the script when scraping for BOM.

### 2022-02-09

- Moving through components to add part numbers and locate model inconsistencies.
- Resolved some very old model components that didn't get updated against the prototype.
- `Printer Pard Codes.xlsx` has a significant update with tabs for each BOM category.
- Fusion model now is largely updated with internal part codes for auto-generating a BOM.
- Python script for scraping part numbers and instances is initially done.
- Removed a lot of unused and outdated files from the Fusion project.
- Removed PN080 and PN081, the freestanding 80mm fan mount and grille, along with some other stale entries.
- Exported XY Pulleys and XY Joints again for final reprint before disassembly.

### 2022-02-08

- Lots of progress auto-generating a BOM, though I will need to individually tag each part that needs to be included.
- Each part is tagged with a part number starting in "PN". These match up with the printed IDs, but are extended to any BOM part.
- This should massively speed up generating the BOM, as there are fewer parts added to the list (the script doesn't add anything without a "PN" part number).

### 2022-02-07

- Visual display of chamber temperatures is critical, so I'm quickly adjusting the default display for Klipper.
- I also plan to change the menu layout, so I'm laying the groundwork for that, as well.
- Created a repository for [Clock Face](https://github.com/jon-harper/clock-face), as I'm calling the display screen.
- Removed the OctoPrint menu and changed "SD Card" to read "Virtual SD"
- It works and I've sketched up a new menu layout, so stopping on that for now.

### 2022-02-06

- Updating issues.
- Going with a very simple, conservative, notched-edged panel approach for the floor.
- Working on auto-generating a BOM

### 2022-02-05

- Closed #11 regarding air filtration, as a working vertical prototype is completed.
- Will proceed with 0.2" plywood for panels due to cost.
- FPD of a new gantry lock bar.
- All project files now up to date with parametric heated insert holes.
- Enclosure maintaining at 45C with 48C target

### 2022-02-04

- Enclosure maintains 3C above target at 45C.
- A 2/3 full 75mm tank is currently doing the job. Printed off two 50mm tanks.

### 2022-02-03

- Working on testing Klipper, lights, and the exhaust in an enclosure.

### 2022-02-02

- Modified exhaust adapter for ~20mm OD hose.
- Continuing to work on enclosure/Klipper/filtration integration
- Widened HEPA filter latch for vertical filter.
- Added a render of the finished filter assembly.
- Added pinout diagram for the SKR 2.

### 2022-01-25 - 2022-02-01

Focused at the moment on finding a plastics fabricator to answer some basic questions about material and panels.

Meanwhile, since I can't enclose the prototype yet, I've setup Klipper on the ABS printer and am getting that ironed out. This way I can test the chamber exhaust in an real-world environment.

## Q1 2022

### 2022-01-24

- Tested filtration with 75mm fans; much improved.
- Fit tested model with shroud--may need some minor adjustments to maintain tension around the HEPA filter.
- Current cold temperatures are making it diffiult to maintain chamber temps, so having more warp than usual and therefore more reprints.

### 2022-01-23

- Tested the filtration; seems to work slowly but efficiently. Likely will rely on 75mm fan solution.
- Iterated through some changes to the base and fan intake for the vertical stand.
- Added a shroud to help keep the HEPA cartridge in place
- Modified the TPU latch to print on its back.
- Found two Raspberry Pis.

### 2022-01-22

Filtration

- Added a small hole to the center of the 75mm tank to add more perimeters for sturdiness. The center pillar is pretty weak.
- AC -> HEPA duct is done for the vertical filtration assembly.
- Testing dual 50mm fan setup in an enclosure today.

GitHub

- Added a number of issues to GitHub and pinned an issue containing a list of what needs closing before disassembly.
- Removed Marlin firmware folder. It's not maintained or even finished, nor do I intend to move away from Klipper now.
- Reworded some of the readme.md and slimmed it down. Moved the TODO entirely to Issues.
- Moved orientation-specific STLs for filtration to subfolders.

### 2022-01-21

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

### 2022-01-20

- Will need TPU shims to leave room for tubing connectors.
- Fixed fan holes to fit regardless of orientation.
- Added foot to 75mm fan intake.
- Added small front foot to use with 75mm fan intake
- Modeled 75mm radial fan

### 2022-01-19

- Dual 50mm seem like they would work for a small chamber, particularly with one 50mm running continuously as exhaust.
- Modeled and started a FPD for dual 75mm blowers.
- Looking into flexible hosing, ordered 1/4" ID, 1/2" OD silicone tubing and push connectors.
- Dual 75mm is front-heavy.

### 2022-01-18

- Created a hole diameter test for heat pressing with variable tapers.
- Big change in standard heated inserts after testing. All inserts (both vertically and horizontally) will default to 4.5mm with a -4 degree taper.
- Re-exported all affected STL files.
- Created `heated_insert_test_block.md` in the `/Docs` folder to explain heated insert testing.
- Air filter prototype is finished; waiting on new fans to test.

### 2022-01-17

- Filtration: Finished the latch, hinge, and carbon tank gasket.
- Added in all fasteners to the filtration model.
- Started printing FPD of components.
- Added renders to GitHub.
- Hinges work, latches align.
- Remodeled backside of activated carbon duct to reduce weight by 50 grams, down from over 200 (2mm perimeters, 20% infill).
- Generic ABS not happy with such a large solid volume (delaminating). Printing in PETG for now, will switch to modified ABS later.

### 2022-01-16

- Took a break yesterday; came up with some good ideas.
- ~~Working on a relatively straightforward, 3-fan filtration setup, but need to dissect a fan first to get the diameter of the inner bearings.~~
- Destroyed a fan; starting over.
- Almost done with a different setup using just two 5015 or 7530 fans.

### 2022-01-15

- Activated carbon appears to be a good supplier. No sign of rust on any of the test items.
- Updated the FAQ a bit.

### 2022-01-14

- Waiting on HEPA filters so working on polishing XY components for milestone print.
- Added surface chamfers to XY Pulleys, XY Joint components.
- Fixed #1 and #2 ID text to specify that they are Left side components.
- Redid #8, R Top XY Joint. Center rib now stretches to the wire anchor, the anchor is slightly deeper, and there is now a lip around the rear edge.
- Found a screw hole that somehow got lost on #10.

### 2022-01-13

- Had some initial success using a French press filter to hold the activated carbon.
- Testing a lid with another French press filter to act as a sealed container for activated carbon.
- AC will either need to be pre-sieved or thoroughly shaken in the container to sieve the finer particles out.
- Last export of bed corner bracket didn't have part code. This is fixed.
- Modest edits to the readme.

### 2022-01-12

- Working on some concepts for filtration.

### 2022-01-11

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

### 2022-01-10

- Hotend now locks in place with two screws into the mount itself, rather than passing through to the front plate. This allows preassembly of the hotend and fewer screws to remove the mount plate for belt access (4->2).
- Between the above and changing the fan screws, the hotend cage, fan and all, can be removed with 4 total screws instead of 8.
- Fixed an issue with the front mount plate's vent not passing all the way through.
- Steadily adding 0.4mm chamfers to narrow holes (mostly screw holes) that touch the build surface in case of elephant's foot. Completed hotend and stepper mount modification so far.
- Also moving ID # off the build surface if an alternate location is available, e.g. under the stepper on the BMG mount. This keeps the # from fusing closed.
- Added Octopus pinout diagram to docs.
- Belt clamps now have a 'U' shape with much more grip.
- Display works on prototype now. Note: Klipper docs use a reversed orientation for their board aliases from Marlin, so I skipped using aliases and directly inserted pins.

### 2022-01-09

- Created a Klipper config repository.
- Working on an Raspberry Pi camera mount.

### 2022-01-08

- Added #110 (a different #110), which is a panel mount for an SD card extension PCB. Crack the extension case, slip the cable through the back and the PCB into the slot. Mounts with 2 brass inserts.
- Finished prototype wiring, labeling, and front panel. Now working on Klipper.
- Need to flip RPi mount to lay flat for cooling.
- Started adding issues to Github.
- Working on initial Klipper config.

### 2022-01-07

- Printing was delayed by layer shifting on the 92mm fan mount. 
- Did a relayout on the left panel mount. The Fusion timeline is more manageable and the layout of the connectors more logical.
- Front panel mounts all fit save for Ethernet and SD Card--expect those to arrive today.
- Added zip tie anchors to the forward-facing side of the panel mount.
- RJ-45 cutout is off by a bit, but it fit after some effort. Going on the TODO list.

### 2022-01-06

- More wire anchors, more wire routing.
- Finishing front panel component printing.
- Added through hole for a screw to the display slot so that the front panel will have two vertical fasteners.
- Added a cutout for full size SD card slot with the rest of the panel mounts in front. Waiting on extension PCB to arrive in the mail, so no corresponding mount yet.
- Moved USB, HDMI, and Ethernet panel mounts to left panel to avoid crowding the display area.
- Modified left interior panel mount for chamber thermistor and chamber fan ports.
- Shortened and recrimped much of the undercarriage.
- Feeling more comfortable with the general state and layout of the undercarriage wiring.
- Shortened tops of wiring panel mounts to leave space for flooring panel to inset.

### 2022-01-05

- Working on wiring in general:
- Raspberry Pi now has a dedicated power/IO cable that I've hot-glued in place. I can't figure another way to properly secure Dupont connectors, as they don't latch. Hot glue it is.
- Created a harness to properly wire the SP901E and mounted it.
- Checked light wiring connections and recrimped a few.
- Added wire anchors in numerous locations.

### 2022-01-04

- Added JST SM connectors for the alpha and beta steppers. They now plug in to the back skirt end panels instead of being wired to the board directly. This modified #106 and #107.
- Designed skirt slot for display and USB, HDMI, and Ethernet ports.
- Started initial Raspberry Pi and Klipper setup.
- Reorganized fan headers, added Supply Voltage column to `Connectors.xlsx`.
- Finished the back skirt assembly, including today's modifications.

### 2022-01-03

- Added tab with a screw hole for the skirt grille. It's a little flimsy in the center currently.
- Modified power switch port to accept 15mm hex nut cutout. Should stabilize the power switch.
- Skirt ends: moved M5 hole down to give easier access with plugs and switches and such installed.

### 2022-01-02

- Tweaked frame caps so the screw holes are more printable
- Re-exported X gantry's front plate.

### 2022-01-01

- Back in office. 31 parts to print until I'm caught up.
- Strengthened PSU bracket
- Switched to M4 screws for PSU bracket (oops)
- Modified fan exhaust and intakes to print properly. Fan mount had impossible overhangs; this is fixed.
- Tweaked tolerance for IEC plug

## Q4 2021

### 2021-12-30

- Added some bracing to the electrical panel mounts to reduce flex and moved them further back.
- Introduced the wiring panels to the master model.
- Added lighting into the model for 3 x 12 pixel strips at 60px/m (16.6mm spacing).
- Made a few fixes to the lighting strip so the zip tie does not cross over an LED.
- Plenty of new renders.

### 2021-12-29

- Fixed ABL mount issues with belt attachment screws.
- Also simplified mounting the hotend fan. Two screws mount into the fan shroud and two pass through to mount both. The fan shroud and fan then can come off with two screws instead of four.
- Added motion joints.
- Reviewed assemblies and added any missing fasteners.
- Updated wiring anchors on the x gantry. BMG mount now has a groove and zip tie channels for wiring on the right side.
- `Electrical T Slot Extension` now has a slot for inserting new roll-in tee nuts (or taking them out) without having to dismount the extrusion.

### 2021-12-28

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

### 2021-12-27

- Finished rear exhaust and tagging pieces with IDs for the skirt.
- Publishing 104-111 and reserving 112 and 113 for the display (to be done when back in office).
- Fixed up the electronics undercarriage file with parts already designed.
- Added PSU to the model and desgined a power supply mount, as well.

### 2021-12-26

- Significant work done on skirts:
- Designed frame and section system. Front panels are modular and replaceable but fit together with screws.
- Finished 92mm fan intake, right switch panel, two identical center grille pieces.
- Work for screen and front communications ports can be done once back in office.
- Rear panel has two grilles and two fan cutouts, plus an IEC panel mount spot.
- Not entirely satisfied with fan cutouts, will work on them in the morning and push everything tomorrow.
- Added #s 100-103, the caps to cover the exterior frame edges at the base and top.

### 2021-12-23

- I needed to bring a buck converter with me, so added #85 for a 5A DROK mount.

### 2021-12-22

- Preparing for vacation, so slowing activity.
- Significantly cleaned up wiring in undercarriage area.
- Added Marlin firmware modifications to source tree. Eventually switching to Klipper, but this is functional.
- Slight modification to the SKR2 board mount to improve clearance beneath.
- Created a Raspberry Pi board mount.

### 2021-12-21

**IT PRINTS.**

- Working on firmware for lighting. May need to open an issue with Marlin or push a fix to get two light strips synced with different controllers. First controller (BTT 12864 display) follows the lighting pattern, the second is static.
- Testing a patch to `printer_event_leds.h` and `printer_event_leds.cpp`. It requires adding another preprocessor flag, but it seems to work.
- Printing at 120mm/s and 0.16mm layers okay. Blower needs a higher minimum cutoff.
- Reintroduced Y axis frame bracing to reduce frame vibration during Y axis moves.
- Modified light channel to have deeper siding.

### 2021-12-20

- Finished all crimps but ABL.
- Started mapping headers and began Wiki with corresponding article.
- Tested limit switches, fans, thermistors, bed heat, and finally first hotend heat and filament extrusion.
- Designed mount for programmable LEDs. Design is parametric based on spacing, PCB width, and LED count. Includes a zip tie anchor.
- LED tests. SP901E is finicky with WS2815, leaving it out for now.
- Nearly all connectors are now labeled.
- Resolved display issue.
- Added a modification of an old PTFE tubing coupler design. This part should go away in later revisions.
- First print should be tomorrow.

### 2021-12-19

- Recrimped (properly) all but three of the JST SM connections. Generic crimper for the XH and PH connectors arrived, so went ahead and finished the connectors for all three harnesses above the electrical undercarriage.
- Created an 80mm fan mount for cooling the steppers. Will upload after verifying the second print fits.
- Mounted the Octopus.
- Started work on skirt layout, including IEC (power in) and power switch location.
- Crimped even more wires.

### 2021-12-18

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

### 2021-12-17
- Fixed issue with patch panels.
- Terminated wires, probably terribly, but at least have the lengths and wrap done. Will re-crimp properly later (before using the wires).
- Finished up the `T Slot Wire Anchor` design.
- Tested panel mount--will need to be moved backwards.
- Added a wire guide for the right `XY Joint` to keep the harness elevated.
- Redesigned wire panel mounts to sit further back, leaving more room for exiting wire.
- Added a folder for test GCODE and a basic movement test file, though it needs...testing.
- Modified Z limit switches to lower them 6mm.
- Discovered issue with BLTouch mount after attaching cable ties. Will probably try and move mount position forward a few mm.

### 2021-12-16

- Finished labeling wiring panels.
- Documented part names for consistency and added info to the Readme.
- All parts with wires now have 2-3 letter codes for commonality of labels on connectors and panels.
- Designed panels for left and right side to connect wiring.
- Created `Electronics Master` file for undercarriage area.
- Working on wire anchors/guide channels
- Will start testing lighting channels at some point soon.
- Crimped way, way more wires today. Probably done crimping until the JST-PH connectors arrive.

### 2021-12-15

- Tested XY motion
- Designed and tested replacement for Z bottom bracket that includes rail alignment.
- Tested all endstops
- Added build plate
- Sketched up panel mounts for JST-SM connectors for 2-6 pins and fit-tested
- Began setting up wiring for JST-SM
- Added STL Filename column to `Part Codes`
- Crimped a lot of wires.
- Created file for tracking wire codes and terminal names

### 2021-12-14
- Fixed some issues with the left pulley component.
- Fixed an incorrect peg hole depth on right mid `XY Joint`.
- Added 5mm to the AB stepper mounts.
- Pushed Y limit switch out ~20mm to allow clearance for the X limit switch. This is hacky, but will work and keep the bed area available.
- Adjusted screw holes on right pulley component to account for the new limit switch mount.
- Designed Bowden mount for BMG.
- Designed `Gantry Lock` for servicing hotend and belts.
- Raised the Y limit switch a bit to give clearance for heated inserts in the mount.

### 2021-12-13
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

### 2021-12-12

- FPD and second iteration for part cooling duct. The front half is from the EVA project, modified for heated inserts.
- Redid all gantry core fastener locations to make room for other parts.
- Working belt clamp design.
- Created a Tony Table with part codes.

### 2021-12-11
- Assembled second X gantry print--much better clearances around the hotend and fit is good.
- PTFE collar issue resolved with a brace on the mounting bracket
- Added fourth screw hole to extruder mount and relocated to ensure flat connection.
- Added zip tie anchors on front mount plate for wiring.
- Started work on belt tie-offs.
- Updated part color-coding and ran into some Fusion bugs.

### 2021-12-10
- Installed bed frame of correct length. Bed is now a complete unit and finished.
- Installed new lead screws (500mm).
- X axis extrusion and Z crossbar should both arrive today for proper kinematics testing.
- Still having 12864 display issues.
- Modified the hotend mounting bracket to have an install point for ABL.
- Created a BLTouch bracket (what I have on hand).
- There is now a working mount for the BMG + stepper of arbitrary depth. Included cutouts for mounting with wires sideways.
- *Frame is now current to spec*.

### 2021-12-09
- Testing bed height adjustment screw with a locking thumbscrew, similar to the Ender 5's Z endstop trigger.
- Working in earnest on hotend mount and cooling. 
- FPD for V6/BMG mount.
- Testing `PTFE Collar` to allow PTFE tube from extruder to be removable and reattachable easily.
- Started work on paneling.
- Added a few missing joints.
- Added clearance to edges of X axis by rounding the `XY Joint` fronts.

### 2021-12-08
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

### 2021-12-07
- Organized files, now tracking STLs with a naming scheme in a spreadsheet
- Fixed misnumbered and nonsequential parts
- Lots of work to fix endstop issue and raise Z bed max
- Several iterations to fix small issues with the XY Joint (no longer XY Interface)
- Actively working towards a hotend arrangement design
- Switched to button head screws for most printed parts on the test rig
- Designed cable support piece for the bed wires

### 2021-12-06
- Worked around X axis linear rail
- Adjusted XY interface for linear rail on bottom
- Modeled X gantry and hotend
- Tested cooler ideas, explored EVA as a COTS option (belts incompatible)

### 2021-12-05
- Worked on Z axis all day
- Z limit switch designed, printed, and tested
- Fixed issues with Z steppers after too much troubleshooting
- Added several files for components
- Making switch to button head screws to avoid recesses to socket head.
- Tested bed auto align
- First time with working Z kinematics!

### 2021-12-04
- Finished printing FPD Z axis parts
- Spit and polish to Z stepper mount designs
- Assembled Z axis minus limit switches

### 2021-12-03
- Lots of Z axis fixes and tweaks
- FPD of bed frame bracket
- FPD of printed Z gantry
- Finished `Z Master` file containing full Z motion
- Created XYZ master integrating XY and Z master files, will add frame

### 2021-12-02
- FPD for stepper mounts and bearing holder (prototyped in PETG to get more printers involved)
- First test of heated inserts on tensioner piece with press--went well
- Adjusted all parts to ensure press inserts holes are included where needed
- Added Z frame to `Parameters` file
- Created `Z Frame` file to assemble Z components with
- Folder cleanups, moved old stuff, reorganized `Assemblies` folders
- Finished heat pressing all tensioner parts
- Mounted first AB stepper and bearing holder, printed second
- First XY kinematics test (manually moving tensioned belts)

### 2021-12-01
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

### 2021-11-30
- Cleaned up stepper pulley plates after assembly
- XY Interface design started
- Completed first printable design (FPD) for left side of XY interface (where X extrusion mates with the Y linear rail carriage)

### 2021-11-29
- Created XY Master file
- Swapped in braces with center threads
- Fit tested stepper pulley plates

### 2021-11-28
- Lots of work on the rear idlers and stepper pulleys
- Disassembled most of test printer
- Pieces will now be numbered and have a L or R designation where applicable.

### 2021-11-27

- Created a `clock-3` branch and started organizing files
- Expanded layout file
- Finished full belt path in layout file and added offset planes for frame and belts
- Still determining exact belt Z offset, as much of the design depends on that

### 2021-11-26

- Created a layout file for inserting derived parametrics and sketches
- Started breaking out parameters
- Sketched 3-point Z layout
- Did a quick pass at designing the stepper pulley bodies to look for issues in the layout file
- Created a hole diameter test block and brass insert practice block, inaugurating the `Tools` folder.

### ~2021-11-25

- Picked it back up again. Time for a redesign.
- Planning 3 point Z, smaller, tighter enclosure
- Switched to F695 idlers from F688 to save ~1/4" of width and depth.
- Working on a switch to brass inserts now that I have a press for them.


### Break

Life got involved.

## Q3 2021

### 2021-08-19

- Back to printing Linear Bearing Mounts.
- Planning to install wiring harness in center-rear.
- Fit tested new limit switches (Ender 3-style).

### 2021-08-15

- Printed and assembled simple PETG hotend mounting plate. The entire gantry cart for the hotend is now in finished PETG except the backside belt attachment component.
- Proceeding with Mini Fit Jr connectors for (nearly) everything.
- Installed heatsinks on alpha and beta steppers

### 2021-08-12 - 2021-08-14

- Resolved print issues
- Currently one Linear Bearing Mount printed, waiting on filament.
- Printed second Z endstop and updated firmware configuration.

### 2021-08-11

- Reprint of two Linear Bearing Mounts
- Test print for a corner bracket cover
- Reworked hotend carriage's belt fastening a bit. Added guide channels around the backside for working blind to center the belt.

### 2021-08-10

- Installed insulating washers.
- Installed finished feet.
- Installed new 204020 extrusion for above door.
- The hole for the linear bearing has too little clearance with my current print settings. Doing tests to find a balance.

### 2021-08-09

- Worked on aligning Z axis components
- Continued printing PETG bed parts
- Printed TPU feet
- Designed insulating washer for between the underside of the bed and the hex nuts

### 2021-08-08

- Started assembling and mounting print bed & frame
- Glued heatsinks on to alpha and beta steppers
- Attached PETG endstops
- Testing PETG Z limit switch mount
- More minor PETG parts
- Designed bracket cover

### 2021-08-07

- First Tr8 nut mount print
- Designed Linear Bearing Assembly
- Designed Bed Mount Alignment Spacer to properly center and align bed.
- Added limit switch bumper to nut mount
- Added Z limit switch mount
- New Alignment Spacers for Z Axis assembly.
- Minor appearance fixes.
- Continued refining bed components.

### 2021-08-06

- Restarted Z axis work
- Got Tr8 nut mount nearly designed
- Fixed up component tree, added Internal Assembly
- Assembled bed & swapped in more threaded brackets

### 2021-08-05

- Got to a good place on the hotend/belt mount components
- Designed the X Axis Limit Switch Bumper and Endstop (I need a shorter name for this)
- Attached the hotends on a simple mount. There's no way to raise or lower them (nor a print bed yet) but it gives me a moving test object.
- Working on hotend wire management and clamping belts.

### 2021-08-04

- Continued redesinging hotend/belt mount
- Integrated hotend to X gantry
- Replaced X rail stops with Y axis rail stops, need to redesign x limit switch bumper.
- Reorganized a lot of files.
- TPU printed files are now color coded a teal color.
- Started an Internal Assembly file integrating frame and components.

### 2021-08-03

- Printed final tensioners
- Fought with Fusion
- Redesigned hotend mount
- Redid Frame model from scratch.
- Modeled off-brand BCZAMD version of Bondtech's BMG ALU mount.

### 2021-08-02

- Finished reassembling both Y gantry carts and got the X gantry extrusion on.
- Iterated on tensioner design
- Printed stepper caps

### 2021-08-01

- Assembling X gantry at new height
- Designed new tensioners through several iterations. The new design is much narrower and sleeker. Also uses a shorter screw.
- Stepper alignment caps need redesign
- Inserted super thick brackets to the frame. Minor fixes.

### 2021-07-31

- Reassembling piece by piece to check for issues and square frame.
- Need to reassemble again to inset more spring-loaded t nuts and to record for instructions.
- Alignment shims now slide in to the extrusion or some other guide to prevent slippage.
- Moved X axis extrusion up 4mm to simplify logistics for screws and raise the nozzle.
- Redid floor of Y gantry carts for PETG printing

### 2021-07-30

- Finished frame brackets and fasteners, needs review
- Started printing parts in PETG.
- 80mm alignment spacer for base alignment added
- Added more pre-assembled fasteners with screws and tee nuts
- Disassembled test frame for reassembly to new specs

### 2021-07-29

- Designed Y endstop switch mount
- Lots of small polishing
- Added alignment piece for the stepper mounts
- Preformatted brackets added
- Alignment spacer for the Y axis crossbars added
- Completed frame, working on inserting all brackets and fasteners

### 2021-07-28

- Endstop switch work

### 2021-07-27

- Second pass at back piece, adjusted hole sizes for standoffs
- Initial X endstop design. Wrong way; flipped to home to the right.
- Mounted hotend gantry test.

### 2021-07-26

- Fusion is crashing again/still.
- Started hotend gantry design
- Assembles in three main pieces, finished the MGN12H carriage section in the middle.
- First pass at back piece for belt mounting.

### 2021-07-25

- Finished up V1 of the bed, still needs polish
- Now have a mount for leadscrews.
- Redesigning the jigs for the Z axis to be slightly narrower.

### 2021-07-24

- Started designing bed
- Got initial size in place, 510mm x 260mm for frame, re-using Z axis struts that are going to be widened.

### 2021-07-23

- Z Axis needs to be setup *first* or it's going to be difficult.
- Strugged with Z axis all day.

### 2021-07-22

- Fusion crapped itself. Again.
- Looking in to endstop positioning. 
- Will home to the front-right, so considering that aspect.
- Designed jig for Z axis
- Steppers will all have 2mm or 3mm thick covers on the their mounting plates to hold the 35 metal spacers in place and add additional spacing for the 45mm screws.
- 35mm spacer + 3mm plate + 3mm printed spacer = 41mm, leaving 4mm to screw in to the stepperi

### 2021-07-21

- Printed and finished linear rail stops
- Adjusted height of tensioners (off by 5mm)
- Tested XY kinematics
- Started design of Z axis 

### 2021-07-20

- Assembled full belt system
- Designed gantry lock for servicing belts and hotend
- Designed end stops for X and Y axis linear rails

### 2021-07-19

- Worked on belt system
- Printed various tensioner iterations
- Assembled working right tensioner and installed one belt.
- Adjusted wall thicknesses & offsets for tensioner. Fixed a few issues and tested a lot of bad ideas.
- Tensioner now acts as endstop for Y axis linear rails on the front side.

### 2021-07-18

- Moved out extrusions in the X axis. Ideally will resolve spacing and alignment with shorter X axis rail or 60mm wide front extrusions connecting the interior and exterior frames.
- Tweaked and assembled right Y gantry.
- Moved Y axis rails backwards to add more room for hotend.

### 2021-07-17

- Finished stepper pulley/rear idlers component.
- Assembled stepper pulley/idler blocks.
- Continued work on Y gantry.
- Finished printing Mk2 of the Y gantry. No major snags.
- Mk1 belt tensioner designed
- Began tensioner printing