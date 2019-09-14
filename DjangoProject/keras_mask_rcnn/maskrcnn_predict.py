from mrcnn.config import Config
from mrcnn import model as modellib
from mrcnn import visualize
import numpy as np
import colorsys
import argparse
import imutils
import random
import cv2,glob
import os,time
import warnings
warnings.simplefilter("ignore")

global model
# load the class label names from disk, one label per line
print("present working directory: ",os.getcwd())
CLASS_NAMES = open("keras_mask_rcnn\\coco.txt").read().strip().split("\n")
#print(CLASS_NAMES)
# generate random (but visually distinct) colors for each class label
# (thanks to Matterport Mask R-CNN for the method!)
hsv = [(i / len(CLASS_NAMES), 1, 1.0) for i in range(len(CLASS_NAMES))]
COLORS = list(map(lambda c: colorsys.hsv_to_rgb(*c), hsv))
random.seed(42)
random.shuffle(COLORS)

anim_list = ['bird','cat','dog','horse','sheep','cow','elephant','bear','zebra','giraffe','hot dog','teddy bear']
class SimpleConfig(Config):
	# give the configuration a recognizable name
	NAME = "coco_inference"

	# set the number of GPUs to use along with the number of images
	# per GPU
	GPU_COUNT = 1
	IMAGES_PER_GPU = 1

	# number of classes (we would normally add +1 for the background
	# but the background class is *already* included in the class
	# names)
	NUM_CLASSES = len(CLASS_NAMES)

# initialize the inference configuration
config = SimpleConfig()

# initialize the Mask R-CNN model for inference and then load the
# weights
print("[INFO] loading Mask R-CNN model...")
model = modellib.MaskRCNN(mode="inference", config=config,model_dir=os.getcwd())
model.load_weights("keras_mask_rcnn\\mask_rcnn_coco.h5", by_name=True)
model.keras_model._make_predict_function()

def predict_results():
	# load the input image, convert it from BGR to RGB channel
	# ordering, and resize the image
	query_image = glob.glob("media/images/*")[:1]
	for single_image in query_image:
	    t1 = time.time()
	    input_image_name = single_image.split('\\')[-1]
	    image = cv2.imread(single_image)
	    cv2.imwrite("media/images/query_image.jpg",image)
	    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	    image = imutils.resize(image, width=512)
	    # perform a forward pass of the network to obtain the results
	    print("[INFO] making predictions with Mask R-CNN...")
	    r = model.detect([image], verbose=0)[0]
	    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
	    det_obj = 0
	    for i in range(0, len(r["scores"])):
	    	# extract the bounding box information, class ID, label, predicted
	    	# probability, and visualization color
	    	(startY, startX, endY, endX) = r["rois"][i]
	    	classID = r["class_ids"][i]
	    	label = CLASS_NAMES[classID]
	    	if(label in anim_list):
	    		det_obj+=1
	    		score = r["scores"][i]
	    		color = [int(c) for c in np.array(COLORS[classID]) * 255]
	    		# draw the bounding box, class label, and score of the object
	    		cv2.rectangle(image, (startX, startY), (endX, endY), color, 2)
	    		text = "{}: {:.3f}".format(label, score)
	    		y = startY - 10 if startY - 10 > 10 else startY + 10
	    		#cv2.putText(image, text, (startX, y), cv2.FONT_HERSHEY_SIMPLEX,0.6, color, 2)
	    print("elapsed time: ",time.time()-t1)
	    # show the output image
	    print("\n======================Detected Objects=========================")
	    print("No.of detected objects(animals): ",det_obj)
	    print("================================================================\n")
	    cv2.imwrite("media/output/output_image.jpg", image)
	#cv2.waitKey()
	return input_image_name