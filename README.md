# VideoFilters
Pretty self explanatory, provide the processit function with the correct argument. This will require the cascadeclassifier trained on detecting faces.
1. if whole_frame=False
  Only apply the filter around the detected face, If true apply to the whole frame
2. if randomzoom=True
  Randomly zoom on detected face
  
Examples

# Face Only with a low alpha (preferring edited image)
![](Face Only.gif)

# Whole Frame with a high alpha (preferring original image)
![](WholeFrame.gif)
