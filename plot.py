#!/usr/bin/env python3
"""
平面上の2点に存在する点電荷の電気力線をプロットするコード
電荷q1 := 1の座標(x1, y1) := (1, 0)
電荷q2 := -1の座標(x2, y2) := (-1, 0)
Copyright (C) 2023 Yoshikawa Teru
This code is released under the MIT License.
"""

# 必要なライブラリのインポート
import numpy as np
import matplotlib.pyplot as plt

# 座標系の作成
N = 300 # メッシュグリッドの分割数
L = 4 # メッシュグリッドの範囲
x = np.linspace(-L, L, N + 1) # xの範囲
y = np.linspace(-L, L, N + 1) # yの範囲
X, Y = np.meshgrid(x, y) # メッシュグリッドの生成

# 点電荷の位置と電荷量
q1, x1, y1 = 1, 1, 0 # 点電荷 1つ目
q2, x2, y2 = -1, -1, 0 # 点電荷 2つ目

# 各点での電場の成分を計算
k = 9 * 10 ** 9# クーロン定数
Ex = k * q1 * (X - x1) / ((X - x1)**2 + (Y - y1)**2)**(3/2) + k * q2 * (X - x2) / ((X - x2)**2 + (Y - y2)**2)**(3/2)
Ey = k * q1 * (Y - y1) / ((X - x1)**2 + (Y - y1)**2)**(3/2) + k * q2 * (Y - y2) / ((X - x2)**2 + (Y - y2)**2)**(3/2)

# 電気力線の始点を決める
n = 12 # 電気力線の本数
theta = np.linspace(0, 2*np.pi, n + 1)
x_start = 0.1 * np.cos(theta)
y_start = 0.1 * np.sin(theta)
x_start = np.concatenate([x1 + x_start, x2 + x_start])
y_start = np.concatenate([y1 + y_start, y2 + y_start])
points = np.array([x_start, y_start]).T

# plt.plot(x_start, y_start, marker='o', markersize=10, color='red')

# 電気力線をプロット
plt.streamplot(X, Y, Ex, Ey, start_points=points, density=10, color = np.sqrt(Ex**2 + Ey**2), cmap='jet', arrowsize=1.5)

# 点電荷の位置をプロット
plt.plot(x1, y1, marker='o', markersize=15, color='yellow')
plt.plot(x2, y2, marker='o', markersize=15, color='yellow')
plt.plot(x1, y1, marker='+', markersize=10, color='red')
plt.plot(x2, y2, marker='_', markersize=10, color='blue')

# グラフの設定
plt.title('line of electric force')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim([-L, L])
plt.ylim([-L, L])
plt.grid()
plt.savefig("line-of-electric-force.png")
plt.show()
