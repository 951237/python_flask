# -*- coding : utf-8 -*-

from flask import Flask, render_template, request  # 플라스크, 탬플릿, 리퀘스트 라이브러리 호출
from tensorflow.keras.models import Sequential      # 케라스 모델 라이브러리 호출
from tensorflow.keras.layers import Dense           # 케라스 레이어 라이브러리 호출
from tensorflow import keras                        # 텐서플로 케라스 호출
import numpy as np      # 넘파이 라이브러리 호출

app = Flask(__name__)       # 플라스크 앱 설정하기

model = Sequential()        # 모델 객체 생성
model.add(Dense(1, input_dim=4))        # 모델에 레이어 생성, 입력 4개, 출력 1개

new_model = keras.models.load_model('./model/predic_cabbage.h5')        # 트레이닝 모델 불러오기


@app.route("/", methods=['GET', 'POST'])    # 겟방식과 포스트 방식을 모두 선언
def index():        # 웹페이지 불러오기 함수, 웹페이지 파일의 이름과 동일
    if request.method == 'GET':     # get형식일 경우 
        return render_template('index_new.html')    # index파일 불러오기

    if request.method == 'POST':    # post방식 즉 폼에 입력해서 전송했을 경우
        avg_temp = float(request.form['avg_temp'])      # 폼에서 'avg_temp'의 입력값을 avb_temp변수 값으로 지정
        min_temp = float(request.form['min_temp'])
        max_temp = float(request.form['max_temp'])
        rain_fall = float(request.form['rain_fall'])

        price = 0       # 배추가격을 초기화 하기

        data = [avg_temp, min_temp, max_temp, rain_fall]    # 변수의 값을 리스트로 저장장
        dic = new_model.predict(np.array(data).reshape(1, 4))   # 리스트값을 넘파이를 통해서 1, 4형식으로 지정하여 예측하기

        return render_template('index_new.html', price=dic)     # index페이지에 price 부분에 예측값을 반환


if __name__ == '__main__':  # 플라스크 기본 형식 
    app.run(host='0.0.0.0', port=8000, debug=True)
