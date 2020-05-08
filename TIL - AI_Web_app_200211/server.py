# -*- coding : utf-8 -*-

from flask import Flask, render_template, request  # 라이브러리 호출

import numpy as np
from tensorflow import keras
import tensorflow as tf


app = Flask(__name__)  # 플라스크 앱 설정

# 가중치와 옵티마이저를 포함하여 정확히 동일한 모델을 다시 생성합니다
new_model = keras.models.load_model('./model/predic_cabbage.h5')


@app.route("/", methods=['GET', 'POST'])  # 겟방식과 포스트 방식을 모두 선언
def index():  # 웹페이지 파일의 이름과 동일
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        avg_temp = float(request.form['avg_temp'])
        min_temp = float(request.form['min_temp'])
        max_temp = float(request.form['max_temp'])
        rain_fall = float(request.form['rain_fall'])

    price = 0

    data = [avg_temp, min_temp, max_temp, rain_fall]
    dic = new_model.predict(np.array(data).reshape(1, 4))
    price = dic[0]
    return render_template('index.html', price = price)


if __name__ == '__main__':
    app.run(debug=True)
