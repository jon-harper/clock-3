---
title: Development Goals
summary: Goals and purpose for the Clock 3 project.
authors: Jon Harper
date: 2022-04-11
---

This page is a list of major designs goals behind Clock 3 and their implementation.

## Ease of Sourcing

- Use off-the-shelf components where possible:
    - 400mm linear rails and 500mm lead screws were chosen for ready availability.
    - JST-SM connectors are used for low-current connections.
    - Limit switches are Makerbot/Creality-type.
    - Heated bed is a stock Creality CR-10 bed (310mmx310mm).
    - Heater cartridge connectors are compatible with E3D V6 cartridges.
- Minimize the number of fastener types:
    - Fasteners are M3 button head or M5 socket head cap screws.
    - Minor exceptions are all readily available and small in number.
    - Care is taken to avoid adding new fastener lengths or types unless necessary.
- Custom-fabricated components are few and easily sourced:
    - Panels have a minimal number of holes and cuts.
    - Vector paths for laser cuts are provided.
    - Floor panels have gaps with printed cutouts for wiring passthrough. Wiring is then connected to a concealed panel mount underneath the flooring.
    - Frame relies on perpendicular braces, largely avoiding tapped ends. Blind joints or counterbored and tapped holes are completely unused.

## Ease of Access, Service, and Modification

- Designed for ease of assembly and simple cable management:
    - Parts have printed ID numbers to help identification.
    - Left- and right-handed parts are notated with a printed `L` or `R`, as well.
    - Many printed components integral zip tie anchors and cable guides.
- Components are made to be serviceable and accessible:
    - Disassembly of most kinematic components does not require other components to be disassembled first.
    - A gantry lock design is included to keep the gantry in place and square during belt servicing.
- Side and rear panels unscrew and take the insulation with them:
    - Components and cabling are almost entirely separated, i.e. electrical components can be unplugged from a harness.
    - Easy, direct access to electronics through two individually-removeable floor panels.
    - Side panels use drop-in tee nuts for quick removal and reattachment.

## Flexibility, Safety, and Stability

- Designed parametrically for flexible build parameters:
    - The core Fusion 360 file can be adjusted for different print tolerances.
    - Build volume can be scaled up (capability is maintained, but this is not actively developed yet).
    - Different types and depths of heated inserts can be used; likewise, adjustments can be made for different print tolerances.
    - NOTE: The pace of development occured technical debt in this area. V0.8/v0.9 (after completed documentation) will involve a significant rework of the Fusion 360 model.
- Built in air filtration and ambient temperature control:
    - Dual fans for recirculated and vented air, fed through both activated carbon and HEPA filters.
    - Filtration system is in steady production use.
    - Use of polyisocyanurate (PIR) foam insulation allows for steady chamber temperatures with only air exhaust for cooling.
- Documentation:
    - Full bill of materials, split into a shopping list (to be purchased) and assembly list (finished parts for assembly)
    - Component-by-component, step-by-step assembly instructions on this site.
    - Open development on [github](https://github.com/jon-harper/clock-3).
    