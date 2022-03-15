# Clock 3

![Cover photo of hotend](/Media/Photos/2021-12/20211223_cover.jpg)

This is the evolution of the concept of a fully-enclosed 3D printer with externally mounted steppers. The idea of building an enclosed 3D printer to suit my specific needs came out of excess free time during the 2021 Winter Storm.

Clock 1 was a thought experiment to enclose an Ender 5-like Cartesian printer. Clock 2 was a from-scratch CoreXY printer that I largely built before acquiring the ability to safely print ABS.

Clock 3 is a complete redesign incorporating most of the common, off-the-shelf components from Clock 2. It incorporates lessons from repeated assembly/disassembly of Clock 2, successful concepts from other projects, and a lot of experimentation with ABS in an enclosure. Clock 3 is a working name for this project and is not final.

## Status

You can find the changelog in its entirety in the [changelog.md](changelog.md) file, while the [Issues](/issues) page is a good place to see what's in progress.

### 2022-03-14

The delay in issuing a preliminary BOM is in developing a Python script to scrape the model for part counts. The basic script works, but I'm working on expanding it to draw in a source file and append the counts to it. This will make issuing new BOMs take seconds, but time up front is needed.

## Notes

- Klipper firmware for Clock 3 is available [here](../clock3-klipper).
- The Clock Face project is [here](../clock-face), which revises the physical display and menu system for Klipper.
- This project is very much under active development, [**first printing on 12/21/2021**](/Media/Cropped/20211221_Hotend.jpg).
- All renders and quite a few photos are stored in this repository, but you can also follow along visually with assembly and discussion on Instagram [@jonspaceharper](https://www.instagram.com/jonspaceharper/).
- A heat set insert press (or a steady hand with a soldering iron) is strongly recommended.

## Development Goals

- Maximize the number of off-the-shelf components
  - 400mm linear rails and 500mm lead screws were chosen for ready availability.
  - JST-SM connectors are used for nearly all connections.
  - Limit switches are the Makerbot/Creality style.
  - Heated bed is a stock replacement Creality CR-10 bed (310x310mm).
- Design parametrically to allow for flexible build parameters
  - The core Fusion 360 file can be adjusted for different tolerances.
  - Build volume can be scaled up (capability is maintained, but this is not actively developed yet).
  - Different typed and depths of heated inserts can be used; likewise, adjustments can be made for different print tolerances.
- Design for ease of assembly and simple cable management
  - Parts have printed ID numbers to help identification.
  - Left- and right-handed parts are notated with a printed 'L' or 'R', as well.
  - Many printed components have zip tie anchors and cable guides.
- Components are made to be serviceable and accessible
  - Disassembly of most components does not require other components to be disassembled first.
  - A gantry lock design is included to keep the gantry in place and square when working on belts.
  - Side and rear panels unscrew and take the insulation with them.
  - Components and cabling are almost entirely separated, i.e. electrical components can be unplugged from a harness.
  - Easy, direct access to electronics through two individually-removeable floor panels.
- Minimize the number of fastener types and sizes and keep components easily-sourced
  - Fasteners are (with minimal exception) M3 button head or M5 socket head cap screws.
  - Minor exceptions are all readily available and small in number.
  - Care is taken to avoid adding new fastener lengths or types.
- Require a minimum of custom-fabricated components with emphasis on reducing the number of cuts.
  - Panels are have as few cutouts are possible.
  - Floor panels use holes to pass through wiring to printed panels underneath instead of individual cutouts.
  - Frame relies on perpendicular braces, largely avoiding instead tapped ends. Blind joints or counterbored and tapped holes are completely unused.
- Air filtration and temperature control
  - Active chamber temperature control
  - Dual fans for recirculated and vented air, fed through both activated carbon and HEPA (completed February 2022)
- Documentation
  - Full [changelog](changelog.md)
  - Full bill of materials (*verification in progress*)
  - Component-by-component, step-by-step assembly instructions (*in progress*)
  - Open development on Github

## Key Specifications

- 300x300x350mm build volume
- Dual independant Z axes with auto-leveling
- CoreXY kinematics
- V6, 300C hotend with the ability to support others
- Direct drive or Bowden feed (currently only configured for direct drive with a BMG)
- Fully enclosed
  - Simple side and rear panel removal
  - Large, clear front door with inset frame
- HEPA and activated carbon filtration
  - Continuous interior filtration through AC and HEPA
  - Filtered ventilation
- Temperature controlled chamber
  - Filtration exhaust speed is temperature-controlled
  - Exhaust fan can be set to run at low speed continuously for negative internal pressure
- External steppers and electronics (exluding direct drive extruder)
- 12V RGB LED lighting (WS2815 preferred, any 3- or 4-wire addressible strip will work)
- Spring steel magnetic bed
- Generic ABL mount point, initially with BLTouch support
- Panel mounted connectors for Raspberry Pi (USB, Ethernet, HDMI) and SD card port for flashing the MCU.

## Media

Head to the [Media](/Media) folder for renders and photos of the prototype.

# Organization

## Naming Scheme

### STL Files

STLs are numbered sequentially to help with assembly. The number of each component is printed discreetly on each piece so that it is either concealed or very hard to see after installation. Each *component* falls into one of several *categories* and is identified by either its name or location. Components that come in left and right versions have *chirality*.

The printed text on each component also include an L or R for chiral components to help with identification. Some miscellanious and very basic parts lack numbers due to size or geometry constraints.

Example: `01 - XY - Pulleys - L Bottom.stl`

You can find all of the printable files in the [STL](STL/) folder along with a list of [part codes](Docs/Part%20Codes.md).

### Component Labeling

What one board labels as "THB" another may label as "TB". Likewise, endstop/limit switch connector abbreviations (and pin order!) are not standard, inasmuch as anything in 3D printing is standardized. To that end, a single nomenclature is adopted for part labels. Each connector has a two- or three-letter code for labeling panels and wiring. Your actual wiring may use a different system, but printed parts with labels follow this pattern. It is recommended for continuity with printed parts and documentation to use the same. The full part list may be found in the [`Docs`](Docs/) folder.

## Misc.

There are a number of tools to help determine parametric details such as the ideal M5 screw hole size or the proper hole size for your brand of brass inserts. These can be found in the `STL/Tools` folder and are meant to be printed. The results can be fed back in to the Fusion model and then exported for printing. Stock exported STL files will come with default tolerances and may not fit as precisely.

There is also a `CAD/Tools` folder with parametric tools such as an LED channel. 