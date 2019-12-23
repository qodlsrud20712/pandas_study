import pandas as pd
# dict_data = {'a':1, 'b':2, 'c':3}
#
# sr = pd.Series(dict_data)
#
# print(type(sr), sr, sep = '\n')
#
# list_data = ['2019-01-02', 3.14, 'ABC', 100, True]
#
# print('리스트를 시리즈로 변환하여 변수 sr에 저장', sr, sep = '\n', end = '\n\n')
#
# print('인덱스를 별도로 정의하지않으면, 디폴트로 정수형 위치 인덱스(0,1,2,...)가 자동 지정')
# print(type(sr.index), sr.index, sep='\n')
# print(type(sr.values), sr.values, sep='\n')
# print()
# print('인덱스 배열은 변수 idx에 저장. 데이터 값 배열은 변수 val에 저장')
# [print(idx, val)for idx, val in sr.items()]
#
# tup_data = ('영인', '2010-05-01', '여', True)
# sr = pd.Series(tup_data, index = ['이름', '생년월일', '성별', '학생여부'])
# print(sr)
# print()
#
# print('sr[0] = {}'.format(sr[0]))
# print("sr['이름'] = {}\n".format(sr['이름']))
#
# print("sr[[1,2]]\n{}".format(sr[[1,2]]))
# print("sr[['생년월일', '성별']]\n{}\n".format(sr[['생년월일', '성별']]))
#
# print("sr[1:2]\n{}".format(sr[1:2]))
# print("sr['생년월일':'성별']\n{}".format(sr['생년월일':'성별']))
#
# dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4': [13,14,15]}
#
# df = pd.DataFrame(dict_data)
#
# print(type(df), df, sep = '\n')
#
# df = pd.DataFrame([[15, '남', '덕영중'], [17,'여','수리중']], index=['준서', '예은'], columns=['나이', '성별', '학교'])
#
# print(df, df.index, df.columns, sep = '\n')
# print()
#
# df.index = ['학생1', '학생2']
# df.columns = ['연령', '남녀', '소속']
#
# print(df, df.index, df.columns, sep = '\n')
# print()
#
# df.rename(columns = {'연령':'나이', '남녀': '성별', '소속':'학교'}, inplace=True)
# print(df, df.index, df.columns, sep = '\n')
# print()
#
# df.rename(index = {'학생1':'준서', '학생2': '예은'}, inplace=True)
# print(df, df.index, df.columns, sep = '\n')
# print()
#
# exam_data = {'수학':[90,80,70], '영어':[98,89,95], '음악':[85,95,100], '체육':[100,90,90]}
#
# df = pd.DataFrame(exam_data, index = ['서준', '우현','인아'])
# print(df)
# print()
#
# pd.options.mode.chained_assignment = None
#
# print('inplace = False', 'pd.options.mode.chained_assignment = None')
#
# df2 = df[:]
#
# df3 = df2.drop('우현')
# print('df3', df3, sep = '\n')
# print()
#
# df4 = df[:]
# df5 = df4.drop(['우현', '인아'], axis=0)
# print('\ndf5', df5, sep='\n')
# print()
#
# print("inplace = True", "pd.options.mode.chained_assignment = 'warn'")
# pd.options.mode.chained_assignment = 'warn'
#
# df.drop('인아', inplace= True)
# print("df", df, sep = '\n')
#
# df.drop(['서준', '우현'], axis = 0, inplace= True)
# print('\ndf', df, sep ='\n')

exam_data = {'수학':[90,80,70], '영어':[98,89,95], '음악':[85,95,100], '체육':[100,90,90]}

df = pd.DataFrame(exam_data, index = ['서준', '우현','인아'])
print(df)
print()

pd.options.mode.chained_assignment = None

print('inplace = False', 'pd.options.mode.chained_assignment = None')

df2 = df[:]

df3 = df2.drop('수학', axis=1)
print('df3', df3, sep = '\n')
print()

df4 = df[:]
df5 = df4.drop(['영어', '음악'], axis=1)
print('\ndf5', df5, sep='\n')
print()

print("inplace = True", "pd.options.mode.chained_assignment = 'warn'")
pd.options.mode.chained_assignment = 'warn'

df.drop('수학', axis = 1, inplace= True)
print("df", df, sep = '\n')

df.drop(['영어', '음악'], axis = 1, inplace= True)
print('\ndf', df, sep ='\n')


