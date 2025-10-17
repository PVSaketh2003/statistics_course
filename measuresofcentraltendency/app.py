# 1) stats 2) numpy
import statistics as stats

data = [50,60,70,80,90,90,80,100]

print(" data ", data)

mean = stats.mean(data)
median = stats.median(data)
mode = stats.mode(data)

print("mean",mean)
print("median",median)
print("mode",mode)


