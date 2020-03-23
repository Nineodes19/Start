"""
输入三角形三体边的边长，计算三角形的面积
"""
import math
side1 = float(input('请输入三角形的边长a：'))
side2 = float(input('请输入三角形的边长b：'))
side3 = float(input('请输入三角形的边长c：'))

S = (side1 + side2 + side3) / 2
area = (S*(S-side1) * (S - side2) * (S - side3)) ** 0.5
print('三角形三边分别为：a=',side1,'b=',side2,'c=',side3)
print('三角形的面积是：',area)