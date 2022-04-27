---
title: Decision Guide
summary: A guide for deciding on variations of the stock Clock 3 printer.
authors: Jon Harper
date: 2022-04-05
---

*This document is actively being refined and edited for mistaeks.*

Clock 3 is still a prototype, so a wide variety of possible configurations have not yet been tested. There is still room for flexibility, however.

## Hotend

The initial prototype is being tested with two hotends: an E3D V6 and a "Haldis Red Lizard" (Phaetus Dragonfly clone). Any V6-compatible hotend with the same heatsink height should work, as long as the width of the heatsink fits within the mount.

## Direct Drive (v. Bowden)

Direct drive with a BMG extruder is currently the only supported configuration. Adding a Bowden configuration is planned, as are other extruders. This section is a placeholder until then.

## Door and Frame

### Door Assembly

MISUMI sells [complete door kits](https://us.misumi-ec.com/vona2/detail/110302284740/). We take a modular approach and buy the parts individually, but some may find a kit appealing. Note that one can purchase this door kit with or without an interior panel. These kits are composed of the following part numbers:

| Part Number | Description                   | MISUMI PN              |
|-------------|-------------------------------|------------------------|
| PN553       | Screw, M5-0.8 x 16mm SHCS     | SCB5-16                |
| PN710       | Corner Bracket, Door Frame    | HBLTC5                 |
| PN713       | 2020 Door Panel Gasket, 564mm | HFSSK3-2000            |
| PN714       | 2020 Door Panel Gasket, 646mm | HFSSK3-2000            |
| PN751       | 2020 Door Extrusion, 564mm    | HFTF5-2020-564-TPW     |
| PN752       | 2020 Door Extrusion, 646mm    | HFTF5-2020-646-TPW     |
| PN760       | Acrylic Sheet, 577x659x3mm    | (included in kit only) |

!!! note
    If you buy the interior panel from MISUMI instead of locally sourcing, shipping costs increase. Adding a panel to a kit only increases the price a few dollars but *may* increase shipping costs more.

Additionally, a 90mm handle ships with the kit. It is not very comfortable and the screw holes are wrong for the outer panel; use the printed handle instead.

If you have M5x16 SHCS on hand already and are having both panels made separately, buying the rest of the parts individually is more cost-effective.

### Windows

#### Acrylic

We use 3mm acrylic. If using 5mm **inner** window panels, change `HFSSK3-2000` to [`HFSSK5-2000`](https://us.misumi-ec.com/vona2/detail/110302375310/?ProductCode=HFSSK5-2000) when sourcing for the door panel gasket.

It is possible to use a 5mm **outer** window panel, but this will require changes to the gasketing behind the door.

!!! note
    At present, we know of no other supplier than MISUMI for this panel mounting gasket. Please notify us if another supplier is found.

#### Polycarbonate (PC)

Switching to PC for the inner panel is a more expensive option. There is no issue with using PC, nor are adjustments required. This can be done relatively affordably for the inner panel by buying a kit.

### Wooden Panels

These will need to be locally fabricated. The wooden panels are 6mm and 12mm thick; approximately the same values in SAE plywood measurements will work with some adjustment. 

- 12mm panels: 15/32" is preferable 
- 6mm panels: Should be thicker, if possible 5/16".

### Insulation

Polyisocyanurate foam is an excellent insulator with superior qualities to polystyrene (Styrofoam) and comparable price. The default thickness all around is 1/2", but this can be increased as desired to better control chamber temperatures.

- Top insulation: up to 1" thick.
- Floor insulation: up to 3/4" thick (will need to be tested).
- Side insulation: up to 1" thick.
- Rear insulation: up to 3/4" thick; additional can be added with some adjustments.

## Electrical

There are an incredible number of different approaches to wiring. While lever nuts can be used, we prefer a connector-based approach for robustness and space considerations. Where possible, any changes to wiring will only impact the Materials list and wiring panel mounts. The panel mounts only connect parts above the flooring, so using lever nuts solely for undercarriage connections is very easily doable.

### Lever Nuts

The front-to-back Z crossbars are ideal mounting positions for lever nuts. In the future, a part holder for this purpose may be added; for now, you can find lots of examples on CAD and STL sharing sites.

### Cable Raceways/Wire Channels

These have not been tested. Mounting the raceways might require additional parts beyond the raceways themselves.

