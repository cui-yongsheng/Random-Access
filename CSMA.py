import numpy as np
import matplotlib.pyplot as plt

class CSMA:
    def __init__(self, num_nodes, transmission_probability, simulation_time):
        self.num_nodes = num_nodes
        self.transmission_probability = transmission_probability
        self.simulation_time = simulation_time
        self.node_status = np.zeros(num_nodes)  # 0表示空闲，1表示发送中
        self.transmission_attempts = np.zeros(num_nodes)  # 记录发送尝试次数

    def listen_channel(self):
        return np.sum(self.node_status) > 0  # 如果有节点在发送，则信道忙碌

    def simulate(self):
        for time in range(self.simulation_time):
            # 每个节点决定是否发送
            for node in range(self.num_nodes):
                if np.random.rand() < self.transmission_probability and self.node_status[node] == 0:
                    self.node_status[node] = 1  # 发送数据
                    self.transmission_attempts[node] += 1  # 记录尝试次数

            # 检测冲突
            if self.listen_channel():
                # 发生冲突，所有发送中的节点重新尝试
                for node in range(self.num_nodes):
                    if self.node_status[node] == 1:
                        self.node_status[node] = 0
                        self.transmission_attempts[node] += 1

            # 节点状态更新
            self.node_status = np.maximum(0, self.node_status - 1)

if __name__ == "__main__":
    num_nodes = 10
    transmission_probability = 0.5
    simulation_time = 1000

    csma_simulation = CSMA(num_nodes, transmission_probability, simulation_time)
    csma_simulation.simulate()
    

    # 显示结果
    print('CSMA仿真结果:')
    print('总发送尝试次数:', np.sum(csma_simulation.transmission_attempts))
    print('平均尝试次数:', np.mean(csma_simulation.transmission_attempts))

    # 绘制节点的发送尝试次数直方图
    plt.hist(csma_simulation.transmission_attempts, bins=range(1, int(np.max(csma_simulation.transmission_attempts)) + 2), align='left')
    plt.title('CSMA仿真结果')
    plt.xlabel('发送尝试次数')
    plt.ylabel('节点数量')
    plt.show()