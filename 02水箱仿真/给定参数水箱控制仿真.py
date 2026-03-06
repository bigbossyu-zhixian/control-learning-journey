"""
项目名称：一阶水箱液位控制系统仿真
    作者：bigboss
    时间：2026-3-04

    
项目目的：
建立单水箱液位动态模型，并在给定参数条件下，
利用数值方法模拟液位随时间变化过程。


数学模型：
A*dh/dt=u-k*h
其中：
A -- 水箱横截面积（截面积）
u -- 进水流量（控制输入）
k*h -- 出水流量（与液位成比例）


核心概念：
1、一阶线性微分方程
2、动态过程与稳态平衡
3、数值积分方法（Euler显示法）


学习目标：
1、理解物理系统并转化为数学模型（微分方程）
2、理解稳态条件 dh/dt=0 的物理意义
3、使用欧拉法近似连续系统   
"""
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['Arial Unicode MS']
A=1 # 水箱截面积
k=0.5 # 出水量系数，与水位高度有关
T=10 
u=1 # 进水流量（控制输入）
dt=0.01 # 步长，用欧拉法来表示时的精度要求
t=np.arange(0,T,dt) # 生成数组，在0～10秒内取的时间点
h=np.zeros(len(t)) # 全零数组，后续迭代中能保存每一轮迭代后的数值
for i in range(len(t)-1): # 后续迭代过程中，因为取了i+1所以i的值要控制不能超过h数组的值“len（t）”
    d_h=(u-k*h[i])/A # 当前时刻液位变化率。单独定义，便于后续修改以及调整；“[]”对数组的内容进行索引
    h[i+1]=h[i]+dt*d_h
plt.plot(t,h,label="h(t)") # 因为只有一个函数图像，没有将其设置为局部变量形式，直接画出图像
plt.xlabel("t(s)")
plt.ylabel("h(m)")
plt.title("水箱控制仿真")
plt.legend()
plt.grid(True)
plt.show()
