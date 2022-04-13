def imageData = getCurrentImageData()

// Define output path (relative to project)
def outputDir = buildFilePath(PROJECT_BASE_DIR, 'OGImages')
mkdirs(outputDir)
def name = GeneralTools.getNameWithoutExtension(imageData.getServer().getMetadata().getName())
def path = buildFilePath(outputDir, "YAP_MRD_HumanLung_Slide" + name + "_OG.png")


// Define image server 
def server = getCurrentServer()

// Write the image if no downsample
//writeImage(server, path)

// Write the full image downsampled by a factor of *
def requestFull = RegionRequest.createInstance(server, 4.5)
writeImageRegion(server, requestFull, path)