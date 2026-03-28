def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    arr = [[i * j for j in range (len(image[0]))] for i in range(len(image))]
  # Write code here
    for i in range(len(image)):
        for j in range(len(image[i])):
            gr = 0.299*image[i][j][0]+0.587*image[i][j][1]+0.114*image[i][j][2]

            arr[i][j]=gr

    return arr
                
            
        
        
            
    