def yolo_model_predict():
	import os,glob
	from matplotlib.pyplot import imshow
	import scipy.io
	import scipy.misc
	import numpy as np
	from PIL import Image
	from keras import backend as K
	from keras.models import load_model
	from Yolo_model.yolo_utils import read_classes, read_anchors, generate_colors, preprocess_image, draw_boxes

	global class_names,anchors,yolo_model,yolo_outputs
	
	K.clear_session()
	class_names = read_classes("Yolo_model/model_data/coco_classes.txt")
	anchors = read_anchors("Yolo_model/model_data/yolo_anchors.txt")
	yolo_model = load_model("Yolo_model/model_data/yolo.h5")
	from Yolo_model.yad2k.models.keras_yolo import yolo_head, yolo_eval
	yolo_outputs = yolo_head(yolo_model.output, anchors, len(class_names))

	image_list = glob.glob("media/images/*")[:1]
	for i1 in image_list:
		input_image_name = i1.split("\\")[-1]
		input_image = Image.open(i1)
		input_image.save("media/images/query_image.jpg",quality=100)
		width, height = input_image.size
		width = np.array(width, dtype=float)
		height = np.array(height, dtype=float)
		image_shape = (height, width)

		boxes, scores, classes = yolo_eval(yolo_outputs, image_shape)

		sess = K.get_session()
		image, image_data = preprocess_image("media/images/" + input_image_name, model_image_size = (608, 608))

		#Run the session
		out_scores, out_boxes, out_classes = sess.run([scores, boxes, classes],feed_dict={yolo_model.input:image_data,K.learning_phase(): 0})

		#Print the results
		print('Found {} boxes for {}'.format(len(out_boxes), input_image_name))
		#Produce the colors for the bounding boxs
		colors = generate_colors(class_names)
		#Draw the bounding boxes
		draw_boxes(image, out_scores, out_boxes, out_classes, class_names, colors)
		#Apply the predicted bounding boxes to the image and save it
		
		image.save("media/output/output_image.jpg", quality=100)
		K.clear_session()
		return input_image_name
'''
output_image = scipy.misc.imread(os.path.join("out", input_image_name))
imshow(output_image)
'''