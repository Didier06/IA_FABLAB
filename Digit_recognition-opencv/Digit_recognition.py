import cv2
import numpy as np
from tensorflow import keras
from keras.models import load_model
from keras.layers import Dense

#from tensorflow.keras.models import load_model

cap = cv2.VideoCapture(0 + cv2.CAP_DSHOW)
WIDTH = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
HEIGHT = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

model = load_model('model\modelcnn.keras')
#model = load_model('model\model_ANN_dense.keras')


def prediction(image, model):
    img = cv2.resize(image, (28, 28))
    img = img / 255
    img = img.reshape(1, 28, 28) # pour cnn 
    #img = img.reshape((1, 28 * 28)) # pour dense
    predict = model.predict(img)
    prob = np.amax(predict)
    #class_index = model.predict_classes(img)
    class_index = (model.predict(img) > 0.6).astype("int32")
    
    result = class_index[0]
    if prob < 0.65:
        result = 0
        prob = 0
    return result, prob


while True:

    _, frame = cap.read()
    #frame = cv2.rotate(frame, cv2.ROTATE_180)
    frame_copy = frame.copy()
    size = 150
    bbox_size = (size, size)
    bbox = [(int(WIDTH // 2 - bbox_size[0] // 2), int(HEIGHT // 2 - bbox_size[1] // 2)),
            (int(WIDTH // 2 + bbox_size[0] // 2), int(HEIGHT // 2 + bbox_size[1] // 2))]

    img_cropped = frame[bbox[0][1]:bbox[1][1], bbox[0][0]:bbox[1][0]]
    img_gray = cv2.cvtColor(img_cropped, cv2.COLOR_BGR2GRAY)
    
    #img_gray = cv2.bitwise_not(img_gray)
    (thresh, img_gray) = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)
    """ threshold : First argument is the source image, which should be a grayscale image. Second argument is the threshold value 
    which is used to classify the pixel values. Third argument is the maxVal which represents 
    the value to be given if pixel value is more than """
    #(thresh, img_gray) = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TRUNC)
    #img_gray = cv2.resize(img_gray, (200, 200))
    #img_gray = cv2.bitwise_not(img_gray)
    #cv2.imshow("cropped", img_gray)

    img_gray = cv2.resize(img_gray, (size, size))
    #cv2.imshow("cropped", img_gray)

    result, probability = prediction(img_gray, model)
    val = np.argmax(result)
    print(result)
    cv2.putText(frame_copy, f"Prediction : {result}", (40, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 255), 2, cv2.LINE_AA)

    cv2.putText(frame_copy, "Probability : " + "{:.2f}".format(probability), (40, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 255), 2, cv2.LINE_AA)
    cv2.rectangle(frame_copy, bbox[0], bbox[1], (0,255,0), 3)

    cv2.imshow("input", frame_copy)
    cv2.imshow("cropped", img_gray)
    #cv2.waitKey(0)
    if cv2.waitKey(100) & 0xFF == 27:# The waitKey() function waits for the specified millisecond (it leaves only the last 8 bits of the original (in this case, whatever cv2.waitKey(0) is).
        break

cv2.destroyAllWindows()
