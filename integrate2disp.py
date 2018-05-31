# Integrates from velocity to displacement
from obspy import read
from bokeh.plotting import figure, output_file, show
from bokeh.palettes import Set1_3, Set1_4
from bokeh.layouts import column
from scipy import integrate

input_path = 'E:\project_amanah\S3\earthquake\dataset-avicenna\panyaungan2018\panyaungan2018-2.miniseed'

st = read(input_path)
print(st.__str__(extended=True))

print(st[0].stats)
print(st[3].stats)

print(st[0].data)

# disp_bhe = integrate(st[0].data)
disp_bhe = integrate.simps(st[0].data)
print('disp_bhe=%s' % disp_bhe)

# output to static HTML file
output_file("integrate2disp.html")

# create a new plot with a title and axis labels
p = figure(title="%s.%s %s Hz %s" % (st[0].stats.network, st[0].stats.station, st[0].stats.sampling_rate, st[0].stats.starttime),
           x_axis_label='sample', y_axis_label='velocity',
           plot_height=120)
p.sizing_mode = 'scale_width'

# add a line renderer with legend and line thickness
#p.line(x, y, legend="Temp.", line_width=2)
p.line(range(len(st[0].data)), st[0].data, color=Set1_3[0], legend=st[0].stats.channel)
p.line(range(len(st[1].data)), st[1].data, color=Set1_3[1], legend=st[1].stats.channel)
p.line(range(len(st[2].data)), st[2].data, color=Set1_3[2], legend=st[2].stats.channel)

p_disp = figure(title="DISP",
           x_axis_label='sample', y_axis_label='displacement',
           plot_height=120)
p_disp.sizing_mode = 'scale_width'
p_disp.line(range(len(disp_bhe)), disp_bhe, color=Set1_4[3], legend=st[0].stats.channel)

# show the results
show(column(p, p_disp, sizing_mode='scale_width'))
