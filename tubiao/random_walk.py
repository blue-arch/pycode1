from random import choice
class RandomWalk():
    '''一个生成随机漫步数据的类'''
    def __init__(self,num_points = 5000):
        '''初始化漫步随机属性'''
        self.num_points = num_points
        #所以随机漫步始于（0，0）
        self.x_values = [0]
        self.y_values = [0]
    def fill_walk(self):

        while len(self.x_values) < self.num_points:
            #决定前进的方向以及距离
            x_direction = choice([1,-1])
            x_diatance = choice([0,1,2,3,4])
            x_step = x_direction * x_diatance

            y_direction = choice([1, -1])
            y_diatance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_diatance

            #拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            #计算下一个点的x,y值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)




