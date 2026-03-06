"""
项目名称：一阶系统时间常数对指数相应的影响
    作者：bigboss
    日期：2026-03-04

    
项目目的：
    通过绘制不同时间常数 tau 下的指数衰减曲线，
    理解时间常数对系统响应快慢的影响。

    
核心概念：
    一阶系统响应形式：
    y(t)=e^(-t/tau)


学习目标：
    1、熟悉 numpy 数组计算
    2、理解 for 循环在参数扫描中的作用
    3、建立 tau 与系统动态特性的物理联系
"""
import numpy as np # 将numpy名称简化一下
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['Arial Unicode MS'] # mac电脑中识别不出中文，会乱码,写上这句就不会了
plt.rcParams["axes.unicode_minus"]=False # 画出的图像中能出现负号
taus=(0.5,1,2) # 设置不同时间参数，用于比较系统响应快慢
t=np.linspace(0,5,100) # 在0～5秒之前取100个时间点（用于画连续曲线）
plt.figure(figsize=(7,5))
for tau in taus: # for循环下，就能画出tau不同下的图像
    y=np.exp(-t/tau) # 指数函数，对应的是一阶系统单位响应的数学表达式
    plt.plot(t,y,label=f'tau={tau}',linewidth=2) # f‘{}'表示格式化字符串，{}里放变量、表达式、函数调用，程序运行时会把花括号里的内容计算结果替换到字符串中
plt.xlabel("Time") # x轴名称
plt.ylabel("y(t)") # y轴名称
plt.title("一阶系统指数衰减响应") # 整个函数图像名称
plt.legend() # 显示图例
plt.grid(True) # 显示网格线
plt.show()  # 只有写上这个命令才能显示图像
