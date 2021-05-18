import os
import random

name = "input.pdf"
output = "output.pdf"

##tr = "C:\Program Files\ImageMagick\\ "

#cmd = "convert {0} -colorspace gray +clone -blur 0x1 +swap -compose divide -composite -linear-stretch 5%x0% -rotate 1.5 {1}".format(name, output)

#cmd = "convert {0} +clone -blur 0x1 +swap -compose divide -composite -gamma 0.1 -linear-stretch 5%x0% -rotate 1.5 {1}".format(name, output)

#cmd = "convert $f -colorspace gray \( +clone +noise Random -threshold 99% -negate -blur 0x5 -level 97.5%,97.5% \) -evaluate-sequence min -blur 0xecho $RANDOM %2 +1 | bc` -level 25%,75% -rotate -0.echo $RANDOM %10 +1 | bc -sharpen 0x3.0 -blur 0xecho $RANDOM %2 +1 | bc -level 10%,90% -rotate -0.` echo $RANDOM %10 +1 | bc` -sharpen 0x1.2 -colorspace gray"

#cmd = "convert {0} -compose divide -composite -linear-stretch 5%x0% -rotate 1.5 {1}".format(name, output)

#cmd = "convert -density 105 {0} -rotate 1 -attenuate 0.1 +noise Multiplicative -flatten -attenuate 0.01 +noise Multiplicative -sharpen 0x1.25 -colorspace Gray {1}".format(name, output)

# Conf 1
#cmd = "convert -density 105 {0} -rotate 1 -gamma 0.5 -brightness-contrast -1,10 -attenuate 0.1 +noise Multiplicative -flatten -attenuate 0.01 +noise Multiplicative -sharpen 0x1 -colorspace Gray {1}".format(name, output)

# Conf 2
#cmd = "convert -density 100 {0} -rotate 0.6  -brightness-contrast -3,25  -attenuate 0.05 +noise Multiplicative -flatten -attenuate 0.05 +noise Multiplicative -sharpen 0x1 -colorspace RGB {1}".format(name, output)

# Conf 3
cmd = "convert -density 100 {0} -rotate 1 -brightness-contrast 10x10 -colorspace RGB {1}".format(name, output)

print(cmd)

os.system(cmd)

os.system(output)
