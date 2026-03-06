# Control Learning Journey
This repository records my learning process of control systems and Python simulation.
The goal of this project is not only to write code,but to understand the physical meaning and mathematical models behind control systems.
---
# Learning Structure
## 01 Python Basics
Basics Python exercises and plotting using numpy and matplotlib.
 
Content:
- Python syntax practice
- Function plotting
- Numerical arrays
---
## 02 Tank System Simulation
A first-order water tank system simulation.

Physical model:
Water level change = Inflow -Outflow

Mathematical model:
A * dh/dt = u - k*h

Simulation goals:
- Simulation water level response over time
- Study the influence of parameters
- Understand time constant of first-order systems
---
# Purpose Of This Project
The purpose of this repository is:
- Learn Python for scientific computing
- Understand control system modeling
- Connect physics,mathematics and programming
## 系统结构图

```mermaid
flowchart TD

A[输入参数<br>u: 进水流量<br>A: 水箱截面积<br>k: 出水系数<br>h0: 初始水位]

B[水箱数学模型<br>dh/dt = (u - k√h) / A]

C[Python数值仿真<br>Euler积分]

D[得到水位变化曲线<br>h(t)]

A --> B
B --> C
C --> D
```
