# Requires an ImageMagick installation. See https://imagemagick.org/script/convert.php

from os import system

name = "input.pdf"
output = "output.pdf"

# Conf 1
#cmd = "convert -density 105 {0} -rotate 1 -gamma 0.5 -brightness-contrast -1,10 -attenuate 0.1 +noise Multiplicative -flatten -attenuate 0.01 +noise Multiplicative -sharpen 0x1 -colorspace Gray {1}".format(name, output)

# Conf 2
#cmd = "convert -density 100 {0} -rotate 0.6  -brightness-contrast -3,25  -attenuate 0.05 +noise Multiplicative -flatten -attenuate 0.05 +noise Multiplicative -sharpen 0x1 -colorspace RGB {1}".format(name, output)

# Conf 3
cmd = "convert -density 100 {0} -rotate 1 -brightness-contrast 10x10 -colorspace RGB {1}".format(name, output)

#print(cmd)

# Execute the postprocessing command
system(cmd)

# and open the final file
system(output)
