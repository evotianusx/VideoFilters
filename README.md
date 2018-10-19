# VideoFilters
Pretty self explanatory, provide the processit function with the correct argument. This will require the cascadeclassifier trained on detecting faces.
1. if whole_frame=False
  Only apply the filter around the detected face, If true apply to the whole frame
2. if randomzoom=True
  Randomly zoom on detected face
3. You can play around movementx,movementy to have more or less shift and also the direction
4. play with alpha parameter to make the edited image stand out more or less

Examples

# Face Only with a low alpha 
![](Face_Only.gif)

# Whole Frame with a high alpha 
![](WholeFrame.gif)
