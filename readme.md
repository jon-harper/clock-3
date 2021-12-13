# Clock 3

Clock 3 is a working name for this project and is not final. It is an evolution of my second attempt at an enclosed 3D printer. The idea of building my own 3D printer to suit my needs came out of excess free time during the 2021 Winter Storm. Clock 1 was a thought experiment; Clock 2 I built. Clock 3 is a refinement incorporating lessons from other projects and a lot of experimentation.

## Design Goals

- Use a maximum number of off-the-shelf components
- Design parametrically to allow for flexible build volumes
- Active chamber temperature control
- Dual filters for recirculated and vented air
- Design components to be serviceable and accessible
- Minimize the number of fastener types and sizes and keep components easily-sourced
- Require a minimum of custom-fabricated components
- Design for ease of assembly and simple cable management
- Documentation!

## Specifications

- V6 hotend
- 300x300x350mm build volume
- Dual independant Z with auto-leveling
- CoreXY kinematics
- Fully enclosed
- HEPA and activated carbon filtration
- External steppers and electronics to allow higher internal temperatures without affecting temperature-sensitive components
- 12V RGB LED lighting
- Spring steel magnetic bed

# Organization

This is the Clock 3 branch. It contains all data needed to build a Clock 3 printer aside from some tools common to all projects. These tools can be found in the `master` branch.

## Naming Scheme

### STL Files

STLs are numbered sequentially to help with assembly. The number of each component is printed discreetly on each piece so that it is either concealed or very hard to see after installation. Each *component* falls into one of several *categories* and is identified by either its name or location. Components that come in left and right versions have *chirality*.

The printed text on each component also include an L or R for chiral components to help with identification. Some miscellanious and very basic parts lack numbers due to size or geometry constraints.

You can find all of the step files in the [STL](STL/) folder, and the list of [part codes here](docs/Part Codes.md).

## Tools

There are a number of tools to help determine parametric details, such as your ideal M5 screw hole size or the proper hole size for your brand of brass inserts. These can be found in the `Tools` folder and are meant to be printed. The results can be fed back in to the Fusion model and then exported for printing. *Exported STL files will come with default tolerances and may not fit.*