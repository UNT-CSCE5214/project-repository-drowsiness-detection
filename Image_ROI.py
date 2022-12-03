cvSetImageROI(
img, /* the source image */
cvRect(face->x, /* x = start from leftmost */
face->y + (face->height)/5, /* 
y = a few pixels from the top */
face->width, /* width = same width with the face */ 
(face->height)/3  /* height = 1/2 of face height */
)
