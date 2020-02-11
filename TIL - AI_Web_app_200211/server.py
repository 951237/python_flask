# -*- coding : utf-8 -*-

from flask import Flask, render_template, request  # 라이브러리 호출

import datetime
import tensorflow as tf
import numpy as np

app = Flask(__name__)  # 플라스크 앱 설정

x = tf.placeholder(tf.float32, shape = [None, 4])
y = tf.placeholder(tf.float32, shape=[None, 1])
w = tf.Variable(tf.random_normal([4,1], name = 'weight'))
b = tf.Variable(tf.random_normal([1]), name = 'bias')

hypothesis = tf.matmul(x, y) + b

saver= tf.train.Saver()
model = tf.global_variables_initializer()

sess = tf.Session()
sess.run(model)

save_path = './model/saved.cpkt'
saver.restore(sess, save_path)

@app.route("/", methods=['GET', 'POST'])  # 겟방식과 포스트 방식을 모두 선언
def index():  # 웹페이지 파일의 이름과 동일
    if request.method == 'GET'
        return render_template('index.html')
    if request.method =='POST':
        avg_temp = float(request.form['avg_temp'])
        min_temp = float(request.form['min_temp'])
        max_temp = float(request.form['max_temp'])
        rain_fall = float(request.form['rain_fall'])

    price = 0

    data = ((avg_temp, min_temp, max_temp, rain_fall),)
    arr = np.array(data, dtype = np.float32)

    x_data = arr[0:4]
    dict = sess.run(hypothesis, feed_fict = {x : x_data})
    print(dict[0])
    return render_template('index.html', price = price)


if __name__ == '__main__':
    app.run(debug=True)
