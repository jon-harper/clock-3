# Clock 3

![Cover photo of hotend](/Media/Photos/2021-12/20211223_cover.jpg)

This is the evolution of the concept of an enclosed 3D printer with externally mounted steppers. The idea of building my own 3D printer to suit my needs came out of excess free time during the 2021 Winter Storm.

Clock 1 was a thought experiment to enclose an Ender 5-like Cartesian printer. Clock 2 was a from-scratch CoreXY printer that I largely built before acquiring the ability to safely print ABS.

Clock 3 is a complete redesign incorporating most of the common, off-the-shelf components from Clock 2. It incorporates lessons from repeated assembly/disassembly of Clock 2, successful concepts from other projects, and a lot of experimentation with ABS in an enclosure. Clock 3 is a working name for this project and is not final.

## First, a Note

This project is very much under active development, [**first printing on 12/21/2021**](/Media/Cropped/20211221_Hotend.jpg). All renders and quite a few photos will be stored here, but you can also follow along visually with assembly and discussion on Instagram [@jonspaceharper](https://www.instagram.com/jonspaceharper/).

Compilation of assembly and maintenance documentation will start in January of 2022 after a full Bill of Materials is available (i.e. the initial prototype is finished).

## Development Goals

- Maximize the number of off-the-shelf components
  - 400mm linear rails and 500mm lead screws were chosen for ready availability.
  - JST-SM and JST-XH connectors are used for wide availability and compatibility
  - Limit switches are the Makerbot/Creality design rather than custom.
- Design parametrically to allow for flexible build parameters
  - The core Fusion 360 file can be adjusted for different material shrink tolerances.
  - Build volume can be scaled up (cabability is maintained, but this is not actively developed yet).
  - Different typed and depths of heated inserts can be used, though using the really cheap ones instead of knurled is not recommended.
- Design for ease of assembly and simple cable management
  - Parts have printed ID numbers to keep tracking simple.
  - Left- and right-handed parts are notated with a printed 'L' or 'R', as well.
  - Printed components have zip tie anchors and cable guides.
- Components are made to be serviceable and accessible
  - Disassembly of most components does not require other components to be disassembled first.
  - A gantry lock design is included to keep the gantry in place and square when working on belts.
  - Side and rear panels unscrew and take the insulation and inner panel with them.
- Minimize the number of fastener types and sizes and keep components easily-sourced
  - Fasteners are all M3 or M5.
  - M5 fasteners are all button head cap screws (BHCS) and all M3 are socket head cap screws (SHCS).
  - Early designs used all SHCS, even for M5, but this is being eliminated for button head.
- Require a minimum of custom-fabricated components with minimal cutting.
  - ABS panels are uniform in thickness and have as few cutouts are possible.
  - Floor panels use cutouts for printed panels instead of direct panel mounts.
  - Frame relies on perpendicular braces instead of tapped ends and either blind joints or counterbored and tapped holes.
- Air filtration and temperature control
  - Active chamber temperature control (*to come*)
  - Dual filters and fans for recirculated and vented air (*to come*)
- Documentation
  - Full [changelog](changelog.md)
  - Component-by-component, step-by-step assembly instructions (*in progress*)
  - Open development on Github

## Key Specifications

- 300x300x350mm build volume
- Dual independant Z with auto-leveling
- CoreXY kinematics
- V6, 300C hotend
- Direct drive or Bowden feed BMG
- Fully enclosed
  - Simple side and rear panel removal
  - Large, clear front door with inset frame
- HEPA and activated carbon filtration
  - Continuous interior filtration
  - Filtered ventilation
- External steppers and electronics (exluding direct drive extruder)
- 12V RGB LED lighting (WS2815 preferred, any SPI addressible strip will work)
- Spring steel magnetic bed
- Multiple ABL options, initially BLTouch

# Organization

## Naming Scheme

### STL Files

STLs are numbered sequentially to help with assembly. The number of each component is printed discreetly on each piece so that it is either concealed or very hard to see after installation. Each *component* falls into one of several *categories* and is identified by either its name or location. Components that come in left and right versions have *chirality*.

The printed text on each component also include an L or R for chiral components to help with identification. Some miscellanious and very basic parts lack numbers due to size or geometry constraints.

Example: `01 - XY - Pulleys - L Bottom.stl`

You can find all of the printable files in the [STL](STL/) folder along with a list of [part codes](Docs/Part%20Codes.md).

## Component Labeling

What one board labels as "THB" another may label as "TB". Likewise, endstop/limit switch connector abbreviations (and pin order!) are not standard, inasmuch as anything in 3D printing is standardized. To that end, a single nomenclature is adopted for part labels. Each connector has a two- or three-letter code for labeling panels and wiring. Your actual wiring may use a different system, but printed parts with labels follow this pattern. It is recommended for continuity with printed parts and documentation to use the same. The full part list may be found in the [`Docs`](Docs/) folder.

## Tools

There are a number of tools to help determine parametric details, such as your ideal M5 screw hole size or the proper hole size for your brand of brass inserts. These can be found in the `Tools` folder and are meant to be printed. The results can be fed back in to the Fusion model and then exported for printing. Stock exported STL files will come with default tolerances and may not fit as precisely.
