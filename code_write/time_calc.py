'''import time as t

class Mytimer():

    def __init__(self):
        self.lasted = []
        self.start1 = 0
        self.stop1 = 0
        self.prompt = '未开始计时'
        self.unit = ['年','月','日','时','分','秒']

    def __str__(self):
        return self.prompt

    __repr__ = __str__

    # 不继承int,str...类还可以用add?????
    def __add__(self, other):
        prompt = '总共运行了'
        result = []
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index])
            if result[index]:
                prompt += (str(result[index]) + self.unit[index])
        return prompt


    def start(self):
        self.start1 = t.localtime()
        print('计时开始：')

    def stop(self):
        self.stop1 = t.localtime()
        self._calc()
        print('计时结束：')

    def _calc(self):
        self.lasted = []
        self.prompt = '总共运行了'
        for index in range(6):
            self.lasted.append(self.stop1[index] - self.start1[index])
            if self.lasted[index]:
                self.prompt += str(self.lasted[index])+self.unit[index]


t1 = Mytimer()
t1.start()
t.sleep(5)
t1.stop()'''



import time as t


class MyTimer:
    def __init__(self):
        self.unit = ['年', '月', '天', '小时', '分钟', '秒']
        self.prompt = "未开始计时！"
        self.lasted = []
        self.begin = 0
        self.end = 0

    # 开始计时
    def start(self):
        self.begin = t.localtime()
        self.prompt = "提示：请先调用stop()结束计时！"
        print("计时开始……")

    # 停止计时
    def stop(self):
        if not self.begin:
            print("提示：请先调用start()开始计时！")
        else:
            self.end = t.localtime()
            self._calc()
            print("计时结束！")

    # 内部方法，计算运行时间
    def _calc(self):
        self.lasted = []
        self.prompt = "总共运行了"
        for index in range(6):
            self.lasted.append(self.end[index] - self.begin[index])
            if self.lasted[index]:
                self.prompt += (str(self.lasted[index]) + self.unit[index])
        # 为下一轮计算初始化变量
        self.begin = 0
        self.end = 0
        print(self.prompt)

    # 调用实例直接显示结果
    def __str__(self):
        return self.prompt
    __repr__ = __str__

    # 计算两次计时器对象之和
    def __add__(self, other):
        prompt = "总共运行了"
        result = []
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index])
            if result[index]:
                prompt += (str(result[index]) + self.unit[index])
        return prompt

t1 = MyTimer()
t2 = MyTimer()
t1.start()
t.sleep(45)
t1.stop()
t2.start()
t.sleep(15)
t2.stop()
print(t1 + t2)























