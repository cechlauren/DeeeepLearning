#Use Python to call QuPath from the command line, converting image types and pyramidalize (?) it.
#Adapt from https://www.imagescientist.com/command-line-and-python#converting
#Script variable points to a Groovy script to be used by Python. 
#Before using: Set up QuPath and Python in computing environment, create InputImages directory containing all target images.
import os
import subprocess
import time
script = "./ApplyMasks.groovy" #ensure correct location
imageDirectory = "../InputImages"
outputDirectory = "../ProcessedImages"
qupath = "/Build/QuPath-0.2.3/QuPath-0.2.3 (console).exe" #or whatever equivalent for computing environment

fileList = os.listdir(imageDirectory)
for file in fileList:
    if (file.endswith('.tif', '.png') and not file.endswith('.ome.tif')):
        imageFile = imageDirectory + file
        outputImage = outputDirectory + file #will not specify if file came from .tif or .png
        subprocess.run([qupath, "script", script, "-i", imageFile], shell=True)
        #subprocess.run([qupath, "convert-ome", imageFile, outputImage, "-y=4", "-p"], shell=True)
        os.rename(imageFile, outputImage)
