import pygal
from die import Die

#创建两个筛子
die_1 = Die()
die_2 = Die(10)

results = []
for roll_num in range(50000):
    result = die_1.roll()+ die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2,max_result+1):
    f = results.count(value)
    frequencies.append(f)

print(frequencies)
hist = pygal.Bar()
hist.title = "Results of rolling a D6 and a D10 50000times."
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
hist.x_title = "Results"
hist.y_title = "Frequency of result"

hist.add('D6+D10',frequencies)
hist.render_to_file('dice_visual.svg')







