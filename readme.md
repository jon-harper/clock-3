# Clock 3


| First Print | Completed Panels |
|---|---|
| [![Cover photo of hotend](/Media/Photos/2021-12/20211223_cover.jpg)](/Media/Photos/2021-12/20211223_cover.jpg) | [![Cover photo with door open](/Media/Photos/2022-04-15_door_open.jpg)](/Media/Photos/2022-04/2022-04-15_door_open.jpg) |

This is the evolution of the concept of a fully-enclosed 3D printer with externally mounted steppers. The idea of building an enclosed 3D printer to suit my specific needs came out of excess free time during the 2021 Winter Storm.

Clock 1 was a thought experiment to enclose an Ender 5-like Cartesian printer. Clock 2 was a from-scratch CoreXY printer that I largely built before acquiring the ability to safely print ABS.

Clock 3 is a complete redesign incorporating most of the common, off-the-shelf components from Clock 2. It incorporates lessons from repeated assembly/disassembly of Clock 2, successful concepts from other projects, and a lot of experimentation with ABS in an enclosure. Clock 3 is a working name for this project and is not final.

## Status

You can find the changelog in its entirety in the [changelog.md](changelog.md) file. Documentation is ongoing and active at [jon-harper.github.io/clock3-docs](https://jon-harper.github.io/clock3-docs/).

### 2022-04-15

The finished wooden and acrylic paneling is in place and fits. Continued testing of the prototype is is centered around documenting assembly currently, with concurrent testing of the hotend assembly on a modified Ender 5.

### 2022-03-31

The preliminary [Bill of Materials](/BOM/bill_of_materials.xlsx) is done. This will eventually be a Markdown file and a CSV file, but the frequency of edits makes an Excel document easier at present. Documentation is in progress and will be published here as it progresses.

## Notes

- Klipper firmware for Clock 3 is available [here](../clock3-klipper).
- The Clock Face project is [here](../clock-face), which revises the physical display and menu system for Klipper.
- The Fusion 360 model is not published yet, but you can find the project's Python scripts [here](../Clock3Scripts)
- This project is very much under active development, [**first printing on 12/21/2021**](/Media/Cropped/20211221_Hotend.jpg).
- All renders and quite a few photos are stored in this repository, but you can also follow along visually with assembly and discussion on Instagram [@jonspaceharper](https://www.instagram.com/jonspaceharper/).
- A heat set insert press (or a steady hand with a soldering iron) is strongly recommended.

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
