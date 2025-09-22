
## referenced repos

### [FaceAge](https://github.com/AIM-Harvard/FaceAge)

developed by Havard AIM(AI in Medicine) team. 

core components are mtcnn (**Multi-task Cascaded Convolutional Networks**), it detects the face, creates bounding box (co-ordinates) and also returns confidence score. 
It also returns the keypoints for face landmarks (left eye, right eye, nose tip, left and right corner of the mouth). 

skimage which will be replaced with OpenCV, for dealing with images and converting images to NumPy array.

a .h5 model that predicts the facial age of a person, a  CNN-based classification model whose final layers replaced with densely connected layers which outputs the regression line for the predicted facial age. 

the model was trained on the dataset of about 6GB size. most of the images used are from of hollywood celebrities and might not work accurately with the faces from Nepal (Asian skin)

code: 

downloads the weights for the model.

weights_url = "https://github.com/AIM-Harvard/FaceAge/releases/download/v1/faceage_model.h5"
!wget -O FaceAge/models/faceage_model.h5 $weights_url
import gdown
folder_id = "1xOfTNGGPEmy6HZp0TwiODXVcBsDz1OUR"
gdown.download_folder(f'https://drive.google.com/drive/folders/{folder_id}', quiet=False, use_cookies=False)
pip install mtcnn
import tensorflow as tf
def get_face_bbox_from_image(path_to_image):
  assert os.path.exists(path_to_image)
  pat_img = imread(path_to_image)
  try:
    return mtcnn.mtcnn.MTCNN().detect_faces(pat_img)[0]
  except:
    # patient
    print('ERROR: Processing error for file "%s"'%(path_to_image))
    return dict()

face_bbox_dict = dict()

t = time.time()

for idx, input_image in enumerate(input_file_list):

  clear_output(wait = True)

  # get rid of label information and file extension
  subj_id = input_image.split("_")[3].split(".")[0]

  print('(%g/%g) Running the face localization pipeline for "%s"'%(idx + 1,
                                                                   len(input_file_list),
                                                                   subj_id))
  subj_age = input_image.split("_")[0]
  subj_gender = input_image.split("_")[1]
  subj_race = input_image.split("_")[2]
  path_to_image = os.path.join(input_base_path, input_image)
  face_bbox_dict[subj_id] = dict()
  face_bbox_dict[subj_id]["age"] = subj_age
  face_bbox_dict[subj_id]["gender"] = subj_gender
  face_bbox_dict[subj_id]["race"] = subj_race

  face_bbox_dict[subj_id]["path_to_image"] = path_to_image

  face_bbox_dict[subj_id]["mtcnn_output_dict"] = get_face_bbox_from_image(path_to_image)
  if not idx % 5:
    tf.keras.backend.clear_session()
    gc.collect()
elapsed = time.time() - t
print("\n... Done in %g seconds."%(elapsed))
### [DermaVision](https://github.com/iad1tya/Dermavision/tree/main)

openly available repository.  

CNN-based skin analysis model is trained which detects the  severity of the acne, pigmentation pattern and dark circles identification. 

tested the model, 


mtcnn/facenet detects the face, the face is cropped and then the cropped image is classified using YOLO. (alot of classification dataset is available.)


faceage needs a testing as well

sdc:

