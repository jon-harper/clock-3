G90              ; absolute positioning
G28              ; home
G0  Z 4          ; drop the bed a bit
G0  X 155 Y 155  ; center on the bed
G0  X 310        ; move to XMAX
G28 X            ; home X
G0  X 155        ; back to center
G0  Y 310        ; Y to YMAX
G28 Y            ; home Y
G0  Y 155        ; back to center
G0  Z 300        ; drop to 300
G0  Z 350        ; drop to ZMAX
G28 Z            ; home Z
G0  Z 4          ; drop the bed a bit