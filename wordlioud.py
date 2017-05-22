#coding:utf-8
from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt
import jieba
import codecs
from wordcloud import WordCloud, ImageColorGenerator

# 获取当前文件路径
# __file__ 为当前文件, 在ide中运行此行会报错,可改为
# d = path.dirname('.')
d = path.dirname(__file__)
# 读取文本 alice.txt 在包文件的example目录下
text = open(path.join(d, 'alice.txt')).read()
#中文分割
cut_text = " ".join(jieba.cut(text))
# read the mask / color image
# 设置背景图片
alice_coloring = imread(path.join(d, "love.png"))

wc = WordCloud(
    #设置中文字体
    font_path="HYQiHei-25J.ttf",
    #背景颜色
    background_color="white",
    #词云显示的最大词数
    max_words=200,
    #设置背景图片
    mask=alice_coloring,
    #字体最大值
    max_font_size=80,
)
# 生成词云,也可以我们计算好词频后使用generate_from_frequencies函数
wc.generate(cut_text)

#fre = {u'吃饭':100,u'睡觉':20,u'打豆豆':80}
# 不加u会乱码
#wc.generate_from_frequencies(fre)

#从背景图片生成颜色值
image_colors = ImageColorGenerator(alice_coloring)
# 显示默认词云
plt.imshow(wc)
plt.axis("off")
# 绘制以图片色彩为背景的词云
plt.figure()
plt.imshow(wc.recolor(color_func=image_colors))
plt.axis("off")
# 绘制原图像
#plt.figure()
#plt.imshow(alice_coloring, cmap=plt.cm.gray)
#plt.axis("off")
plt.show()
# 保存图片
wc.to_file(path.join(d, "LOVE.png"))