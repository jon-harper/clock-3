---
title: Development Goals
summary: Goals and purpose for the Clock 3 project.
authors: Jon Harper
date: 2022-04-11
---

This page is a list of major designs goals behind Clock 3 and their implementation.

## Ease of Sourcing

- Use off-the-shelf components where possible.
    - 400mm linear rails and 500mm lead screws were chosen for ready availability.
    - JST-SM connectors are used for all intermediate, low-amperage connections.
    - Limit switches are the Makerbot/Creality style.
    - Heated bed is a stock replacement Creality CR-10 bed (310x310mm).
    - Heater cartridges are tailed with Micro Fit 3.0 connectors, which are used on E3D V6-compatible cartridges.
- Minimize the number of fastener types.
    - Fasteners are (with minimal exception) M3 button head or M5 socket head cap screws.
    - Minor exceptions are all readily available and small in number.
    - Care is taken to avoid adding new fastener lengths or types unless necessary.
- Custom-fabricated components are few and easily sourced.
    - Panels have as few cutouts are possible and are easily laser-cut.
    - Vector paths for laser cuts are provided.
    - Floor panels have gaps with filled by printed cutouts for wiring passthrough. Wiring is instead connected to a printed panel mount underneath the flooring.
    - Frame relies on perpendicular braces, largely avoiding tapped ends. Blind joints or counterbored and tapped holes are completely unused.

## Ease of Access, Service, and Modification

- Design for ease of assembly and simple cable management.
    - Parts have printed ID numbers to help identification.
    - Left- and right-handed parts are notated with a printed 'L' or 'R', as well.
    - Many printed components have zip tie anchors and cable guides.
- Components are made to be serviceable and accessible.
    - Disassembly of most components does not require other components to be disassembled first.
    - A gantry lock design is included to keep the gantry in place and square when working on belts.
  - Side and rear panels unscrew and take the insulation with them.
    - Components and cabling are almost entirely separated, i.e. electrical components can be unplugged from a harness.
    - Easy, direct access to electronics through two individually-removeable floor panels.
    - Side panels use drop-in tee nuts for quick removal and reattachment.

## Flexibility, Safety, and Stability

- Design parametrically to allow for flexible build parameters.
    - The core Fusion 360 file can be adjusted for different print tolerances.
    - Build volume can be scaled up (capability is maintained, but this is not actively developed yet).
    - Different types and depths of heated inserts can be used; likewise, adjustments can be made for different print tolerances.
    - NOTE: The pace of development occured technical debt in this area. V0.8/v0.9 (after completed documentation) will involve a significant rework of the Fusion 360 model.
- Build in air filtration and ambient temperature control.
    - Dual fans for recirculated and vented air, fed through both activated carbon and HEPA.
    - Filtration system is in steady production use.
    - Heavy use of insulation allows for high chamber temperatures with only air exhaust for cooling.
- Document everything.
    - Full bill of materials, split into a shopping list (to be purchased) and assembly list (finished parts for assembly)
    - Component-by-component, step-by-step assembly instructions on this site.
    - Open development on [github](https://github.com/jon-harper/clock-3).
    