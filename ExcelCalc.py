import xlrd
year = ['2011','2012','2013','2014']
dates = ['ianouario','fevrouario','martio','aprilio','maio','iounio','ioulio','augousto','septemvrio','oktovrio','noemvrio','dekemvrio']
TouristsPerYear = []
for z in range(4):
    wb = xlrd.open_workbook(f'afikseis_kai_mesa_metaforas{z}.xls')
    sheet = wb.sheet_by_index(11)
    if z == 0:
        TouristsPerYear.append(int(sheet.cell_value(134,6)))
    else :
        TouristsPerYear.append(int(sheet.cell_value(136,6)))
#To TouristPerYear exei tis plhrofories gia to zhtoumeno 1
#print("TOP 5 COUNTRIES WITH MOST VISITORS IN 2011")
country2011=[]
value2011=[]
excelopen0 = xlrd.open_workbook("afikseis_kai_mesa_metaforas0.xls")
sheet1 = excelopen0.sheet_by_index(11)
 #France
country2011.append(sheet1.cell_value(79,1))
value2011.append(int(sheet1.cell_value(79,6)))
 #Germany
country2011.append(sheet1.cell_value(80,1))
value2011.append(int(sheet1.cell_value(80,6)))
 #UK
country2011.append(sheet1.cell_value(83,1))
value2011.append(int(sheet1.cell_value(83,6)))
 #Italy
country2011.append(sheet1.cell_value(86,1))
value2011.append(int(sheet1.cell_value(86,6)))
#Russia
country2011.append(sheet1.cell_value(106,1))
value2011.append(int(sheet1.cell_value(106,6)))

#print("TOP 5 COUNTRIES WITH MOST VISITORS IN 2012")
country2012 = []
value2012 = []
excelopen1 = xlrd.open_workbook("afikseis_kai_mesa_metaforas1.xls")
sheet2 = excelopen1.sheet_by_index(11)
#France
country2012.append(sheet2.cell_value(81,1))
value2012.append(int(sheet2.cell_value(81,6)))
#Germany
country2012.append(sheet2.cell_value(82,1))
value2012.append(int(sheet2.cell_value(82,6)))
#UK
country2012.append(sheet2.cell_value(85,1))
value2012.append(int(sheet2.cell_value(85,6)))
#Italy
country2012.append(sheet2.cell_value(88,1))
value2012.append(int(sheet2.cell_value(88,6)))
#Russia
country2012.append(sheet2.cell_value(108,1))
value2012.append(int(sheet2.cell_value(108,6)))

#print("TOP 5 COUNTRIES WITH MOST VISITORS IN 2013")
country2013 = []
value2013 = []
excelopen2 = xlrd.open_workbook("afikseis_kai_mesa_metaforas2.xls")
sheet3 = excelopen2.sheet_by_index(11)
#France
country2013.append(sheet3.cell_value(81,1))
value2013.append(int(sheet3.cell_value(81,6)))
#Germany
country2013.append(sheet3.cell_value(82,1))
value2013.append(int(sheet3.cell_value(82,6)))
#UK
country2013.append(sheet3.cell_value(85,1))
value2013.append(int(sheet3.cell_value(85,6)))
#Italy
country2013.append(sheet3.cell_value(88,1))
value2013.append(int(sheet3.cell_value(88,6)))
#Russia
country2013.append(sheet3.cell_value(109,1))
value2013.append(int(sheet3.cell_value(109,6)))

#print("TOP 5 COUNTRIES WITH MOST VISITORS IN 2014")
country2014 = []
value2014 = []
excelopen3 =xlrd.open_workbook("afikseis_kai_mesa_metaforas3.xls")
sheet4 = excelopen3.sheet_by_index(11)
#France
country2014.append(sheet4.cell_value(81,1))
value2014.append(int(sheet4.cell_value(81,6)))
#Germany
country2014.append(sheet4.cell_value(82,1))
value2014.append(int(sheet4.cell_value(82,6)))
#UK
country2014.append(sheet4.cell_value(85,1))
value2014.append(int(sheet4.cell_value(85,6)))
#Italy
country2014.append(sheet4.cell_value(88,1))
value2014.append(int(sheet4.cell_value(88,6)))
#Russia
country2014.append(sheet4.cell_value(109,1))
value2014.append(int(sheet4.cell_value(109,6)))

countries = [country2011,country2012,country2013,country2014]    #countries kai values einai ta array pou exoun tis plhrofories gia to zhtoumeno 2
values = [value2011,value2012,value2013,value2014]

for i in range(len(countries)):
    for z in range(len(country2011)):
        print(countries[i][z],values[i][z],year[i])

#Afikseis touriston stin ellada ana meso metaforas
TransportArray=[ [], [] ,[] ,[] ]
for i in range(4):
    openexceltest = xlrd.open_workbook(f"afikseis_kai_mesa_metaforas{i}.xls")
    selida = openexceltest.sheet_by_index(11)
    if i==0 :
        for k in range(2,6):
            TransportArray[0].append(int(selida.cell_value(134,k)))
    else:
        for z in range(2,6):
            TransportArray[i].append(int(selida.cell_value(136,z)))

transport = ["aeroporikos","sidirodromikos","thallasios","odikos"] # transport,TrasnportArray,year  einai ta array pou exoun tis plhrofories gia to zhtoumeno 3
for r in range(4):
    for o in range(4):
        print(year[r],transport[o],TransportArray[r][o])

#afikseis touriston sthn ellada ana trimino
trimina = [ [],[],[],[] ]
def myfunction(anexcel,year):
    if anexcel=="afikseis_kai_mesa_metaforas2.xls":
        xlsopen=xlrd.open_workbook(anexcel)
        temparray=[]
        for i in range(12):
            sheet = xlsopen.sheet_by_index(i)
            if i == 0 or i == 1 or i == 2 or i == 3 or i == 4 or i == 5:
                temparray.append(int(sheet.cell_value(64, 6)))
            else:
                temparray.append(int(sheet.cell_value(65, 6)))
        for z in range(0, 12, 3):
            trimina[2].append(sum(temparray[z:z + 3]))
    else:
        xlsopen=xlrd.open_workbook(anexcel)
        temparray=[]
        for i in range(12):
            sheet=xlsopen.sheet_by_index(i)
            temparray.append(int(sheet.cell_value(65,6)))
        for z in range(0, 12, 3):
            trimina[year].append(sum(temparray[z:z + 3]))
myfunction("afikseis_kai_mesa_metaforas0.xls",0)
myfunction("afikseis_kai_mesa_metaforas1.xls",1)
myfunction("afikseis_kai_mesa_metaforas2.xls",2)
myfunction("afikseis_kai_mesa_metaforas3.xls",3)
#to array trimina exei tis plhrofories gia to zhtoumeno 4