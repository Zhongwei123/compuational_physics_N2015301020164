# compuational_physics_N2015301020164
## Exercises;
 - [x] [Exercise_01:name](http://upload-images.jianshu.io/upload_images/7918656-61a16e5b4ad9ad63.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
 - [x] [Exercise 02;name moving](https://www.zybuluo.com/mdeditor#894381-full-reader)
 附上效果截图
![](https://github.com/Zhongwei123/compuational_physics_N2015301020164/blob/master/%E5%8A%A8%E5%9B%BE%E7%AC%AC%E4%BA%8C%E6%AC%A1%E4%BD%9C%E4%B8%9A.gif.gif)
- [x] [Exercise 03;chapter1 T3]
# 第三次做业
##《计算物理》第一章课后习题3
---
一. 课题
It is often the case that the frictional force on an object will increase as object moves faster. A fortunate example of this is a parachutist; the role of the parachute is to produce a frictional force due to air drag, which is narmally larger than would normally be the case without the parachute. Here we consider a very simple examle in which the frictional force depends on the velocity. Assume that the velocity of a object obeys the equation of the form
         $$dv/dt=a-bv$$
Where a and b are constants. You could think of a as coming from an applied force, such as gravity, while b arises from friction. Note that the frictional force is negative(we asume that b>0), so that it opposes the motion. Use the Euler method to solve for v as a function of time. A convenient choice of parameters is a=10 and b=1. You should find that v apporaches a as a constant value at long times; This is called the terminal velocity.

---
###二.实验目的
1 用欧拉法拟合出速度随时间的变化，并用mathplotile在python上绘出
2 该速度微分方程可以轻松算出解析解，同样地绘出解析解的速度随时间变化的曲线
3 观察收尾速度
4 改变a与b的设定值，观察变化

---
###三.源代码
   *本有四段代码，但区别是改变a与b的设定值， 故不重复粘贴
```python
   @author: 钟伟
"""

import numpy as np
import matplotlib.pyplot as plt

a = 10  
b = 1
"""设置初始条件"""
vi = int(input("please input the initial velovity:")) 
"""输入初始速度"""
t = 0
delt_t = 0.1
process_v = vi

"""设定两个列表储存数据"""
list_v=[process_v,] 
list_t=[t,]

"""进行计算，并将计算结果储存在列表中"""
while t<4:
    process_v = process_v + (a-b*process_v)*delt_t 
    """欧拉法计算"""
    t=t+delt_t
    list_v.append(process_v)
    list_t.append(t)

"""解析解的方程由积分法求出"""    
c=a-b*vi
t=np.linspace(0,4,1000)
v=(a-c*np.exp(-b*t))/b

"""画出图像"""
plt.figure(figsize=(50,25))
plt.plot(list_t,list_v,label="$v(t)$",marker='s')
plt.plot(t,v,linewidth=2,color="yellow")
plt.xlabel("Time(s)")
plt.ylabel("velocity(m/s)")
plt.title("velocity variation")
plt.ylim(0,11)
plt.legend()
plt.show()
```
创建时间
 Sep 28 15:46:29 2017
 
 ---
###三.调试及结果
*均为v=1 a=10 模拟业余跳伞刚一跳就迫不及待打开伞 重力加速度为10m/s

1.b=1
