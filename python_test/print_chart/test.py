from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF
from reportlab.lib import colors

data = [
#    -----Sunspot Number------
# YR MO     PREDICTED    HIGH    LOW   
#-----------------------------------
(2017, 10,    10.4,    11.4,     9.4),
(2017, 11,    10.4,    12.4,     8.4),
(2017, 12,    10.6,    13.6,     7.6),
(2018, 1,     10.8,    15.8,     5.8),
(2018, 2,     10.6,    15.6,     5.6),
(2018, 3,     9.6,     15.6,     3.6),
(2018, 4,     9.1,     16.1,     2.1),
(2018, 5,     9.5,     16.5,     2.5),
(2018, 6,     10.0,    18.0,     2.0),
(2018, 7,     10.4,    19.4,     1.4),
(2018, 8,     10.7,    19.7,     1.7),
(2018, 9,     11.0,    21.0,     1.0),
(2018, 11,    10.1,    20.1,     0.1),
(2018, 12,    9.5,     19.5,     0.0),
(2019, 1,     8.9,     18.9,     0.0),
(2019, 2,     8.3,     18.3,     0.0),
(2019, 3,     7.8,     17.8,     0.0),
(2019, 4,     7.3,     17.3,     0.0),
(2019, 5,     6.8,     16.8,     0.0),
(2019, 6,     6.4,     16.4,     0.0),
(2019, 7,     5.9,     15.9,     0.0),
(2019, 8,     5.5,     15.5,     0.0),
(2019, 9,     5.1,     15.1,     0.0),
(2019, 10,    4.8,     14.8,     0.0),
(2019, 11,    4.4,     14.4,     0.0),
(2019, 12,    4.1,     14.1,     0.0)
	]

drawing =Drawing(200,150)

pred = [row[2]+40 for row in data]
high = [row[3]+40 for row in data]
low = [row[4]+40 for row in data]
times = [40*((row[0]+row[1]/12.0)-2017) for row in data]

drawing.add(PolyLine(list(zip(times,pred)),strokeColor=colors.blue))
drawing.add(PolyLine(list(zip(times,high)),strokeColor=colors.red))
drawing.add(PolyLine(list(zip(times,low)),strokeColor=colors.green))

drawing.add(String(65,115,'Sunspots',fontSize=18,fillColor=colors.red))
renderPDF.drawToFile(drawing,'report1.pdf','Sunspots')