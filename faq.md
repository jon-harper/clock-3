# Frequently Asked Questions

## General

### Why another 3D printer?

TODO

This is a longer story that I'd like to get right.

### Can I get a kit from somewhere?

That would be super cool, but not at the moment.

### Can you build one for me?

No, but a Bill of Materials is coming soon (as of February 2022).

### Will you come work for my company?

Hey, that's a cool idea. Reach out and we'll find out.

---

## Conceptual

### Why so many lock washers?

A bag of 500 lock washers costs not much more than 100. A builder will need more than 100 lock washers no matter what I do, so I standardized on M5x12mm + lock washer + nut for most printed parts where it is reasonable to do so. There are a few exceptions to the rule that neither need nor have lock washers, like the outside corner pieces on the frame.

Also, Loctite eats ABS if it's not completely dry. I'm not that patient.

### Why a V6 hotend instead of [x]?

Several reasons:

- V6 clones are readily available and generally only differ in length with respect to compatibility
- the mount interface can be reused for other hotends that are "J-head" style, like the newer Dragon hotends.

### Why does the Z axis not have a third driver?

That's on the todo list for the future. Given time and cost constraints, two steppers has to do for now. With silicone columns and a BLTouch for assisted leveling, it's less a problem than an "nice to have".

### Why not a larger build volume?

I strongly considered this, but settled on the Creality CR-10 form factor. Going larger starts becoming quite troublesome:

- Overall increase in cost beyond 310x310
- Power usage scales nonlinearly, as bed volume scales quadratically and chamber volume cubically.
- CR-10 build plates are cheap and readily available. 350mm build plates (and larger) are harder to come by.

The Z volume is limited somewhat by the stepper being placed outside of the chamber. This necessarily sacrifices about 150mm of thread, and a 500mm lead screw is already hard enough to get aligned.

### Why don't you use M4 screws?

To keep the number and type of screws down. This project is made entirely of M3 and M5 screws.

---

## Materials and Sourcing

### Do I have to use the same brands for materials (e.g. Misumi)?

Most of the printer is substitutable with OEM materials. Although initial support is only provided for the BIGTREETECH Octopus MCU, a FYSETC S6 or Spider would theoretically work just as well. The only part that can't be substituted without major work is the Raspberry Pi.

### There is a really good supplier that sells custom [x]. Why don't you use their product?

I'm avoiding single-source parts, Raspberry Pi notwithstanding. Ideally this will keep the cost down as well as prevent supply and sourcing issues.

### Can I use Neopixels (WS2812B, 5V) instead of WS2815 (12V)?

Yes. You can even use a different driver, like APA102, as long as it uses no more than 4 wires (VCC, GND, and one or two data). The SP901E is a data repeater and compatible across a range of voltages. That said, you may see a small difference in lighting quality with a 5V LED string like the Neopixel due to voltage drop.
