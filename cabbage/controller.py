from cabbage.model import CabbageModel
import tensorflow as tf

class CabbageController:
    def __init__(self, avg_temp, min_temp, max_temp, rain_fall):
        self._avg_temp = avg_temp
        self._min_temp = min_temp
        self._max_temp = max_temp
        self._rain_fall = rain_fall

    def service(self):
        X = tf.placeholder(tf.float32, shape=[None, 4])    # 저장된 모델 불러옴 / [행, 열]
        W = tf.Variable(tf.random_normal([4, 1]), name='weight')
