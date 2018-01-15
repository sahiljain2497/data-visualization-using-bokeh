from bokeh.plotting import figure,output_file,show
import xlrd

o=figure(plot_width=500,plot_height=500)
book=xlrd.open_workbook("./verlegenhuken.xlsx")
sheet=book.sheet_by_index(0)
x=[]
y=[]
for i in  range(1,sheet.nrows):
    for j in range(sheet.ncols-2,sheet.ncols):
        if j == sheet.ncols-2 :
            x.append(int(sheet.cell(i,j).value)/10)
        else :
            y.append(int(sheet.cell(i,j).value)/10)
#print(x,y)
o.title.text="Temperature and Air Pressure"
o.circle(x,y,size=5,color="blue")
output_file("Graph.html")
show(o)
