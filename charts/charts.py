import matplotlib.pyplot as pyplot

def generate_pie_chart():
  labels = ['A', 'B', 'C']
  values = [11,22,35.4]

  fig, ax = pyplot.subplots()
  ax.pie(values, labels=labels)
  pyplot.savefig('pie.png')
  pyplot.close()