# -*- coding : utf-8 -*-

from flask import Flask, render_template, request  # 라이브러리 호출


app = Flask(__name__)  # 플라스크 앱 설정


@app.route("/", methods=['GET', 'POST'])  # 겟방식과 포스트 방식을 모두 선언
def index():  # 웹페이지 파일의 이름과 동일
    return render_template('index.html', price = 0)


if __name__ == '__main__':
    app.run(debug=True)
