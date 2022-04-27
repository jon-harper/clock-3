---
title: Linear Rail Installation
summary: Instructions on initial installation of the linear rails.
authors: Jon Harper
date: 2022-04-07
---

*This document is actively being refined and edited for mistaeks.*

## 1. Secure The Carriages

You'll need a few rubber bands, zip ties, or some other method of temporarily securing the carriages of your linear rails. Whatever your use, the carriage should remain in place.

!!! note
    Later you will remove the rubber bumpers that keep the carriage on. This method will be the only thing keeping your carriage on the rail.

## 2. Check Rail Flatness

Cheap linear rails often come slightly bowed, like so:

![Not a flat rail](../../img/rail_install/not_flat.jpg)

This isn't indicative of quality, but it doesn't make the rail useless. With slight pressure:

![A rail pressed lightly](../../img/rail_install/forced_flat.jpg)

A determination still has to be made for each rail, however.

1. Set each rail side by side.
2. Sort them by how bowed them are.
3. Check for any pits, dings, rust, or other damage.
4. The flattest rail should be reserved for your X axis.
5. The next best two use for the Y axis.
6. Remaining rails that are usable will be used for the Z axis.

!!! Important
    Replace any rails that are excessively bowed and cannot be "pressed flat" easily, like above. Likewise, any rails with clear damage that will impact carriage motion should be replaced.

## 3. Lubricating Rails and Carriages

### Directions

Linear rails ship with some form of protective grease. We not only need to remove that grease, we need to reapply our own lubricant.

RatRig produced two excellent guides for cleaning and lubricating linear rails:

- [Beginner Linear Rail Maintence](https://ratrig.dozuki.com/Guide/02.+%5BBeginner%5D+Linear+rail+maintenance+guide+without+disassembly/9?lang=en)
- [Intermediate Linear Rail Maintenance](https://ratrig.dozuki.com/Guide/03.+%5BIntermediate%5D+Linear+rail+maintenance+guide+with+disassembly/10)

The difference between the two guides is that in the second, the carriage is removed from the rail. This is the suggested method of lubricating your rail, but also runs the risk of the carriage bearings coming free. Use caution.

!!! note
    If you are using grease, you will need to remove the carriage for application.

### Reference

- [Bearing lubricant: Choosing between grease and oil](https://www.linearmotiontips.com/lubrication-grease-or-oil/) from Linear Motion Tips
- [What should be used to lubricate linear bearings and how often should they be lubricated?](https://www.thomsonlinear.com/en/support/tips/what-should-be-used-to-lubricate-linear-bearings) from Thomson Linear Motion
- [HIWIN Lubrication Manual](https://hiwin.us/wp-content/uploads/lubricating_instructions.pdf)

## 4. Installing Your Rails

### Part List

| ID    | Qty | Description |
|-------|-----|-------------|
| A1    | 1   | 2020 Extrusion, 540mm, Milled |
| A2    | 1   | 2020 Extrusion, 540mm, Milled |
| A3    | 1   | 2020 Extrusion, 440mm, Milled |
| Z1    | 1   | 2020 Extrusion, 510mm |
| Z2    | 1   | 2020 Extrusion, 510mm |
| PN501 | 80  | Screw, M3-0.5 x 8mm SHCS |
| PN576 | 80  | Tee Nut, 6mm Slot, M3, Slide In |
| PN631 | 5   | Linear Rail, MGN12, 400mm |
| PN632 | 5   | Linear Rail Carriage, MGN12H |
| PNXXX | 10  | Linear Rail Alignment Clamps |

### A. Basic Steps

| Step | Example |
|------|---------|
| Insert a tee nut in the channel | ![Step 1](../../img/rail_install/step1.jpg) |
| Use the screw hole as a peephole to guide the rail over the nut | ![Step 2](../../img/rail_install/step2.jpg) |
| Drop an M3 x 8mm screw in place | ![Step 3](../../img/rail_install/step3.jpg) |
| Rotate the screw to level with the linear rail. Do not tighten fully. | ![Step 4](../../img/rail_install/step4.jpg) |
| Slide in the next tee nut and move the rail fowards. This is easier when one hand is not taking a picture. | ![Step 5](../../img/rail_install/step5.jpg) |
| Drop in a screw and secure | ![Step 6](../../img/rail_install/step6.jpg) |
| Don't overtighten; slide forward | ![Step 6](../../img/rail_install/step7.jpg) |

### B. Rescuing Lost Screws

| Problem | Example |
|---|---|
| If a screw misses a tee nut and falls in, back out the rail until you can "pop" the screw up with your finger. | ![Screw misses the tee nut](../../img/rail_install/oops1.jpg)
| Use an allen wrench to re-align the rail with the tee nut | ![Hunting for nuts](../../img/rail_install/oops2.jpg)
| Add another screw and secure | ![Adding another screw](../../img/rail_install/oops3.jpg)
| Fixed! | ![Three completed fasteners](../../img/rail_install/finished.jpg)

### C. Finishing

| Step | Example |
|------|---------|
| Continue adding nuts and screws until all 16 are populated. At some point, you'll need to secure the carriage around both the rail and extrusion. | ![finished rails](../../img/rail_install/finishing1.jpg) |
| Add rail alignment clamps to keep the rail in place. Leave the rubber band on to keep the carriage from sliding too much. | ![finished rails](../../img/rail_install/finishing2.jpg) |

