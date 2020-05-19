# coding:utf-8

import re
import requests
import tkinter as tk
import webbrowser

url = 'http://www.qmaile.com/'

response = requests.get(url)
response = response.text
# print(response.content.decode('utf-8'))

# 数据提取
res = re.compile('<option value="(.*?)" selected')

reg = re.findall(res, response) # 返回列表 接口URL


# 画布
root = tk.Tk()
root.title('嘟嘟VIP影视播放')
root.geometry('500x250+200+200')
l1 = tk.Label(root, text="播放接口", font=("Araial", 12))
l1.grid()
l2 = tk.Label(root, text="播放链接", font=("Araial", 12))
l2.grid(row=6, column=0)
t1 = tk.Entry(root, text='', width=50)
t1.grid(row=6, column=1)
one = reg[0]
two = reg[1]
three = reg[2]
four = reg[3]
five = reg[4]

var = tk.StringVar()
var.set(one)
r1 = tk.Radiobutton(root, text='播放接口1', variable=var, value=one)
r2 = tk.Radiobutton(root, text='播放接口2', variable=var, value=two)
r3 = tk.Radiobutton(root, text='播放接口3', variable=var, value=three)
r4 = tk.Radiobutton(root, text='播放接口4', variable=var, value=four)


r1.grid(row=0, column=1)
r2.grid(row=1, column=1)
r3.grid(row=2, column=1)
r4.grid(row=3, column=1)


def del_text():
    t1.delete(0, 'end')


def play():
    webbrowser.open(var.get() + t1.get())


b1 = tk.Button(root, text="播放", font=("Arial", 10), width=8, command=play)
b1.grid(row=7, column=1)

b2 = tk.Button(root, text="清除", font=("Arial", 10), width=8, command=del_text)
b2.grid(row=9, column=1)


# 消息循环
root.mainloop()






