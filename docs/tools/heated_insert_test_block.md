# Heated Insert Parameter Testing Tool

## What to Print

You will need to do the test process twice, once printed flat and once vertically. The file needed is `M3 Het Set Insert Parameter Block.stl` file in the `/STL/Tools` subdirectory.

## Hole Sizes

Below are the sizes and taper angles of each position on the test block.

| Diameter | Taper 0 | Taper 1 | Taper 2 | Taper 3 | Taper 4 | Taper 5 |
| :---:    | :---:   | :---:   | :---:   | :---:   | :---:   | :---:   |
| 4.35     | 0       | -2      | -4      |  X      |  X      |  X      |
| 4.50     | 0       | -2      | -4      | -6      |  X      |  X      |
| 4.65     | 0       | -2      | -4      | -6      | -8      |  X      |
| 4.80     | X       | -2      | -4      | -6      | -8      | -10     |
| 4.95     | X       |  X      | -4      | -6      | -8      | -10     |

## Using the Test Blocks

Start with the top three insert holes. Press the inserts (preferably with a insert press) and note the characteristics:

1. How readily the insert drops in: is there resistance? Does it seems to just fall right in without grabbing the plastic? There should be some resistance, but too much will cause plastic to bubble up inside the threads.
2. The resulting plastic around the insert: does it raise at all above the insert? Is there a clear gap around the knurls? Is there a smooth transition between the plastic around the knurls and the untouched plastic? You're looking for the last of the three.
3. The bottom of the insert: is it smooth? Did any plastic seep up from underneath? Too high signals your insert is not fully seated. Too low is caused by plastic coming up underneath the insert.

Using the following three checks, move down and to the right, noting which insert "feels" right in each row (not too much pressure, not too little). If a taper of doesn't work for one row, don't re-use it for the next row. Keep moving down and to the right.

Your finished product should look something like [this picture](../Media/). Note that an insert was plucked out (with tweezers!) before being fully inserted. If you feel too much resistance with insertion or generally feel it's the wrong size, it probably is the wrong size.

Carefully look over the inserts and check depths with calipers. You're looking for the correct depth (5.8mm) and a smooth surface. In the picture, the ideal size wound up being 4.5 with a taper of -4 degrees (third row, third column).

## Updating the Fusion Model

The `Parameters` file will need to be updated. `M3_insert_dia` and `M3_insert_taper` are the respective parameters to set. From there you will need to update and export the STL files.