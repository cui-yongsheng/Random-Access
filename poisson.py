import numpy as np
import matplotlib.pyplot as plt

# 定义参数
arrival_rate = 5  # 泊松到达过程的强度，表示单位时间内到达的平均次数

# 模拟泊松到达过程
time_interval = 1  # 时间间隔
simulation_time = 100  # 仿真时间
num_simulations = int(simulation_time / time_interval)
arrival_times = np.cumsum(np.random.exponential(scale=1/arrival_rate, size=num_simulations))

# 绘制泊松到达过程
plt.step(arrival_times, range(1, num_simulations + 1), where='post', label='Arrival Times')
plt.xlabel('Time')
plt.ylabel('Number of Arrivals')
plt.title('Poisson Arrival Process Simulation')
plt.legend()
plt.show()
