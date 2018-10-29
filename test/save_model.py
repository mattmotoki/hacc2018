import tensorflowjs as tfjs
from keras.applications.mobilenet import MobileNet

model = MobileNet(weights='imagenet')
tfjs.converters.save_keras_model(model, 'test_model')
