from flask import Flask, render_template

app = Flask(__name__)


posts = [
    {
        '작성자' : '951237',
        '제목' : '블로그 포스트 1',
        '내용': '첫번째 포스트',
        '작성일': '2020. 2. 7',
    },
    {
        '작성자': 'cutemin226',
        '제목': '블로그 포스트 2',
        '내용': '두번째 포스트',
        '작성일': '2020. 2. 8',
    },
]

@app.route('/')
@app.route('/home')     # home 페이지
def home():
    return render_template('home.html', posts = posts) # templates폴더의  파일
    # 불러오기 post는 페이지의 내용

@app.route('/about')    # about 페이지 
def about():
    return render_template('about.html', title = 'About') # templates폴더의 파일
    # 불러오기 'title'는 웹페이지 윈도우 이름


if __name__ == '__main__':
    app.run()

