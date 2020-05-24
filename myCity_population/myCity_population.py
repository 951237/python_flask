import pandas as pd
import matplotlib.pyplot as plt

# 데이터 프레임 살펴보기


def df_info(df):
    print(df.head(), '\n')
    print(df.tail(), '\n')
    print(df.columns, '\n')
    print(df.info())

# 데이터프레임의 칼럼별 데이터값 확인


def df_unique(df, num):     # 데이터프레임 이름과, 칼럼내의 유니크 데이터 갯수
    col = df.columns.to_list()
    for i in col:
        v_unique = df[i].unique()
        if len(v_unique) < num:
            print(f'{i} : {len(v_unique)}개', '\n', f'{df[i].unique()}', '\n')
        else:
            pass


F_URL = '연령별인구_2004.csv'  # 파일 URL
# 천의 자리 구분 콤마 빼고 CSV파일 불러오기
df = pd.read_csv(F_URL, encoding='cp949', thousands=',')

a = df.columns.difference(['행정구역']).tolist()  # 특정 칼럼만 제외하고 선택하여 리스트로 바꾸기
df[a].apply(pd.to_numeric)     # 특정칼럼만 데이터를 숫자로 바꾸기

city = input('인구현황 조회를 원하는 동이름을 입력하시오 : ')
df_city = df[df['행정구역'].str.contains(city)]  # 새솔동 이름 들어간 행을 선택하기
df_man = df_city.iloc[:, 3:104]     # 남자 인구부분만 선택
df_woman = df_city.iloc[:, 106:208]  # 여자 인구부분만 선택

man = df_man.T  # 데이터 프레임 행렬 바꾸
man = man.reset_index(drop=True)    # 인덱스 0부터 번호 다시 따기
man.columns = ['man']    # 칼럼 이름 바꾸기
woman = df_woman.T  # 데이터 프레임 행렬 바꾸기
woman = woman.reset_index(drop=True)    # 인덱스 0부터 번호 다시 따기
woman.columns = ['woman']  # 칼럼 이름 바꾸기
df_merge = pd.merge(man, woman, how='outer', left_index=True,
                    right_index=True)     # 데이터 프레임 합치기

# plt.figure(figsize = (10, 5), dpi = 150)
# plt.plot(df_merge)
df_merge.plot(figsize=(16, 8))
plt.draw()
fig = plt.gcf()
fig.savefig('myFile.png', dpi=fig.dpi)

