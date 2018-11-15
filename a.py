#movielens 1m 数据集含有来自6000ing用户对4000部电影的100万条评分数据。它分成三个表：评分、用户信息和电影信息。
#将该数据从zip文件中解压出来之后，可以通过pandas.read_table将各个表分别读到一个pandas dataframe对象中：
import pandas as pd
unames = ['user_id','gender','age','occupation','zip']
users = pd.read_table('C:/Users/Teddy/Desktop/jupyter notebook/users.dat',sep='::',header=None,names=unames,engine='python')
print(users)

rnames = ['user_id','movie_id','rating','timestamp']
ratings = pd.read_table('C:/Users/Teddy/Desktop/jupyter notebook/ratings.dat',sep='::',header=None,names=rnames,engine='python')
print(ratings)

mnames = ['movie_id','title','genres']
movies = pd.read_table('C:/Users/Teddy/Desktop/jupyter notebook/movies.dat',sep='::',header=None,names=mnames,engine='python')
print(movies)

#利用python的切片语法，通过查看每个DATAframe的前几行即可验证数据加载工作是否成功：

np(names.groupby(['year','sex']).prop.sum(),1)

movies.to


frame4 = pd.DataFrame(pop,index=(2))
print(frame4)
frame4.to_html()