from die import Die
import pygal

die = Die()
results = []
for roll_num in range(10000):
    result = die.roll()
    results.append(result)

frequencies = []
for value in range(1,die.num_sides+1):
    f = results.count(value)
    frequencies.append(f)

print(frequencies)
hist = pygal.Bar()
hist.title = "Results of rolling one D6 10000times."
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = "Results"
hist.y_title = "Frequency of result"

hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')

