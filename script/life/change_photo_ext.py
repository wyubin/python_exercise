import os, glob
[os.rename(x, x.replace('HEIC', 'heic')) for x in glob.glob('./*.HEIC')]
