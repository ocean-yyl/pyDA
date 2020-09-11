#1,numpy函数
"""
numpy是数据科学计算的基础模块，用于数值计算
基于数组运算，效率高
拥有许多高级函数，可以对数据进行高效处理
可以进行线性代数相关运算
"""
import numpy as np
a = np.array([x for x in range(10)])
print(a)
print(type(a))
print()
#2,pandas函数
"""
pandas是专门用作数据处理和分析的函数
"""
import pandas as pd
s = pd.Series([1,2,3],index=['a','b','c'])
print(s)

data = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],columns=['a','b','c'])
print(data)

# excel_data = pd.read_excel('')
# csv_data = pd.read_csv('')
print()


#3, matplotlib
"""
Matplotlib 是 Python 的绘图库。 它可与 NumPy 一起使用，提供了一种有效的 MatLab 开源替代方案。 
它也可以和图形工具包一起使用，如 PyQt 和 wxPython。
"""
import matplotlib.pyplot as plt
x = np.linspace(0,10,500) # 创建0-10的等差数列，500个项
print(x)
y = np.sin(x)

plt.plot(x,y,label="y=sinx",color="red",linewidth=2)
plt.xlabel("x_label")
plt.ylabel("y_label")
plt.title("Title")
plt.legend(loc="center") # 图例位置
plt.show()
