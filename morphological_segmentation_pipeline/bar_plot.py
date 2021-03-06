# # %matplotlib inline
# import matplotlib.pyplot as plt
# import numpy as np 

# x = range(100)
# y = range(100,200)
# fig = plt.figure(figsize=(30, 20), dpi=100)
# ax = fig.add_subplot(111)

# from xlrd import open_workbook
# wb = open_workbook('/Volumes/Studies/LEGmuscle/Result/legVolume_2Jan2018.xlsx')
# for s in wb.sheets():
#     #print 'Sheet:',s.name
#     values = []
#     for row in range(s.nrows):
#         col_value = []
#         for col in range(s.ncols):
#             value  = (s.cell(row,col).value)
#             try : value = str(double(value))
#             except : pass
#             col_value.append(value)
#         values.append(col_value)
# data = np.array(values)


# markers=[',', '+', '_', '.', 'o', '*', 'p', 's', 'x', 'h', '^', 'D']
# marker_count = 0
# subject = [2,4,5,6,7,9,10,11,12,13,14,15]
# sub = [2,4,5,6,7,9,12,13,14,15]
# subject_tp=[3,3,3,5,5,3,1,1,3,3,3,3]
# s_tp=[3,3,3,5,5,3,3,3,3,3]

# width = 0.35       # the width of the bars
# ind = np.arange(len(s_tp))

# increase = []
# row_count = 1
# s_count = 0
# sub_change=[]
# for i in subject:
# # for i in range(1):
#     row_count += 1
#     print(row_count)
#     if subject_tp[s_count] > 1:
#         row_count+=1
#         print('subject',s_count)
#         temp = 0
#         count = 0
#         for j in range(subject_tp[s_count]-1):
#             print(data[row_count+j][6])
#             print(data[row_count+j][13])
#             print('j',j)
#             print(row_count+j)
#             if ((float(data[row_count+j][6]) <=0.4)):
#                 temp = temp + (float(data[row_count+j][6])) * 100
#                 count += 1
#             if ((float(data[row_count+j][13]) <=0.4)):
#                 temp = temp + (float(data[row_count+j][13])) * 100
#                 count += 1
        
#         temp = temp/count
#         print(temp)
#         increase.append(temp)
#     else:
#         row_count += 1
#     row_count = row_count + subject_tp[s_count] - 1
#     s_count += 1
    
# rect = ax.bar(np.arange(len(increase)), increase, width, color='r')

# def autolabel(rects):
#     """
#     Attach a text label above each bar displaying its height
#     """
#     for rect in rects:
#         height = rect.get_height()
#         ax.text(rect.get_x() + rect.get_width()/2., 1.01*height,'%.4f' % float(height),ha='center', va='bottom')
            

# autolabel(rect)

# ax.set_ylabel('Average Increase %')
# ax.set_xlabel('Subject')                
# ax.set_title('Average Increase % of subjects')

# print(len(increase))

# ax.set_xticks(np.arange(len(increase)))
# ax.set_xticklabels(sub)

# plt.show()


import matplotlib.pyplot as plt
import numpy as np 

x = range(100)
y = range(100,200)
fig = plt.figure(figsize=(30, 20), dpi=100)
ax = fig.add_subplot(111)

from xlrd import open_workbook
wb = open_workbook('/Volumes/Studies/LEGmuscle/Result/legVolume_2Jan2018.xlsx')
for s in wb.sheets():
    #print 'Sheet:',s.name
    values = []
    for row in range(s.nrows):
        col_value = []
        for col in range(s.ncols):
            value  = (s.cell(row,col).value)
            try : value = str(double(value))
            except : pass
            col_value.append(value)
        values.append(col_value)
data = np.array(values)


markers=[',', '+', '_', '.', 'o', '*', 'p', 's', 'x', 'h', '^', 'D']
marker_count = 0
subject = [3,4,5,6,7,9,10,11,12,13,14,15]
sub = [3,4,5,6,7,9,12,13,14,15]
subject_tp=[3,3,3,5,5,3,1,1,3,3,3,3]
s_tp=[3,3,3,5,5,3,3,3,3,3]

width = 0.35       # the width of the bars
ind = np.arange(len(s_tp))

increasel = []
increaser = []
row_count = 1
s_count = 0
sub_change=[]
for i in subject:
# for i in range(1):
    row_count += 1
    print(row_count)
    if subject_tp[s_count] > 1:
        row_count+=1
        print('subject',subject[s_count])
        templ = 0
        tempr = 0
        countl = 0
        countr = 0
        for j in range(subject_tp[s_count]-1):
            print(data[row_count+j][6])
            print(data[row_count+j][13])
            print('j',j)
            print(row_count+j)
            if (float(data[row_count+j][6]) <=0.4):
                templ = templ + float(data[row_count+j][6])*100
                countl += 1
            if (float(data[row_count+j][13]) <=0.4):
                tempr = tempr + float(data[row_count+j][13])*100
                countr += 1
        
        templ = templ/countl
        tempr = tempr/countr
        increasel.append(templ)
        increaser.append(tempr)
    else:
        row_count += 1
    row_count = row_count + subject_tp[s_count] - 1
    s_count += 1
    
rectl = ax.bar(np.arange(len(increasel)), increasel, width, color='b')
rectr = ax.bar(np.arange(len(increaser))+width, increaser, width, color='r')
ax.set_ylabel('Average Increase %')
ax.set_title('Average Increase % of subjects')

ax.legend((rectl[0], rectr[0]), ('Left', 'Right'))

def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.01*height,'%.3f' % float(height),ha='center', va='bottom')
            

ax.set_xticks(np.arange(np.max([len(increasel),len(increaser)]))+width/2)
ax.set_xticklabels(sub)
ax.set_xlabel('Subject')
autolabel(rectl)
autolabel(rectr)
plt.show()          