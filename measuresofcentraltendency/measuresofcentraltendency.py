#1) numpy 2) stats

import statistics as stats

data = [10,20,30,40,50,60,70,80,80,90,90,100]

print("data ",data)

#measures of central tendency
mean = stats.mean(data)
median = stats.median(data)
#to calculate mode - 2 appraoches
# 1) print only 1 mode -> use stats.mode
# 2) print all modes -> stats.multimode
mode = stats.mode(data)
multi_mode =  stats.multimode(data)

print("mean :",mean)
print("median :",median)
print("single mode :",mode)
print("multiple mode :",multi_mode)
