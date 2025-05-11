# Wildlif-monitoring-and-Conservation-using-opencv

## Tilte

### Wildlife monitoring and Conservation

## Usage

### This project helps to find moving animals in a video using a computer program.It is useful for watching animals in the forest without going there.

## Code Descripton

### Programming Language: Python

- Python is the High level programming language.

- Python is creted by Van Guido Rossam in the year 1991.

### Packages used: Opencv

- Opencv stands for Open Source Computer Vision.

- It is used for Image Processing

- Opencv is originally developed by Intel and now it is maintained by OpenCV Foundation.

## Working

- Import the opencv package

- Declare the variable to store the path of the wildlife video

- The Video is read by the method VideoCapture()

- The method createBackgroundSubtractorMOG2() is used to find the moving objects in the video.

- findContours() method is used to find the shape of the moving objects.

- boundingRect() gets the position and size of the moving objects.

- rectangle() method is used to show the visual representation of the animal.It shows as a box around the animal.

- imshow() is used to show or run the video with rectangular boxes around the moving objects.

- waitKey() is used to quit the video the key is set to be 'q',when the user clicks q the video will be closed or terminated.

- destroyAllWindows() closes the video window after the video full played completely.

## Use Cases

- See animals in the forest.

- Helps to protect animals by watching their movements.

## Conclusion

### This project hepls the forest officers to track animals without being in the wild.It is a simple low-cost solution that can be used in the real-time or with recorded video.