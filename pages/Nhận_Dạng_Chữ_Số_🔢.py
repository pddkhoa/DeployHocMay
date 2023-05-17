import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np
from tensorflow import keras
from tensorflow.keras.models import model_from_json 
from tensorflow.keras.optimizers import SGD 
import cv2

model_architecture = "digit_config.json"
model_weights = "digit_weight.h5"
model = model_from_json(open(model_architecture).read())
model.load_weights(model_weights) 

optim = SGD()
model.compile(loss="categorical_crossentropy", optimizer=optim, metrics=["accuracy"]) 

mnist = keras.datasets.mnist
(X_train, Y_train), (X_test, Y_test) = mnist.load_data()
X_test_image = X_test

RESHAPED = 784

X_test = X_test.reshape(10000, RESHAPED)
X_test = X_test.astype('float32')

#normalize in [0,1]
X_test /= 255

def create_digit_image(X_test_image, index):
    digit_random = np.zeros((10*28, 15*28), dtype = np.uint8)
    for i in range(0, 150):
        m = i // 15
        n = i % 15
        digit_random[m*28:(m+1)*28, n*28:(n+1)*28] = X_test_image[index[i]] 
    cv2.imwrite('digit_random.jpg', digit_random)
    image = Image.open('digit_random.jpg') 
    return image


def predict_digits(X_test, index, model):
    X_test_sample = np.zeros((150,784), dtype = np.float32)
    for i in range(0, 150):
        X_test_sample[i] = X_test[index[i]]
    prediction = model.predict(X_test_sample)
    s = ''
    for i in range(0, 150):
        ket_qua = np.argmax(prediction[i])
        s = s + str(ket_qua) + ' '
        if (i+1) % 15 == 0:
            s = s + '\n\n'
    return s
st.set_page_config(
    page_title="Nhận Dạng Chữ Số Viết Tay",
    page_icon="🔢",
    layout="wide",)

def main():
    st.title('NHẬN DẠNG CHỮ SỐ VIẾT TAY 🔢🔢🔢')
    st.markdown("""
    Đây là website nhận dạng chính xác các chữ số từ hình ảnh
    """)
    index = np.random.randint(0, 9999, 150)
    if st.button('Tạo ảnh'):
        image = create_digit_image(X_test_image, index)
        st.image(image, width=600)
        result = predict_digits(X_test, index, model)
        st.success(f'Kết quả: \n\n{result}')

if __name__ == "__main__":
    main()