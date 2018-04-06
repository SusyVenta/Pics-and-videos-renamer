# Pics&VidsRenamer
Python script that allows renaming multiple files to their exif creation date\last modification date -  AGPL-3.0+

REQUIREMENTS:

  - This script is written with Python 3.6.5 and thus requires the installation of Python 3.x to run
  - This script requires the installation of the ExifRead 2.1.2 module, which reads files' exif data
  - This script has been written in a Windows 10 environment, specifically designed to work on Windows, but it also works on Linux and 
    probably on MacOS.
  - Before running the script, be sure to change the "path" variable to a path of your choice (your folder containing the files you want 
    to rename
   
DESCRIPTION:

This script checks all the files in the chosen folder, to see if their names fit the format "2018-04-24 10.60.45" (year, month, day hh.mm.ss). I have tested the program with .jpg, .jpeg, .mp4, .png files and it works fine with these.
If a file's name already corresponds to the format, the file won't be renamed. Otherwise, the program checks if the file has exif data and if it does the file will be renamed with the date the photo\video\etc. was taken.
If the file does not have exif information, the new name will be its last modification date (in most cases it's the date the file was created). 
In either case (exif date or last modification date), before renaming the file, the script checks if a file with the new name already exists and, in that case, the current file's new name will be e.g. "2018-04-24 10.60.45-1.jpg". If the latter already exists the new name will be "2018-04-24 10.60.45-1-2.jpg", and so on. This is useful if you want to rename photos received at the same time e.g. on WhatsApp (that have the same last modification date).
Finally, the script will print the names of the files that did not need to be renamed, as well as the name of the files that have been renamed.
At the end you'll have all the files' names in the same format, stating the date the photos\videos\etc. were taken. This is especially useful if you want to backup your files (e.g. with Google Photos) and be able to later access them in chronological order.
Enjoy!
