# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 10:22:33 2018

@author: Pierre
"""

import exifread as EXIF

def date(photo):
    with open(photo, 'rb') as fh:
        tags = EXIF.process_file(fh, stop_tag="EXIF DateTimeOriginal")
        dateTaken = tags["EXIF DateTimeOriginal"]
        return dateTaken