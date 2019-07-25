## References
### Color Detection 
* [https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html] 
* [https://docs.opencv.org/4.0.1/df/d9d/tutorial_py_colorspaces.html]

## Notes

### Useful Tool
* http://colorizer.org/

### Why HSV?
Unlike RGB which is defined in relation to primary colors, HSV is defined in a way that is similar to how humans perceive color.
For our application, the major advantage of using the HSV color space is that the color/tint/wavelength is represented by just the Hue component.
So when I say, I need a particular color and select the hue component then depending on the saturation component I get different shades of that color and further depending on the value component I get different Intensities of a particular shade of the color.

## How to find HSV values to track?
    >>> green = np.uint8([[[0,255,0 ]]])
    >>> hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
    >>> print(hsv_green)
    [[[ 60 255 255]]]
Now you take [H-10, 100,100] and [H+10, 255, 255] as lower bound and upper bound respectively. Apart from this method, you can use any image editing tools like GIMP or any online converters to find these values, but don’t forget to adjust the HSV ranges.

hsv_green : [[[ 60 255 255]]]
hsv_blue : [[[120 255 255]]]
hsv_red : [[[  0 255 255]]]

