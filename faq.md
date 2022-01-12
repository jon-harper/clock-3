# Frequently Asked Questions

## General

### Why another 3D printer?

### Can I get a kit from somewhere?

### Can you build one for me?

---

## Conceptual

### Why so many lock washers?

### Why a V6 hotend instead of [x]?

Several reasons:

- V6 clones are readily available and generally only differ in length with respect to compatibility
- the mount interface can be reused for other hotends that are "J-head" style, like the newer Dragon hotends.

### Why does the Z axis not have a third driver?

That's on the todo list for the future. Given time and cost constraints, two steppers has to do for now. With silicone columns and a BLTouch for assisted leveling, it's less a problem than an "nice to have".

### Why not a larger build volume?

- Overall increase in cost
- Power usage scales nonlinearly, as bed volume scales quadratically and chamber volume cubically.
- CR-10 build plates are cheap and readily available. 350mm build plates are harder to come by.

### Why don't you use M4 screws?

To keep the number and type of screws down further. Keeping to M3 and M5 screws helps ensure that 

---

## Materials and Sourcing

### Do I have to use the same brands for materials (e.g. Misumi)?

### There is a really good supplier that sells custom [x]. Why don't you use their product?

### Can I use Neopixels (WS2812B, 5V) instead of WS2815 (12V)?

Yes. You can even use a different driver, like APA102, as long as it uses no more than 4 wires (VCC, GND, and one or two data). The SP901E is a data repeater and compatible across a range of voltages. That said, you may see a small difference in lighting quality with a 5V LED string like the Neopixel due to voltage drop.
