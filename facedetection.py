
cascade = (CvHaarClassifierCascade*)cvLoad( cascade_name, 0, 0, 0 );
storage is allocated:
CvMemStorage* storage = cvCreateMemStorage(0);
CvSeq* cvHaarDetectObjects( const CvArr* image, CvHaarClassifierCascade* cascade, CvMemStorage* storage,
double scale_factor = 1.1, 
int min_neighbors = 3, 
int flags = 0,30
CvSize min_size = cvSize(40,40) );
