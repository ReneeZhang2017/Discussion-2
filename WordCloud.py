from wordcloud import WordCloud
import matplotlib.pyplot as plt
from imageio import imread

t=open('speech.txt').read()
mask = imread("China_map.jpg") #upload a a map of China and use it as my background.
picture = WordCloud(mask = mask,background_color = "white",margin=1).generate(t)
plt.imshow(picture)
plt.axis("off")
plt.show()

import pandas as pd
df = pd.DataFrame(
    {'Key_words':["development", "party", "people", "system", "chinese",  "socialist", "reform", "promote","world", "economic"]}
                 )
import collections
m=collections.Counter(t)
df["WordCount"]=[m['development'],m['party'],m['people'],m['system'],m['chinese'],m['socialist'],m['reform'],m['promote'],m['world'],m['economic']]
df

df.plot(kind='bar',x='Key_words',y='WordCount')
plt.title("Present Xi's Speech" ,fontsize=14, color='red')
plt.xlabel('Key_words')
plt.ylabel('WordCount')



