#/usr/bin/env python3

import os
import sys
import math
import drawsvg as draw

def draw_backgrounds():

    if not os.path.exists("backgrounds"):
        os.makedirs("backgrounds")

    # Section 1 - 2200x1530
    d = draw.Drawing(2200, 1530, origin='center')
    # Blue background circle is color #313fe5
    circle1 = draw.Circle(0,0,740, stroke='none', fill="#313fe5", fill_opacity=0.2)
    d.append(circle1)
    d.save_svg("backgrounds/section-1.svg")
    d.save_png("backgrounds/section-1.png")


    # Section 2 - 1650x1146
    d = draw.Drawing(1650, 1146, origin='center')
    circle2 = draw.Circle(-300,-225,350, stroke='none', fill="#313fe5", fill_opacity=0.2)
    d.append(circle2)
    d.save_svg("backgrounds/section-2.svg")
    d.save_png("backgrounds/section-2.png")


    # Section 3 - 1650x1061
    d = draw.Drawing(1650, 1061, origin='center')
    circle3_1 = draw.Circle(-375,-225,275, stroke='none', fill="#313fe5", fill_opacity=0.2)
    d.append(circle3_1)
    circle3_2 = draw.Circle(350,-50,275, stroke='none', fill="#56b59c", fill_opacity=0.2)
    d.append(circle3_2)
    d.save_svg("backgrounds/section-3.svg")
    d.save_png("backgrounds/section-3.png")


    # Hero image - 4320x3060
    d = draw.Drawing(4320, 3060)
    sw1 = 150
    r1 = 2250/2-sw1/2
    circle_4_1 = draw.Circle(3077+r1+sw1/2, -770+r1+sw1/2, r1, stroke='#6976ff', fill="none", stroke_opacity=1.0, stroke_width=sw1)
    d.append(circle_4_1)
    sw2 = 160
    r2 = 1630/2-sw2/2
    circle_4_2 = draw.Circle(-644+r2+sw2/2, 1389+r2+sw2/2, r2, stroke='#f4ebb3', fill="none", stroke_opactiy=1.0, stroke_width=sw2)
    d.append(circle_4_2)
    sw3 = 110
    r3 = 1280/2-sw3/2
    circle_4_3 = draw.Circle(0+r3+sw3/2, -892+r3+sw3/2, r3, stroke='#fbc0c0', fill="none", stroke_opacity=1.0, stroke_width=sw3)
    d.append(circle_4_3)
    d.save_svg("backgrounds/section-hero.svg")
    d.save_png("backgrounds/section-hero.png")



if __name__ == "__main__":
    draw_backgrounds()
