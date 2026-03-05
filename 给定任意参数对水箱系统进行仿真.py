"""
项目名称：一阶水箱液位系统函数化建模
    作者：bigboss
    时间：2026-3-05


项目目的：
将水箱动态模型封装为函数形式，
实现参数可调的数值仿真模型，
并引入初始条件分析系统响应。


学习目标：
1、区分局部变量和全局变量
2、为后续引入反馈控制做准备
"""
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['Arial Unicode MS']
def fun(u,k,A,h0,dt=0.01,T=10): # u、k、A、dt、T同前，h0为初始水位
    t=np.arange(0,T,dt)
    h=np.zeros(len(t))
    h[0]=h0
    for i in range(len(t)-1):
        dh=(u-k*h[i])/A
        h[i+1]=h[i]+dh*dt
    return t,h # 函数负责计算，return使内部计算好的数组h、t能被外部调用（返回时间序列与液位响应，供外部调用与分析）
t,h=fun(4,0.5,5,10,0.01,50)
plt.plot(t,h,label="水位h(t)") # 给定参数后，外部负责绘图，计算与展示分离
plt.xlabel("t(s)")
plt.ylabel("h(m)")
plt.grid(True)
plt.title("水箱控制仿真")
plt.legend()
plt.show()

