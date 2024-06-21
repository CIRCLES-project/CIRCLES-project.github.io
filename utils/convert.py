#!/usr/bin/env python3

import os
import sys

filename = sys.argv[1]
(basename, ext) = os.path.splitext(filename)
print("Basename is %s" % basename)

resolutions = [
    2200,
    1600,
    1080,
    800,
    500,
]

for x in resolutions:
    print("Rescaling to %d pixels" % x)
    newname = basename + "-p-%d.png" % x
    # ImageMagick resize will fit the image into the given dimensions
    # By default it does not change the aspect ratio
    cmd = "convert %s -resize %dx%d %s" % (filename, x, x, newname)
    print("cmd is [%s]" % cmd)
    os.system(cmd)
