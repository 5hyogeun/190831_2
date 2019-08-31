import tensorflow as tf

class CalculatorModel:
    def __init__(self):
        pass

    def create_add_model(self):
        w1 = tf.placeholder(tf.float32, name = 'w1')    # tensorflow의 변수 한 개 => 숫자랑 매칭
        w2 = tf.placeholder(tf.float32, name = 'w2')
        feed_dict = {'w1':8.0, 'w2':2.0}    # dummy 값(input value)/ java <= json
        r = tf.add(w1, w2, name='op_add')    # model 이름 정해줌
        sess = tf.Session()
        _ = tf.Variable(initial_value='fake_variable')    # fake_variable => 임시변수
        sess.run(tf.global_variables_initializer())    # 전역변수로 초기화
        saver = tf.train.Saver()
        result = sess.run(r, {w1 : feed_dict['w1'], w2 : feed_dict['w2']})
        print('TF 덧셈 결과 : {}'.format(result))
        saver.save(sess, './saved_add_model/model', global_step=1000)    # 1000번 연산해라
